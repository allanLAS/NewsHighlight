from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, get_sources, get_articles
from ..models import Sources, Articles


# Views
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    :return:
    """

    # Get top headlines
    # top_headlines = get_news()
    # print(top_headlines)

    sources = get_sources('business')
    sports = get_sources('sports')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')

    print(sources)

    # general = get_sources('general')
    title = 'News Highlights'
    return render_template('index.html', txt=title, sources=sources, sports=sports,
                           technology=technology, entertainment=entertainment)


@main.route('/article/<id>')
def articles(id):
    """
    View news articles from a single news source
    :param id:
    :return:
    """
    articles = get_articles(id)
    title = f'{id}'


    return render_template('articles.html', articles=articles, title=title)



