import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtWidgets import QMainWindow, QApplication


class Main_menu(QMainWindow):
    def __init__(self):
        super(Main_menu, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(382, 300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.b_database = QtWidgets.QPushButton(self.centralwidget)
        self.b_database.setGeometry(QtCore.QRect(30, 40, 301, 31))
        self.b_database.setObjectName("b_database")
        self.b_streams = QtWidgets.QPushButton(self.centralwidget)
        self.b_streams.setGeometry(QtCore.QRect(30, 80, 301, 31))
        self.b_streams.setObjectName("b_streams")
        self.b_games_name = QtWidgets.QPushButton(self.centralwidget)
        self.b_games_name.setGeometry(QtCore.QRect(30, 120, 301, 31))
        self.b_games_name.setObjectName("b_games_name")
        self.b_recmendation = QtWidgets.QPushButton(self.centralwidget)
        self.b_recmendation.setGeometry(QtCore.QRect(30, 190, 301, 31))
        self.b_recmendation.setObjectName("b_recmendation")
        self.b_exit = QtWidgets.QPushButton(self.centralwidget)
        self.b_exit.setGeometry(QtCore.QRect(30, 230, 301, 31))
        self.b_exit.setObjectName("b_exit")
        self.l_name_prog = QtWidgets.QLabel(self.centralwidget)
        self.l_name_prog.setGeometry(QtCore.QRect(10, 0, 361, 31))
        self.l_name_prog.setObjectName("l_name_prog")
        self.l_test = QtWidgets.QLabel(self.centralwidget)
        self.l_test.setGeometry(QtCore.QRect(150, 160, 101, 16))
        self.l_test.setObjectName("l_test")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 382, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # привязка функций к кнопкам
        self.functions()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Парсер трансляций"))
        self.b_database.setText(_translate("MainWindow", "Работа с базой данных"))
        self.b_streams.setText(_translate("MainWindow", "Получение информации о трасляциях"))
        self.b_games_name.setText(_translate("MainWindow", "Получение списка названий всех игр"))
        self.b_recmendation.setText(_translate("MainWindow", "Рекомендации"))
        self.b_exit.setText(_translate("MainWindow", "Выход"))
        self.l_name_prog.setText(
            _translate("MainWindow", "Вас приветствует программа по сбору данных о прямых трансляциях"))
        self.l_test.setText(_translate("MainWindow", "0"))

    def functions(self):
        self.b_database.clicked.connect(self.b_database_clicked)
        self.b_streams.clicked.connect(self.b_streams_clicked)
        self.b_games_name.clicked.connect(self.b_games_clicked)
        self.b_recmendation.clicked.connect(self.b_recmendation_clicked)
        self.b_exit.clicked.connect(self.b_exit_clicked)

    def b_database_clicked(self):
        print('1')

    def b_streams_clicked(self):
        print('2')

    def b_games_clicked(self):
        print('3')

    def b_recmendation_clicked(self):
        print('4')

    def b_exit_clicked(self):
        print('5')


def main():
    app = QApplication(sys.argv)
    main_menu = Main_menu()

    main_menu.show()
    sys.exit(app.exec_())

main()