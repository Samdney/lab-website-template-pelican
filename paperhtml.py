#!/usr/bin/env python3

"""
- Reads the chosen HTML file from the source directory
- Extracts the content inside <body>...</body>
- Writes the new fixed-name file straight into the target directory
- Copies everything else from the source directory to the target directory
- Skips the original HTML file

$ python paperhtml.py /path/to/target
$ python paperhtml.py /path/to/target /path/to/source
$ python paperhtml.py /path/to/target /path/to/source --html-file index.html
"""


#!/usr/bin/env python3

import argparse
import re
import shutil
import unicodedata
from pathlib import Path
from html.parser import HTMLParser


DEFAULT_OUTPUT_NAME = "body_content.md"


class BodyExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_body = False
        self.body_depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "body":
            if not self.in_body:
                self.in_body = True
                self.body_depth = 1
            else:
                self.body_depth += 1
            return

        if self.in_body:
            attr_text = "".join(
                f' {name}="{value}"' if value is not None else f" {name}"
                for name, value in attrs
            )
            self.parts.append(f"<{tag}{attr_text}>")

    def handle_endtag(self, tag):
        if tag.lower() == "body" and self.in_body:
            self.body_depth -= 1
            if self.body_depth == 0:
                self.in_body = False
            return

        if self.in_body:
            self.parts.append(f"</{tag}>")

    def handle_startendtag(self, tag, attrs):
        if self.in_body:
            attr_text = "".join(
                f' {name}="{value}"' if value is not None else f" {name}"
                for name, value in attrs
            )
            self.parts.append(f"<{tag}{attr_text} />")

    def handle_data(self, data):
        if self.in_body:
            self.parts.append(data)

    def handle_comment(self, data):
        if self.in_body:
            self.parts.append(f"<!--{data}-->")

    def handle_entityref(self, name):
        if self.in_body:
            self.parts.append(f"&{name};")

    def handle_charref(self, name):
        if self.in_body:
            self.parts.append(f"&#{name};")

    def handle_decl(self, decl):
        if self.in_body:
            self.parts.append(f"<!{decl}>")

    def get_body_content(self):
        return "".join(self.parts)


class TitleExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_title = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.parts.append(data)

    def get_title(self):
        return "".join(self.parts).strip()


def extract_body_content(html_text: str) -> str:
    parser = BodyExtractor()
    parser.feed(html_text)
    parser.close()
    return parser.get_body_content()


def extract_title(html_text: str) -> str:
    parser = TitleExtractor()
    parser.feed(html_text)
    parser.close()
    return parser.get_title()


def normalize_to_ascii(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    return text.encode("ascii", "ignore").decode("ascii")


def title_to_filename(title: str) -> str:
    if not title.strip():
        return DEFAULT_OUTPUT_NAME

    filename = normalize_to_ascii(title.strip())
    filename = re.sub(r"\s+", "-", filename)
    filename = re.sub(r"[^a-zA-Z0-9._-]", "", filename)
    filename = re.sub(r"-{2,}", "-", filename)
    filename = filename.strip(".-")
    filename = filename.lower()

    if not filename:
        return DEFAULT_OUTPUT_NAME

    return f"{filename}.md"


def build_output_content(title: str, slug: str, body_content: str) -> str:
    return (
        f"title: {title}\n"
        f"slug: {slug}\n"
        f"category: paper\n"
        f"icon: fa-solid fa-users\n"
        f"\n"
        f"{body_content}"
    )


def copy_directory_contents(
    src_dir: Path,
    dst_dir: Path,
    original_html: Path,
    generated_filename: str,
) -> None:
    dst_dir.mkdir(parents=True, exist_ok=True)

    for item in src_dir.iterdir():
        if item.resolve() == original_html.resolve():
            continue
        if item.is_file() and item.name == generated_filename:
            continue

        target = dst_dir / item.name
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            shutil.copy2(item, target)


def find_first_html_file(source_dir: Path) -> Path:
    html_files = sorted(source_dir.glob("*.html"))
    if not html_files:
        raise FileNotFoundError(f"No HTML file found in directory: {source_dir}")
    return html_files[0]


def resolve_html_file(source_dir: Path, html_file_arg: str | None) -> Path:
    if html_file_arg is None:
        return find_first_html_file(source_dir)

    html_path = Path(html_file_arg).expanduser()

    if not html_path.is_absolute():
        html_path = source_dir / html_path

    html_path = html_path.resolve()

    if not html_path.exists():
        raise FileNotFoundError(f"Specified HTML file does not exist: {html_path}")

    if not html_path.is_file():
        raise FileNotFoundError(f"Specified HTML path is not a file: {html_path}")

    if html_path.suffix.lower() != ".html":
        raise ValueError(f"Specified file is not an .html file: {html_path}")

    try:
        html_path.relative_to(source_dir.resolve())
    except ValueError:
        raise ValueError("Specified HTML file must be inside the source directory.")

    return html_path


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Extract the content inside <body>...</body> from an HTML file in a source "
            "directory, write it to a new Markdown file in the target directory using "
            "the page title as the filename, prepend metadata, and copy the directory "
            "contents except the original HTML file."
        )
    )
    parser.add_argument(
        "target_dir",
        help="Directory where the generated file and copied content will be placed.",
    )
    parser.add_argument(
        "source_dir",
        nargs="?",
        default=".",
        help="Source directory containing the HTML file and related content. Defaults to current directory.",
    )
    parser.add_argument(
        "--html-file",
        dest="html_file",
        help=(
            "Exact HTML file to use. Can be a filename relative to source_dir "
            "or an absolute path inside source_dir."
        ),
    )
    return parser.parse_args()


def main():
    args = parse_args()

    source_dir = Path(args.source_dir).expanduser().resolve()
    target_dir = Path(args.target_dir).expanduser().resolve()

    if not source_dir.is_dir():
        print(f"Error: source directory does not exist or is not a directory: {source_dir}")
        raise SystemExit(1)

    target_dir.mkdir(parents=True, exist_ok=True)

    try:
        original_html = resolve_html_file(source_dir, args.html_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        raise SystemExit(1)

    html_text = original_html.read_text(encoding="utf-8", errors="replace")

    body_content = extract_body_content(html_text)
    title = extract_title(html_text)

    if not body_content.strip():
        print(f"Warning: no <body> content found in '{original_html.name}'.")

    if not title:
        print(f"Warning: no <title> found in '{original_html.name}'. Using default filename.")
        title = "Untitled"

    generated_filename = title_to_filename(title)
    generated_file = target_dir / generated_filename
    slug = Path(generated_filename).stem
    output_content = build_output_content(title, slug, body_content)

    generated_file.write_text(output_content, encoding="utf-8")

    copy_directory_contents(
        source_dir,
        target_dir,
        original_html,
        generated_filename,
    )

    print(f"Source directory: {source_dir}")
    print(f"Original HTML:    {original_html.name}")
    print(f"Page title:       {title}")
    print(f"Generated file:   {generated_file}")
    print(f"Target directory: {target_dir}")


if __name__ == "__main__":
    main()
    
