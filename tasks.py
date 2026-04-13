
from invoke import task

@task
def build(c):
    c.run('pelican content -s pelicanconf.py')

@task
def serve(c):
    c.run('python -m http.server 8000 -d output')
