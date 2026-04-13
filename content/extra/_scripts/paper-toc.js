document.addEventListener("DOMContentLoaded", function () {
  const content = document.getElementById("paper-content");
  const tocContainer = document.getElementById("paper-toc");
  
  if (!content || !tocContainer) return;

  const headings = Array.from(
    /*content.querySelectorAll("h1, h2, h3, h4")*/
    content.querySelectorAll("h2, h3, h4, h5, h6")
  ).filter((el) => el.textContent.trim().length > 0);

  if (!headings.length) return;

  function slugify(text) {
    return text
      .trim()
      .toLowerCase()
      .replace(/[\u2013\u2014]/g, "-")
      .replace(/[^\w\s-]/g, "")
      .replace(/\s+/g, "-")
      .replace(/-+/g, "-")
      .replace(/^-|-$/g, "");
  }

  const used = new Set();

  function uniqueId(base) {
    let id = base || "section";
    let i = 2;
    while (used.has(id) || document.getElementById(id)) {
      id = `${base || "section"}-${i++}`;
    }
    used.add(id);
    return id;
  }

  headings.forEach((h, i) => {
    if (!h.id) h.id = uniqueId(slugify(h.textContent) || `section-${i + 1}`);
  });

  const rootList = document.createElement("ul");
  rootList.className = "paper-toc-list";

  const stack = [{ level: 0, list: rootList }];
  const linksById = new Map();

  function levelOf(tagName) {
    return Number(tagName.slice(1));
  }

  headings.forEach((heading) => {
    const level = levelOf(heading.tagName);
    const item = document.createElement("li");
    item.className = `paper-toc-item paper-toc-${heading.tagName.toLowerCase()}`;

    const link = document.createElement("a");
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent.trim();
    link.dataset.targetId = heading.id;

    item.appendChild(link);
    linksById.set(heading.id, link);

    while (stack.length > 1 && level <= stack[stack.length - 1].level) {
      stack.pop();
    }

    stack[stack.length - 1].list.appendChild(item);

    const sublist = document.createElement("ul");
    item.appendChild(sublist);

    stack.push({ level, list: sublist });
  });

  rootList.querySelectorAll("ul").forEach((ul) => {
    if (!ul.children.length) ul.remove();
  });

  tocContainer.appendChild(rootList);

  function setActive(id) {
    tocContainer.querySelectorAll("a.active").forEach((a) => {
      a.classList.remove("active");
    });
    const active = linksById.get(id);
    if (active) active.classList.add("active");
  }

  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((e) => e.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);

      if (visible.length) setActive(visible[0].target.id);
    },
    {
      rootMargin: "0px 0px -70% 0px",
      threshold: [0, 0.1, 0.5],
    }
  );

  headings.forEach((h) => observer.observe(h));

  tocContainer.addEventListener("click", function (event) {
    const link = event.target.closest("a[data-target-id]");
    if (!link) return;

    const id = link.dataset.targetId;
    const target = document.getElementById(id);
    if (!target) return;

    event.preventDefault();
    const y = target.getBoundingClientRect().top + window.pageYOffset - 80;

    window.scrollTo({ top: y, behavior: "smooth" });
    history.pushState(null, "", `#${id}`);
    setActive(id);
  });
});
