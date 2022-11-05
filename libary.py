import sqlite3

import time


class Book():
    def __init__(self, name, writer, publisher, category, oppression):
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.category = category
        self.oppression = oppression

    def __str__(self):
        return "Kitap İsmi: {} \n Yazar: {} \n Yayın Evi: {} \n Tür: {} \n Baskı: {} \n".format(self.name,
                                                                                                self.writer,
                                                                                                self.publisher,
                                                                                                self.category,
                                                                                                self.oppression)


class Libary:

    def __init__(self):
        self.connect()

    def connect(self):
        self.con = sqlite3.connect("libary.db")

        self.cursor = self.con.cursor()

        question = "Create Table if not exists books (name TEXT, writer TEXT, publisher TEXT, category TEXT, oppression INT)"

        self.cursor.execute(question)

        self.con.commit()

    def disconnect(self):
        self.con.close()

    def show_books(self):
        ques = "Select * From books"
        self.cursor.execute(ques)
        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Kütüphanede hiçbir kitap yok")
        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)

    def question_book(self, name):

        ques = "Select * From books Where name = ?"
        self.cursor.execute(ques, (name,))

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("Böyle bir kitap bulunmuyor")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            print(book)

    def create_book(self, book):
        ques = "Insert Into books Values(?,?,?,?,?)"

        self.cursor.execute(ques, (book.name, book.writer, book.publisher, book.category, book.oppression))

        self.con.commit()

    def delete_book(self, name):
        ques = "Delete from books Where name= ? "

        self.cursor.execute(ques, (name,))

        self.con.commit()

    def oppression_increase(self, name):
        ques = "Select * from books where name = ?"

        self.cursor.execute(ques, (name,))

        books = self.cursor.fetchall()

        if len(books) == 0:
            print("Böyle bir kitap bulunmuyor")
        else:
            oppression = books[0][4]
            oppression += 1

            second_ques = "Update books Set oppression = ? where name = ?"

            self.cursor.execute(second_ques, (oppression, name))

            self.con.commit()
