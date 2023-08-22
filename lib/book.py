#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!") 

if __name__ == "__main__":
    book = Book("And Then There Were None", 272)
    print(book.title)
    print(book.page_count)
    book.turn_page()
    
    
        