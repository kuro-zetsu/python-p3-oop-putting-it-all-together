#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
    
    @property
    def title(self):
        """The title of the book"""
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    @property
    def page_count(self):
        """The current page"""
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        self._page_count += 1
