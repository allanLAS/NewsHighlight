class News:
    """
    News class to define news
    """

    def __init__(self, author, title, description, urlToImage, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content


class Sources:
    """
     News class to define News sources
    """

    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Articles:
    """
    News articles
    """

    def __init__(self, author, title, description, url, image_url, publishedAt, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.image_url = image_url
        self.publishedAt = publishedAt
        self.content = content

