import pandas as pd
import numpy as np
class BookLover:
    def __init__(self, name,email,fav_genre,num_books = 0,book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        if rating < 0 or rating > 5:
             print("Rating must be between 0 and 5.")
             return
        if self.has_read(book_name):
            print(book_name," already found in book list.")
            return
        new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [rating]
        })
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1

    def has_read(self,book_name):
        return book_name in self.book_list.book_name.values

    def num_books_read(self):
        return self.num_books

    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]

