from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources, get_articles
from ..models import Sources, Articles


# Views
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    :return:
    """

    news_sources = get_sources()
    title = 'News Feed'
    return render_template('index.html', title=title, sources=news_sources)


@main.route('/articles/<id>')
def articles(id):
    """
    View news articles from a single news source
    :param id:
    :return:
    """
    article = get_articles(id)
    title = f'{id}'
    id_articles = id

    return render_template('articles.html', article=article, name=id)



