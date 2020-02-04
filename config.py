import os


class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = '03d3f69ba4844b8e94dc1582f0dc69b9'
    NEWS_API_BASE_URL = "https://newsapi.org/v2/sources?&language=en&apiKey={}"

    ARTICLE_API_BASE_URL = "https://newsapi.org/v2/everything?sources={}&apiKey={}"


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