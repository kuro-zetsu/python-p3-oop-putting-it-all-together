#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition = "Used"):
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def brand(self):
        """The brand of the shoe"""
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        """The size of the shoe"""
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"