import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}"

    ARTICLE_API_BASE_URL = "https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}"
    SOURCE_API_BASE_URL = "https://newsapi.org/v2/sources?language=en&category={}&apiKey={}"


class ProdConfig(Config):
    '''
    Production This is a configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    ENV = 'development'


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
