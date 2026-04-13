html:
	pelican content -s pelicanconf.py

serve:
	python -m http.server 8000 -d output

preview: html serve
