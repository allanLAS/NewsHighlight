
import urllib.request, json
from .models import Sources, Articles, News

# Getting api key
api_key = None
# Getting the news and article base url
news_base_url = None
article_base_url = None
source_base_url = None
search_base_url = None


def configure_request(app):
    global api_key, news_base_url, article_base_url, source_base_url
    api_key = app.config['NEWS_API_KEY']
    news_base_url = app.config['NEWS_API_BASE_URL']
    article_base_url = app.config['ARTICLE_API_BASE_URL']
    source_base_url = app.config['SOURCE_API_BASE_URL']


def process_results(news_list):
    """
    Processes movie results obtained by api
    :param news_list: list of news objects
    :return: news_results: list of new objects
    """

    news_results = []
    for news_item in news_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        image_url = news_item.get('urlToImage')
        published = news_item.get('publishedAt')
        content = news_item.get('content')

        if image_url:
            news_object = News(author, title, description, image_url, published)
            news_results.append(news_object)

    return news_results


def get_news():
    """
    Gets json response to our url request
    :param source:
    :return:
    """
    get_news_url = news_base_url.format(api_key)
    print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_sources(news_results_list)

    return news_results


def get_sources(category):
    get_sources_url = source_base_url.format(category, api_key)
    print(get_sources_url)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    """
    This function processes the sources result
    :param sources_list: A list of dictionaries
    :return: A list of source objects
    """
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        print(sources_item)
        sources_object = Sources(id, name, description, url)
        sources_results.append(sources_object)

    return sources_results


def get_articles(id):
    """
    Function that gets the json response to our url request
    """
    get_articles_url = article_base_url.format(id, api_key)
    print(get_articles_url)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_results=None
        if articles_details_response['articles']:
            articles_results_list = articles_details_response['articles']
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
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')

        article_object = Articles(author, title, description, url, urlToImage, publishedAt, content)
        articles_results.append(article_object)

    return articles_results


def search_news(keyword):
    url = search_base_url.format(keyword, api_key)

    with urllib.request.urlopen(search_base_url) as response:
        data = json.loads(response.read())

        articles = []

        if data['articles']:
            articles_list = data['articles']
            articles = process_articles(articles_list)

    return articles
