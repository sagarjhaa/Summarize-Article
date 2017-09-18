"""
Routes and views for the bottle application.
"""

from bottle import route, view , get,post,request
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        OriginalText = 'Orignal',
        Summary = 'String'
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )


@post('/login')
@view('index')
def do_post():
    
    articleUrl = request.forms.get('articleURL')
    no_of_lines = request.forms.get('noOfLines')

    #Get the original text
    #Get the summarized text

    text = getTextWaPo(articleUrl);

    return dict(year = datetime.now().year,
                OriginalText=text,
                Summary="Summary -Sagar Jha")
   



def getTextWaPo(url):
    page = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,'html.parser')
    text = ' '.join(map(lambda p: p.text,soup.find_all('article')))
    return str(text.encode('ascii',errors='replace')).replace('?'," ")
