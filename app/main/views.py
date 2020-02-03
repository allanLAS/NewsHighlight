from flask import render_template
from . import main
from ..requests import get_sources, get_article
from ..models import Sources, Articles


# Views
@main.route('/')
def index():
    """
    View root page function that returns the index page and its data
    :return:
    """

    # Trending news headline
    trending_headlines = get_news('Trending')
    print(trending_headlines)

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
    article = get_article(id)
    title = f'{id}'
    id_articles = id

    return render_template('articles.html', article=article, name=id)
