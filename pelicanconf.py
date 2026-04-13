from __future__ import unicode_literals
import os, yaml
from datetime import datetime
from pathlib import Path

def parse_date(value):
    return datetime.strptime(value, "%Y-%m-%d")

JINJA_FILTERS = {
    'parse_date': parse_date,
}
    

AUTHOR = "Lab Website Template"
SITENAME = 'Lab Website Template'
SITESUBTITLE = 'by the Greene Lab'
SITEDESCRIPTION = 'An easy-to-use, flexible website template for labs, with automatic citations, GitHub tag imports, pre-built components, and more.'
SITEURL = ""
PATH = "content"
DEFAULT_LANG = "en"
LOCALE = ["en_US.UTF-8", "en_US", "English_United States.1252"]
TIMEZONE = "Europe/Berlin"
THEME = "themes/lab"
STATIC_PATHS = ['images', '_styles', '_scripts', 'papers']
PAGE_PATHS = ['pages']
PATH_METADATA = r"pages/(?P<path_no_ext>(?:.*/)?)[^/]+\.[^.]+$" ###
#PATH_METADATA = r"pages/(?P<path_no_ext>.+)\..+" # Necessary for working subfolder slug within the page path folder
ARTICLE_PATHS = ['articles']
DIRECT_TEMPLATES = ['index', 'archives']
PAGE_URL = "{path_no_ext}{slug}" ###
PAGE_SAVE_AS = "{path_no_ext}{slug}/index.html" ###
#PAGE_URL = "{path_no_ext}/"
#PAGE_SAVE_AS = "{path_no_ext}/index.html"
#PAGE_URL = '{slug}/'
#PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
DEFAULT_PAGINATION = False
DEFAULT_DATE = 'fs'
RELATIVE_URLS = True
PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math', 'neighbors']


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
MATH_JAX = {
    'auto_insert': False, # True
    'align': 'left',
    'process_escapes': True,
    'tex_extensions': ['ams','color','mhchem'],
}

ROOT = Path(__file__).resolve().parent
with open(ROOT / 'data' / 'projects.yaml', 'r', encoding='utf-8') as fh:
    PROJECTS = yaml.safe_load(fh) or []
with open(ROOT / 'data' / 'types.yaml', 'r', encoding='utf-8') as fh:
    TYPES = yaml.safe_load(fh) or {}    
with open(ROOT / 'data' / 'citations.yaml', 'r', encoding='utf-8') as fh:
    CITATIONS = yaml.safe_load(fh) or []
MEMBERS = [
	{
		'name': 'Jane Smith',
	 	'image': 'photo.jpg',
	 	'role': 'principal-investigator',
	 	'affiliation': 'University of Colorado',
	 	'aliases': ['J. Smith', 'J Smith'],
	 	'links': {'home-page': 'https://janesmith.com', 'orcid': '0000-0001-8713-9213'},
	 	'division': 'lab/members',
	 	'slug': 'jane-smith',
	 	'slogan': 'The world is small',
	 	'shortbio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nFaucibus purus in massa tempor nec feugiat nisl pretium fusce.\nElit at imperdiet dui accumsan.\nDuis tristique sollicitudin nibh sit amet commodo nulla facilisi.\nVitae elementum curabitur vitae nunc sed velit dignissim sodales.\nLacinia at quis risus sed vulputate odio ut.\nMagna eget est lorem ipsum.'
	 },
	 {
	 	'name': 'John Doe',
	 	'image': 'photo.jpg',
	 	'role': 'phd',
	 	'group': 'alum',
	 	'links': {'github': 'john-doe'},
	 	'division': 'lab/members',
	 	'slug': 'john-doe',
	 	'slogan': 'The planet is huge',
	 	'shortbio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
	 }, 
	 {
	 	'name': 'Sarah Johnson',
	 	'image': 'photo.jpg',
	 	'description': 'Lead Programmer',
	 	'role': 'programmer',
	 	'links': {'email': 'sarah.johnson@gmail.com', 'twitter': 'sarahjohnson'},
	 	'division': 'lab/members',
	 	'slug': 'sarah-johnson',
	 	'slogan': 'My mind is funny',
	 	'shortbio': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
	 }
	]
LAB_LINKS = {'email': 'contact@your-lab.com', 'orcid': '0000-0001-8713-9213', 'google-scholar': 'ETJoidYAAAAJ', 'github': 'your-lab', 'twitter': 'YourLabHandle', 'youtube': 'YourLabChannel'}

NAV_PAGES = [
    {'title':'Research','slug':'research','tooltip':'What the heck we are working on!?','order':1},
    {'title':'Projects','slug':'projects','tooltip':'Software, datasets, and more','order':2},
    {'title':'Publications','slug':'publications','tooltip':'Published works','order':3},
    {'title':'Lab','slug':'lab','tooltip':'About our lab and team','order':4},
    {'title':'Collaborations','slug':'collaborations','tooltip':'Research friends and family','order':5},
    {'title':'Funding/IR','slug':'funding','tooltip':'Money and investor relations','order':6},
    {'title':'Teaching','slug':'teaching','tooltip':'Musings and miscellany','order':7},
    {'title':'News','slug':'news','tooltip':'News from the lab','order':8},
    {'title':'Outreach','slug':'outreach','tooltip':'Outreach from the lab','order':9},
    {'title':'Blog','slug':'blog','tooltip':'Musings and miscellany','order':10},
    {'title':'Contact','slug':'contact','tooltip':'Email, address, and location','order':11},
]

#NAV_PAGES = [
#    {'title':'Research','slug':'research','tooltip':'Published works','order':1},
#    {'title':'Projects','slug':'projects','tooltip':'Software, datasets, and more','order':2},
#    {'title':'Team','slug':'team','tooltip':'About our team','order':3},
#    {'title':'Blog','slug':'blog','tooltip':'Musings and miscellany','order':4},
#    {'title':'Contact','slug':'contact','tooltip':'Email, address, and location','order':5},
#]

# Sort CITATIONS by year in inverse order
CITATIONS.sort(key = lambda x: datetime.strptime(x['date'], '%Y-%m-%d'), reverse=True)

# Define individual CITATIONS HIGHLIGHTS by title, default newest entry
#HIGHLIGHTSCIT = []
HIGHLIGHTSCIT = ['Constructing knowledge graphs and their biomedical applications', 'Open collaborative writing with Manubot', 'Integration of 168,000 samples reveals global patterns of the human gut microbiome']
HIGHLIGHTSCIT = [h if any(c['title'] == h for c in CITATIONS) else '' for h in HIGHLIGHTSCIT]
HIGHLIGHTSCIT = [next((index for (index, c) in enumerate(CITATIONS) if c['title'] == h), '') for h in HIGHLIGHTSCIT]


JINJA_GLOBALS = {
    'PROJECTS': PROJECTS,
    'TYPES': TYPES,
    'CITATIONS': CITATIONS,
    'CITATIONS_PAGINATION': False,
    'CITATIONS_PER_PAGE': 6,
    'HIGHLIGHTSCIT': HIGHLIGHTSCIT,
    'MEMBERS': MEMBERS,
    'MEMBER_MAP': {m['slug']: m for m in MEMBERS},
    'LAB_LINKS': LAB_LINKS,
    'NAV_PAGES': NAV_PAGES,
   	'FONTS_URL': 'https://fonts.googleapis.com/css2?family=Barlow:wght@200;400;500;600&family=Roboto+Mono:wght@200;400;500;600&family=false:wght@200;400;500;600&family=true:wght@200;400;500;600&display=swap',
    'HEADER_IMAGE': '/images/background.jpg',
    'FOOTER_IMAGE': '/images/background.jpg',
    'CURRENT_DATE': datetime.now(),
    'categories_dict': {
        'News': 'News',
        'Outreach': 'Outreach',
        'Blog': 'Blog',
    },
}


FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
