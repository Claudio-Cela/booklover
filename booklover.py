import pandas as pd
import numpy as np

class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = None): 
        if book_list is None: # had to make book list = to none otherwise modifying one object instance would modify others (they would share the same dataframe)
            book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self, book_name, rating):
        if book_name in self.book_list['book_name'].values:
            print("This book is already in the list")
        else:
            new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [rating]
                })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
        
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        fav_filtered = self.book_list[self.book_list['book_rating']>3]
        return fav_filtered
    
    
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)