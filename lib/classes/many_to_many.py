class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        categories = list(set(mag.category for mag in self.magazines()))
        return categories if categories else None


class Magazine:
    all = []
    
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            print("Invalid categorie provide")
            raise ValueError("Category must be a non-empty string.")
            
        
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            print("INVALID CATEGORY")
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list(set(article.author for article in self.articles()))
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
        
        contributors = [author for author, count in author_count.items() if count > 2]
        return contributors if contributors else None
    
    @classmethod
    def top_publisher(cls):
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)


class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
