class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(author, Author):
            raise ValueError("Invalid author. Must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Invalid magazine. Must be an instance of Magazine.")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        # Get all articles written by this author
        return [article for article in Article.all if article.author == self]

    @property
    def magazines(self):
        # Get a unique list of magazines the author has written for
        return list({article.magazine for article in self.articles})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise ValueError("Invalid magazine. Must be an instance of Magazine.")
        return Article(self, magazine, title)

    @property
    def topic_areas(self):
     return list({magazine.category for magazine in self.magazines})


class Magazine:
    def __init__(self, name, category):
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        if not isinstance(category, str) or len(category.strip()) == 0:
            raise ValueError("Category cannot be empty.")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category cannot be empty.")
        self._category = value

    @property
    def articles(self):
        # Get all articles for this magazine
        return [article for article in Article.all if article.magazine == self]

    @property
    def contributors(self):
        # Get a unique list of authors who contributed to this magazine
        return list({article.author for article in self.articles})

    def article_titles(self):
        # Get the titles of all articles in this magazine
        return [article.title for article in self.articles]

    def contributing_authors(self):
        # Get authors who contributed more than 2 articles to this magazine
        author_article_count = {}
        for article in self.articles:
            author_article_count[article.author] = author_article_count.get(article.author, 0) + 1
        return [author for author, count in author_article_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        # Find the magazine with the most articles
        magazines = {article.magazine for article in Article.all}
        if not magazines:
            return None
        return max(magazines, key=lambda mag: len(mag.articles))
