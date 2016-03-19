# -*- coding: utf-8 -*-
#Импорт фреймворка PyQt4 и его модулей
from PyQt4 import QtGui, QtCore, uic
import time
import os
# Импорт графического интерфейся главного окна и подписей таблиц
import dict_tables
# Графич.интерфейс главного окна
import main_ui
from PyQt4 import QtGui

# Драйвер синхронизации с PostgreSQL
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# Аутентификация в БД
class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        #Настройка окна
        self.setWindowTitle('Вход в БД:')
        self.setWindowIcon(QtGui.QIcon('img/client-login.jpg'))
        #Элементы GUI окна входа
        self.labelName = QtGui.QLabel(self)
        self.labelName.setText("Логин:")
        self.textName = QtGui.QLineEdit(self)
        self.labelPass = QtGui.QLabel(self)
        self.labelPass.setText("Пароль:")
        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Вход', self)
        #Событие на нажатие кнопки
        self.buttonLogin.clicked.connect(self.handleLogin)
        lgn_layout = QtGui.QVBoxLayout(self)
        #Режим строки ввода - Normal or Password. В режиме пароль - данные показуются как звездочки ****
        self.textPass.setEchoMode(QtGui.QLineEdit.Password)
        #Добавление к отображению
        lgn_layout.addWidget(self.labelName)  # label LOGIN
        lgn_layout.addWidget(self.textName)
        lgn_layout.addWidget(self.labelPass)  # label PASSWORD
        lgn_layout.addWidget(self.textPass)
        lgn_layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        try:
            global db, usr, hst, pword
            db = "aircraft"
            usr = self.textName.text()
            hst = 'localhost'
            pword = self.textPass.text()
            #Подключение к СУБД
            con = psycopg2.connect("dbname={0} user={1} host={2} password={3}".format(db, usr, hst, pword))
            #1
            cur = con.cursor()
            global t_user
            #Check admin, проверка на права БД
            check_query = """SELECT "usesuper" FROM pg_shadow WHERE "usename" = '{}';""".format(usr)
            #2
            cur.execute(check_query)
            self.v_type_user = list(cur.fetchone())
            self.admin_check = bool(self.v_type_user[0])
            t_user = self.admin_check # True its Admin, False its user
            # Выполнение методов
            self.accept()
            self.desProg()

            if con:
                con.close()
        except psycopg2.DatabaseError:
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль!')

    def desProg(self):
        splash = QtGui.QSplashScreen(QtGui.QPixmap("img/logo2.jpg"))
        splash.show()
        for i in range(1, 3):
            time.sleep(1)
            splash.showMessage("Загрузка программы ...{0}%".format(i*50), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
            QtGui.QApplication.processEvents()
            splash.show()
        splash.finish(splash)

# Окно автора
class AuthorWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(AuthorWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #Свойства окна
        self.setGeometry(500, 150, 390, 500) # size
        self.setWindowTitle('Инфо автора')
        #pixmap
        pixmap = QtGui.QPixmap(os.path.join('img', 'alexander_author.jpg'))
        pixmap2 = QtGui.QPixmap(os.path.join('img', 'PyQt.png'))
        pixmap3 = QtGui.QPixmap(os.path.join('img', 'postgresql-logo.png'))
        pixmap4 = QtGui.QPixmap(os.path.join('img', 'Opensource.png'))
        #label изображений
        self.pic = QtGui.QLabel(self)
        self.pic.setPixmap(pixmap)
        self.pic.setGeometry(20, 20, 200, 200)

        self.pic2 = QtGui.QLabel(self)
        self.pic2.setPixmap(pixmap2)
        self.pic2.setGeometry(270, 70, 75, 75)

        self.pic3 = QtGui.QLabel(self)
        self.pic3.setPixmap(pixmap3)
        self.pic3.setGeometry(270, 170, 64, 64)

        self.pic4 = QtGui.QLabel(self)
        self.pic4.setPixmap(pixmap4)
        self.pic4.setGeometry(80, 250, 220, 198)
        #label надписей
        self.label2 = QtGui.QLabel(self)
        self.label2.setGeometry(40, 240, 400, 20)
        self.label2.setText("Работа выполнена студентом ЗГИА гр. СП-14о")

        self.label3 = QtGui.QLabel(self)
        self.label3.setGeometry(40, 450, 300, 20)
        self.label3.setText("Мукась Александром Петровичем. 2016 г.")

        self.label4 = QtGui.QLabel(self)
        self.label4.setGeometry(260, 20, 200, 20)
        self.label4.setText("PyQt v. 4.14")

        self.label5 = QtGui.QLabel(self)
        self.label5.setGeometry(260, 42, 200, 20)
        self.label5.setText("Python v. 3.4")

        self.label6 = QtGui.QLabel(self)
        self.label6.setGeometry(240, 150, 200, 20)
        self.label6.setText("СУБД PostgreSQL 9.4")

        self.a_vbox = QtGui.QVBoxLayout(self)

        self.widget_list = [self.pic, self.pic2, self.pic3, self.pic4, self.label2,
                       self.label3, self.label4, self.label5, self.label6]
        for item in self.widget_list:
            self.a_vbox.addWidget(item)

#Добавление нового пользователя
class Add_new_user(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Add_new_user, self).__init__(parent)
        # Местоположение основного окна (позиция , размер)
        self.setGeometry(340, 300, 450, 100)
        self.setWindowTitle('Добавление нового пользователя')
        self.setWindowIcon(QtGui.QIcon('img/add_user.png'))

        # vertical layout for widgets
        self.anu_vbox = QtGui.QVBoxLayout(self)
        self.setLayout(self.anu_vbox)

        # A label to display our selection
        self.u_lbl = QtGui.QLabel(self)
        self.u_lbl.setText('Добавить: ')
        self.u_lbl.setGeometry(40, 40, 100, 20)

        self.le_user = QtGui.QLineEdit(self)
        self.le_user.setGeometry(150, 40, 100, 20)
        # (горизонталь, вертикаль-меньше->выше)
        self.anu_vbox.addWidget(self.le_user)

        self.le_pass = QtGui.QLineEdit(self)
        self.le_pass.setGeometry(260, 40, 100, 20)
        # (горизонталь, вертикаль-меньше->выше)
        self.anu_vbox.addWidget(self.le_pass)

        # Кнопка Старт
        self.btn_accept = QtGui.QPushButton('Создать!', self)
        # setGeometry( позиция ширина, позиция высота, размер ширина, размер высота)
        self.btn_accept.setGeometry(140, 70, 100, 25)
        #self.btn_accept.clicked.connect(self.handle_Start_table_button)
        self.anu_vbox.addWidget(self.btn_accept)

        self.btn_accept.clicked.connect(self.handle_add_user_accept)

    def handle_add_user_accept(self):
        self.v_pass = self.le_pass.text()
        self.v_user = self.le_user.text()

        self.anu_query1 = """ CREATE USER "{0}" WITH PASSWORD '{1}' ;""" .format(self.v_user, self.v_pass)
        self.anu_query2 = """ GRANT SELECT ON "view_#1", "view_#2", "view_#3_1", "view_#3_2",
		    "view_#4_1", "view_#4_2", "view_#5", "view_#6", "view_#7", "view_#8", "view_#9",
		    "view_#10", "view_#11", "view_#12", "view_#13", "view_#14", "pg_shadow"
            TO "{0}" ; """.format(self.v_user)
        try:
            print(self.anu_query1)
            print(self.anu_query2)
            con = None
            con = psycopg2.connect("dbname={0} user={1} host={2} password={3}".format(db, usr, hst, pword))
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()

            cur.execute(self.anu_query1)
            cur.execute(self.anu_query2)

            if con:
                con.close()
            apt_msg = "Пользователь " + self.v_user + " " + "создан!"
            QtGui.QMessageBox.information(self, 'Успешно!', apt_msg)
        except psycopg2.DatabaseError:
            QtGui.QMessageBox.warning(self, 'Ошибка!', 'Не могу создать юзера в БД')

# Основное окно программы
class Window(QtGui.QMainWindow, main_ui.Ui_Form):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # vertical layout for widgets
        self.vbox = QtGui.QVBoxLayout(self)
        #self.setLayout(self.vbox)

        # A label to display our selection
        self.lbl = QtGui.QLabel(self)
        self.lbl.setText('Таблицы:')
        self.lbl.move(60, 80)
        # Center align text
        self.lbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.vbox.addWidget(self.lbl)

        # A label to display our selection
        self.lbl2 = QtGui.QTextEdit(self)

        self.lbl2.resize(600, 60)

        self.lbl2.setText('-None-:')
        self.lbl2.move(250, 80)
        # Center align text
        self.lbl2.setAlignment(QtCore.Qt.AlignHCenter)
        self.vbox.addWidget(self.lbl2)

        # Кнопка Старт
        self.btn_start = QtGui.QPushButton('Старт!', self)
        # setGeometry( позиция ширина, позиция высота, размер ширина, размер высота)
        self.btn_start.setGeometry(60, 160, 920, 25)
        self.btn_start.clicked.connect(self.handle_Start_table_button)
        self.vbox.addWidget(self.btn_start)

        #Остальные элементы GUI
        self.lbl3 = QtGui.QLabel(self)
        self.lbl3.setText('Фильтр по знач.:')
        self.lbl3.setGeometry(1050, 60, 150, 50)
        self.vbox.addWidget(self.lbl3)

        self.f_combo1 = QtGui.QComboBox(self)
        self.f_combo1.setGeometry(1050, 115, 120, 30)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_combo1)

        self.f_line_edit1_1 = QtGui.QLineEdit(self)
        self.f_line_edit1_1.setGeometry(1010, 150, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit1_1)

        self.f_line_edit1_2 = QtGui.QLineEdit(self)
        self.f_line_edit1_2.setGeometry(1115, 150, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit1_2)

        self.f_combo2 = QtGui.QComboBox(self)
        self.f_combo2.setGeometry(1050, 200, 120, 30)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_combo2)

        self.f_line_edit2_1 = QtGui.QLineEdit(self)
        self.f_line_edit2_1.setGeometry(1010, 235, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit2_1)

        self.f_line_edit2_2 = QtGui.QLineEdit(self)
        self.f_line_edit2_2.setGeometry(1115, 235, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit2_2)

        self.f_combo3 = QtGui.QComboBox(self)
        self.f_combo3.setGeometry(1050, 300, 120, 30)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_combo3)

        self.f_line_edit3_1 = QtGui.QLineEdit(self)
        self.f_line_edit3_1.setGeometry(1010, 335, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit3_1)

        self.f_line_edit3_2 = QtGui.QLineEdit(self)
        self.f_line_edit3_2.setGeometry(1115, 335, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit3_2)

        self.f_combo4 = QtGui.QComboBox(self)
        self.f_combo4.setGeometry(1050, 400, 120, 30)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_combo4)

        self.f_line_edit4_1 = QtGui.QLineEdit(self)
        self.f_line_edit4_1.setGeometry(1010, 435, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit4_1)

        self.f_line_edit4_2 = QtGui.QLineEdit(self)
        self.f_line_edit4_2.setGeometry(1115, 435, 100, 27)
        # (горизонталь, вертикаль-меньше->выше)
        self.vbox.addWidget(self.f_line_edit4_2)

        # Свойства основного окна (позиция , размер)
        self.setGeometry(100, 100, 1240, 520)
        self.setWindowTitle('Информационная система"Авиазавод"')
        self.setWindowIcon(QtGui.QIcon('img/plane.png'))

        # Кнопка info author
        self.btn_flr = QtGui.QPushButton('~Автор~', self)
           # setGeometry( позиция ширина, позиция высота, размер ширина, размер высота)
        self.btn_flr.setGeometry(870, 80, 100, 60)
        self.btn_flr.clicked.connect(self.handle_Author_button)
        self.vbox.addWidget(self.btn_flr)

        # table
        self.tableWidget = QtGui.QTableWidget(self)
        #self.tableWidget.setColumnCount(1)
        #self.tableWidget.setRowCount(1)
        self.tableWidget.setGeometry(QtCore.QRect(60, 200, 940, 260))
        self.vbox.addWidget(self.tableWidget)

        self.exit = QtGui.QAction(QtGui.QIcon('img/exit.png'), 'Выйти', self)
        self.exit.setShortcut('Ctrl+E')
        self.exit.setStatusTip('Выход из программы')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.info = QtGui.QAction(QtGui.QIcon('img/Opensource.png'), 'Инфо', self)
        self.info.setShortcut('Ctrl+I')
        self.info.setStatusTip('Инфо об авторе')
        self.info.triggered.connect(self.handle_Author_button)

        self.statusBar()

        menubar = self.menuBar()
        menu = menubar.addMenu('&Меню')
        menu.addAction(self.info)
        menu.addAction(self.exit)

        toolbar = self.addToolBar('Панель инструментов')

        toolbar.addAction(self.exit)
        toolbar.addAction(self.info)

        if (t_user is True): # t_user
            self.add_user = QtGui.QAction(QtGui.QIcon('img/add_user.png'), '+ Пользователя', self)
            self.add_user.setShortcut('Ctrl+U')
            self.add_user.setStatusTip('Добавить пользователя')

            menu.addAction(self.add_user)
            toolbar.addAction(self.add_user)
            self.add_user.triggered.connect(self.handle_Add_user)

        self.table()

    def handle_Author_button(self):
        self.hab_window = AuthorWindow(self)
        self.hab_window.show()

    def handle_Add_user(self):
        self.au_window = Add_new_user(self)
        self.au_window.show()

    def table(self):

        self.combo = QtGui.QComboBox(self)
        self.combo.resize(160, 40)
        # (горизонталь, вертикаль-меньше->выше)
        self.combo.move(60, 100)
        self.vbox.addWidget(self.combo)

        try:
            con = psycopg2.connect("dbname={0} user={1} host={2} password={3}".format(db, usr, hst, pword))
            cur = con.cursor()

            sys_query = """
            SELECT distinct "table_name" FROM information_schema.columns
            WHERE table_schema='public' ORDER BY table_name """

            cur.execute(sys_query)

            v_table_list =[]
            v_tuple = list(cur.fetchall())
            v_table_list = [element for tupl in v_tuple for element in tupl]
            #
            self.combo.addItems(v_table_list)

            self.i = 0
            self.connect(self.combo, QtCore.SIGNAL('activated(QString)'), self.combo_chosen)
            if con:
                con.close()
        except psycopg2.DatabaseError:
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Не могу подключиться к БД')
    def combo_chosen(self, text):

        global v_table_label
        v_table_label = text

        v_dict = dict_tables.t_dictionary
        v_text = v_dict[text]

        self.lbl2.setText(v_text)
        self.lbl2.setDisabled(True)
        self.lbl2.setAlignment(QtCore.Qt.AlignHCenter)

        try:
            self.v_tab_name = text
            con = psycopg2.connect("dbname={0} user={1} host={2} password={3}".format(db, usr, hst, pword))
            cur = con.cursor()
            # 1
            cur.execute("""
            SELECT "column_name" FROM information_schema.columns
              WHERE table_schema='public'
              AND table_name = '{0}'
              ORDER BY ordinal_position; """.format(self.v_tab_name))


            self.v_header_list = []
            v_head_tupl = list(cur.fetchall())
            # Список имен стоблцев
            self.v_header_list = [element for tupl in v_head_tupl for element in tupl]

            self.v_count_col = len(self.v_header_list)

            self.tableWidget.clear()

            # 2
            rowcount_query = """
            SELECT count(*) FROM "{0}"
                        """.format(self.v_tab_name)

            cur.execute(rowcount_query)

            self.v_count_lines = list(cur.fetchone())
            self.v_count_lines = int(self.v_count_lines[0])

            # FILTER__________________________________________
            self.f_combo1.clear()
            self.f_combo2.clear()
            self.f_combo3.clear()
            self.f_combo4.clear()
            #Передадим другой переменной список имен столбцев
            self.hd_ls = self.v_header_list
            #Проверки на кол-во столбцов в табл
            self.v_header_len = len(self.hd_ls)
            if (self.v_header_len < 4):
                if (self.v_header_len == 2):
                    self.f_combo1.addItem(self.hd_ls[0])
                    self.f_combo2.addItem(self.hd_ls[1])
                    self.f_combo3.clear()
                    self.f_combo4.clear()
                elif (self.v_header_len == 3):
                    self.f_combo1.addItem(self.hd_ls[0])
                    self.f_combo2.addItem(self.hd_ls[1])
                    self.f_combo3.addItem(self.hd_ls[2])
                    self.f_combo4.clear()
            else:
            #self.f_combo1.addItems(v_header_list[0])
                self.f_combo1.addItem(self.hd_ls[0])
                self.f_combo2.addItem(self.hd_ls[1])
                self.f_combo3.addItem(self.hd_ls[2])
                self.f_combo4.addItem(self.hd_ls[3])

            # Первый подфильтр
            position = 0
            if (self.f_line_edit1_1.text() and self.f_line_edit1_2.text()):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft1 += """  "{0}" BETWEEN {1} AND {2}""".format(self.f_combo1.currentText(), self.f_line_edit1_1.text(),
                                                                 self.f_line_edit1_2.text())
            elif (self.f_line_edit1_1.text()): # and self.lineEdit1_2.text() is None):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft1 += """  "{0}" = '{1}' """.format(self.f_combo1.currentText(), self.f_line_edit1_1.text())
            else:
                self.ft1 = ""

            # Второй подфильтр
            if (self.f_line_edit2_1.text() and self.f_line_edit2_2.text()):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft2 += """  "{0}" BETWEEN {1} AND {2}""".format(self.f_combo2.currentText(), self.f_line_edit2_1.text(),
                                                                 self.f_line_edit2_2.text())
            elif (self.f_line_edit2_1.text()):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft2 += """ "{0}" = '{1}' """.format(self.f_combo2.currentText(), self.f_line_edit2_1.text())
            else:
                self.ft2 = ""

            # Третий подфильтр
            if (self.f_line_edit3_1.text() and self.f_line_edit3_2.text()):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft3 += """ "{0}" BETWEEN {1} AND {2}""".format(self.f_combo3.currentText(), self.f_line_edit3_1.text(),
                                                                 self.f_line_edit3_2.text())
            elif (self.f_line_edit3_1.text()):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft3 += """ "{0}" = '{1}' """.format(self.f_combo3.currentText(), self.f_line_edit3_1.text())
            else:
                self.ft3 = ""

            # Четвертый подфильтр
            if (self.f_line_edit4_1.text() and self.f_line_edit4_2.text()):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft4 += """ "{0}" BETWEEN {1} AND {2}""".format(self.f_combo4.currentText(), self.f_line_edit4_1.text(),
                                                                 self.f_line_edit4_2.text())
            elif (self.f_line_edit4_1.text()):
                position += 1
                if (position >1):
                    self.ft1 = " AND "
                self.ft4 += """ "{0}" = '{1}' """.format(self.f_combo4.currentText(), self.f_line_edit4_1.text())
            else:
                self.ft4 = ""

            # Конечный фильтр
            if (self.ft1 == "" and self.ft2 == "" and self.ft3 == "" and self.ft4 == ""):
                self.v_filter = ""
            if (self.ft1 != "" or self.ft2 != "" or self.ft3 != "" or self.ft4 != ""):
                self.v_filter = "WHERE "
                if (self.ft1 != ""):
                    self.v_filter += self.ft1
                elif (self.ft2 != ""):
                    self.v_filter += self.ft2
                elif (self.ft3 != ""):
                    self.v_filter += self.ft3
                elif (self.ft4 != ""):
                    self.v_filter += self.ft4

            # 3
            # Данные таблицы без фильтра
            data_tab_query = ""
            data_tab_query = """SELECT * FROM "{0}" """.format(self.v_tab_name)

            # Фильтр добавляет ограничение в запрос

            data_tab_query = data_tab_query + str(self.v_filter)

            cur.execute(data_tab_query)

            self.v_lists_col = list(cur.fetchall())

            # Активация сортировки
            self.tableWidget.setSortingEnabled(True)

            del self.v_filter
            if con:
                cur.close()
                con.close()
        except psycopg2.DatabaseError:
            QtGui.QMessageBox.warning(self, 'Ошибка', 'Не могу подключиться к БД')

        # Кнопка Старт
    def handle_Start_table_button(self):

        self.combo_chosen(self.v_tab_name)

        self.tableWidget.clear()
        # Формированее таблицы
        self.tableWidget.setColumnCount(self.v_count_col)
        self.tableWidget.setHorizontalHeaderLabels(self.v_header_list)
        #Установить кол-во строк
        self.tableWidget.setRowCount(self.v_count_lines)
        # Заполнить содержимым
        num_line = 0
        for line in self.v_lists_col:
            num_col = 0
            for cell in line:
                self.tableWidget.setItem(num_line, num_col, QtGui.QTableWidgetItem(str(cell)))
                num_col += 1
            num_line += 1

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)

    if Login().exec_() == QtGui.QDialog.Accepted:

        window = Window()
        window.show()
        sys.exit(app.exec_())