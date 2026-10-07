class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contracts(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        all_royalties = [contract.royalties for contract in Contract.all if contract.author == self]
        return sum(all_royalties)
        


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError
        self._author = value
    
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise ValueError
        self._book = value
    
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise ValueError
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise ValueError
        self._royalties = value
        
    def contracts_by_date(self, date):
        return [contract for contract in Contract.all if contract.date == date]