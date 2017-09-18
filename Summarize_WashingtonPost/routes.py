"""
Routes and views for the bottle application.
"""

from bottle import route, view , get,post,request
from datetime import datetime
import urllib.request
from bs4 import BeautifulSoup


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

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


@post('/summarize')
@view('index')
def do_post():
    

    default_no_of_lines = 3
    articleUrl = request.forms.get('articleURL')
    no_of_lines = request.forms.get('noOfLines')

    #Get the original text
    #Get the summarized text
    if 'washingtonpost' in articleUrl:
        

        text = getTextWaPo(articleUrl);

        if no_of_lines != "" :
            default_no_of_lines = int(no_of_lines)


        summary = summarize(text,default_no_of_lines)

        return dict(year = datetime.now().year,OriginalText=text,Summary='summary')

    return dict(year = datetime.now().year,OriginalText="Sorry we only process washington post articles only!!",Summary=" ")



def getTextWaPo(url):
    page = urllib.request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,'html.parser')
    text = ' '.join(map(lambda p: p.text,soup.find_all('article')))
    return str(text.encode('ascii',errors='replace')).replace('?'," ")


def summarize(text,n):
    try:

        sents = sent_tokenize(text)
        assert n <= len(sents)

        word_sents = word_tokenize(text.lower())
        #_stopwords = set(stopwords.words('english') + list(punctuation))

        #word_sent = [word for word in word_sents if word not in _stopwords]
        freq = FreqDist(word_sent)

        ranking = defaultdict(int)

        for i,sent in enumerate(sents):
            for w in word_tokenize(sent.lower()):
                if w in freq:
                    ranking[i] += freq[w]

        sents_idx = nlargest(n,ranking,key = ranking.get)
        summary =  [sents[j] for j in sorted(sents_idx)]

        return ' '.join(summary)

    except:
        return sys.exc_info()[0]
