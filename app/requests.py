import urllib.request, json
from .models import Sources, Articles

# Getting api key
api_key = None
# Getting the news and article base url
news_url = None
article_url = None


def configure_request(app):
    global api_key, news_url, article_url
    api_key = app.config['NEWS_API_KEY']
    news_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLE_API_BASE_URL']


def get_articles(id):
    """
    Function that gets the json response to our url request
    """
    get_articles_url = article_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results


def process_articles(articles_list):
    """
    This is a function that processes the articles result and transform them to a list of articles
    Args:
        articles_list: A list of dictionaries that contain articles
    Returns :
        articles_results: A list of article objects
    """
    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        title = articles_item.get('title')
        url = articles_item.get('url')
        image = articles_item.get('urlToImage')
        content = articles_item.get('content')
        publishedAt = articles_item.get('publishedAt')

        if image:
            article_object = Articles(id, name, title, url, image, content, publishedAt)
            articles_results.append(article_object)

    return articles_results


def get_sources():
    """
    Function that gets the json response to our url request
    """
    get_sources_url = news_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    """
    Function  that processes the news result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    """
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')

        source_object = Sources(id, name, description, url)
        sources_results.append(source_object)

    return sources_results
