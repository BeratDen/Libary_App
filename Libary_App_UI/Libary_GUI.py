from depency import *


class Book(QWidget):
    def __init__(self, name, writer, publisher, category, oppression):
        super(Book, self).__init__()
        self.name = name
        self.writer = writer
        self.publisher = publisher
        self.category = category
        self.oppression = oppression

        self.init_ui()

    def init_ui(self):
        self.book_name = QLabel()
        self.book_writer = QLabel()
        self.book_publisher = QLabel()
        self.book_category = QLabel()

        self.book_name.setText(self.name)
        self.book_writer.setText(self.writer)
        self.book_publisher.setText(self.publisher)
        self.book_category.setText(self.category)

        v_box = QVBoxLayout()

        v_box.addWidget(self.book_name)
        v_box.addWidget(self.book_writer)
        v_box.addWidget(self.book_publisher)
        v_box.addWidget(self.book_category)

        v_box2 = QVBoxLayout()

        v_box2.addLayout(v_box)

        self.setLayout(v_box2)
        self.setStyleSheet('border:2px solid black')


class LoginWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.connect()
        self.init_ui()

    def connect(self):
        con = sqlite3.connect("libary.db")

        self.cursor = con.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (user_name TEXT,user_password TEXT)")

        con.commit()

    def init_ui(self):
        font = self.font()
        font.setPointSize(24)
        font.bold()
        self.user_Name = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.btn = QPushButton("Giriş Yap")
        self.write_line = QLabel("")
        self.pageTitle = QLabel("Giriş Yap")
        self.pageTitle.setFont(font)

        v_box = QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.pageTitle)
        v_box.addWidget(self.user_Name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.write_line)
        v_box.addStretch()
        v_box.addWidget(self.btn)
        v_box.addStretch()

        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Kullanıcı Girişi")

        self.btn.clicked.connect(self.login)

    def login(self):
        userName = self.user_Name.text()
        password = self.password.text()

        self.cursor.execute("SELECT * FROM users WHERE user_name = ? and user_password = ? ", (userName, password))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.write_line.setText("Böyle Bir kullanıcı yok\n Lütfen Tekrar Deneyin.")
        else:
            self.gotoScreen2()

    def gotoScreen2(self):
        mainWidow = MainWindow()
        widget.addWidget(mainWidow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class MainWindow(QDialog):
    def __init__(self):

        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):

        self.quit = QPushButton("Çıkış")

        v_box = QVBoxLayout()
        grid = QGridLayout()

        names = ["Kitapları Göster", "Kitap Sorgulama", "Kitap Ekle", "Kitap Sil", "Baskı Yükselt"]
        positions = [(i, j) for i in range(3) for j in range(2)]

        self.listOfBtns = []

        for position, name in zip(positions, names):
            if name == '':
                continue
            btn = QPushButton(name)
            self.listOfBtns.append(btn)
            grid.addWidget(btn, *position)

        v_box.addLayout(grid)

        self.quit.clicked.connect(self.quitApp)

        v_box.addWidget(self.quit)
        self.setLayout(v_box)

        for i in self.listOfBtns:
            i.clicked.connect(self.response)

    def quitApp(self):
        app.quit()

    def response(self):
        sender = self.sender()
        if sender.text() == "Kitapları Göster":
            show_books = ShowBooks()
            widget.addWidget(show_books)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        elif sender.text() == "Kitap Sorgulama":
            quest_book = QuestBook()
            widget.addWidget(quest_book)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        elif sender.text() == "Kitap Ekle":
            create_book = CreateBook()
            widget.addWidget(create_book)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            pass
        elif sender.text() == "Kitap Sil":
            delete_book = DeleteBook()
            widget.addWidget(delete_book)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        elif sender.text() == "Baskı Yükselt":
            increase_opp = Oppression_Increase()
            widget.addWidget(increase_opp)
            widget.setCurrentIndex(widget.currentIndex() + 1)

    # def gotoScreen1(self):
    #    screen1 = MainWindows()
    #    widget.addWidget(screen1)
    #    widget.setCurrentIndex(widget.currentIndex() + 1)


class ShowBooks(QDialog):
    def __init__(self):
        super(ShowBooks, self).__init__()

        self.connect()
        self.init_ui()

    def connect(self):
        self.con = sqlite3.connect("libary.db")

        self.cursor = self.con.cursor()

        question = "Create Table if not exists books (name TEXT, writer TEXT, publisher TEXT, category TEXT, oppression INT)"

        self.cursor.execute(question)

        self.con.commit()

    def disconnectDb(self):
        self.con.close()

    def init_ui(self):
        grid = QGridLayout()
        v_box = QVBoxLayout()

        self.btn_return = QPushButton("Geri")
        self.btn_return.clicked.connect(self.backToHome)

        ques = "Select * from books"
        self.cursor.execute(ques)

        books = self.cursor.fetchall()

        positions = [(row, columns) for row in range(4) for columns in range(4)]
        if len(books) == 0:
            print("Kütüphanede kitap yok")
        else:
            for i, position in zip(books, positions):
                book = Book(i[0], i[1], i[2], i[3], i[4])
                grid.addWidget(book, *position)

        v_box.addWidget(self.btn_return)

        v_box.addLayout(grid)

        self.setLayout(v_box)

    def backToHome(self):
        mainWidow = MainWindow()
        widget.addWidget(mainWidow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class QuestBook(QDialog):
    def __init__(self):
        super(QuestBook, self).__init__()
        self.connect()
        self.init_ui()

    def connect(self):
        self.con = sqlite3.connect("libary.db")

        self.cursor = self.con.cursor()

        question = "Create Table if not exists books (name TEXT, writer TEXT, publisher TEXT, category TEXT, oppression INT)"

        self.cursor.execute(question)

        self.con.commit()

    def init_ui(self):
        self.book_name = QLineEdit()
        self.btn = QPushButton("Sorgula")
        self.btn_return = QPushButton("Geri")

        self.v_box = QVBoxLayout()

        self.v_box.addWidget(self.book_name)
        self.v_box.addWidget(self.btn)

        self.btn.clicked.connect(self.quest)
        self.btn_return.clicked.connect(self.backToHome)

        self.v_box.addWidget(self.btn_return)

        self.setLayout(self.v_box)

    def backToHome(self):
        mainWidow = MainWindow()
        widget.addWidget(mainWidow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def quest(self):
        name = self.book_name.text()

        ques = "Select * From books Where name = ?"

        self.cursor.execute(ques, (name,))

        books = self.cursor.fetchall()
        if len(books) == 0:
            print("Böyle bir kitap bulunmuyor")
        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])
            self.v_box.addWidget(book)


class CreateBook(QDialog):
    def __init__(self):
        super(CreateBook, self).__init__()

        self.connect()
        self.init_ui()

    def init_ui(self):
        self.book_name = QLineEdit()
        self.book_writer = QLineEdit()
        self.book_publisher = QLineEdit()
        self.book_category = QLineEdit()
        self.book_opperssion = QLineEdit()

        self.placeholder1 = QLabel("Kitap Adı:")
        self.placeholder2 = QLabel("Kitap Yazarı:")
        self.placeholder3 = QLabel("Basım Evi:")
        self.placeholder4 = QLabel("Kitap Kategorisi:")
        self.placeholder5 = QLabel("Kitap Baskı Sayısı:")
        self.label = QLabel("")

        self.btn_create = QPushButton("Oluştur")
        self.btn = QPushButton("Geri")

        grid = QGridLayout()

        grid.addWidget(self.placeholder1, 0, 0)
        grid.addWidget(self.book_name, 0, 1)

        grid.addWidget(self.placeholder2, 2, 0)
        grid.addWidget(self.book_writer, 2, 1)

        grid.addWidget(self.placeholder3, 3, 0)
        grid.addWidget(self.book_publisher, 3, 1)

        grid.addWidget(self.placeholder4, 4, 0)
        grid.addWidget(self.book_category, 4, 1)

        grid.addWidget(self.placeholder5, 5, 0)
        grid.addWidget(self.book_opperssion, 5, 1)

        v_box = QVBoxLayout()

        v_box.addLayout(grid)
        v_box.addWidget(self.label)
        v_box.addWidget(self.btn_create)
        v_box.addWidget(self.btn)

        self.btn_create.clicked.connect(self.createBook)
        self.btn.clicked.connect(self.backToHome)

        self.setLayout(v_box)

    def backToHome(self):
        mainWidow = MainWindow()
        widget.addWidget(mainWidow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def connect(self):
        self.con = sqlite3.connect("libary.db")

        self.cursor = self.con.cursor()

        question = "Create Table if not exists books (name TEXT, writer TEXT, publisher TEXT, category TEXT, oppression INT)"

        self.cursor.execute(question)

        self.con.commit()

    def createBook(self):
        ques = "Insert Into books Values(?,?,?,?,?)"
        book_name = self.book_name.text()
        book_writer = self.book_writer.text()
        book_publisher = self.book_publisher.text()
        book_category = self.book_category.text()
        book_opperssion = self.book_opperssion.text()

        self.cursor.execute(ques, (book_name, book_writer, book_publisher, book_category, book_opperssion))

        self.con.commit()

        self.label.setText("Kitap Eklendi")

        self.book_name.clear()
        self.book_writer.clear()
        self.book_publisher.clear()
        self.book_category.clear()
        self.book_opperssion.clear()


class DeleteBook(QDialog):
    def __init__(self):
        super(DeleteBook, self).__init__()
        self.connect()
        self.init_ui()

    def connect(self):
        self.con = sqlite3.connect("libary.db")

        self.cursor = self.con.cursor()

        question = "Create Table if not exists books (name TEXT, writer TEXT, publisher TEXT, category TEXT, oppression INT)"

        self.cursor.execute(question)

        self.con.commit()

    def init_ui(self):
        self.book_name = QLineEdit()
        self.btn = QPushButton("Sil")
        self.btn_return = QPushButton("Geri")
        self.label = QLabel("")

        self.v_box = QVBoxLayout()

        self.v_box.addWidget(self.book_name)
        self.v_box.addWidget(self.btn)

        self.btn.clicked.connect(self.quest)
        self.btn_return.clicked.connect(self.backToHome)

        self.v_box.addWidget(self.btn_return)
        self.v_box.addWidget(self.label)

        self.setLayout(self.v_box)

    def backToHome(self):
        mainWidow = MainWindow()
        widget.addWidget(mainWidow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def quest(self):
        name = self.book_name.text()

        ques = "Delete from books Where name= ? "

        self.cursor.execute(ques, (name,))

        self.con.commit()

        self.label.setText("Kitap Silindi")
        self.book_name.clear()


class Oppression_Increase(QDialog):
    def __init__(self):
        super(Oppression_Increase, self).__init__()
        self.connect()
        self.init_ui()

    def connect(self):
        self.con = sqlite3.connect("libary.db")

        self.cursor = self.con.cursor()

        question = "Create Table if not exists books (name TEXT, writer TEXT, publisher TEXT, category TEXT, oppression INT)"

        self.cursor.execute(question)

        self.con.commit()

    def init_ui(self):
        self.book_name = QLineEdit()
        self.btn = QPushButton("Baskı Yükselt")
        self.btn_return = QPushButton("Geri")
        self.label = QLabel("")

        self.v_box = QVBoxLayout()

        self.v_box.addWidget(self.book_name)
        self.v_box.addWidget(self.btn)

        self.btn.clicked.connect(self.quest)
        self.btn_return.clicked.connect(self.backToHome)

        self.v_box.addWidget(self.btn_return)
        self.v_box.addWidget(self.label)

        self.setLayout(self.v_box)

    def backToHome(self):
        mainWidow = MainWindow()
        widget.addWidget(mainWidow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def quest(self):
        name = self.book_name.text()

        ques = "Select * from books where name = ?"

        self.cursor.execute(ques, (name,))

        books = self.cursor.fetchall()

        print(books)

        if len(books) == 0:
            print("Böyle bir kitap bulunmuyor")
        else:
            oppression = books[0][4]
            oppression += 1

            second_ques = "Update books Set oppression = ? where name = ?"

            self.cursor.execute(second_ques, (oppression, name))

            self.con.commit()
            self.label.setText("Baskı Yükseltildi")
            self.book_name.clear()


app = QApplication(sys.argv)

widget = QStackedWidget()

mainWidow = LoginWindow()

widget.addWidget(mainWidow)
widget.setWindowTitle("Libary App")

widget.show()
widget.setFixedHeight(300)
widget.setFixedWidth(400)

sys.exit(app.exec())
