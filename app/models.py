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

    def __init__(self, id, name, title, url, urlToImage, content, publishedAt):
        self.id = id
        self.name = name
        self.title = title
        self.url = url
        self.urlToImage = urlToImage
        self.content = content
        self.publishedAt = publishedAt
