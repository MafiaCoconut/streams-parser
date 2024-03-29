import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from menu.parser_page import ParserWindow
# from menu import parser_page
import youtube as youtube
import help_files.information as information
import json


class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.setObjectName("Application")
        self.resize(869, 653)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, -22, 871, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setCurrentIndex(0)

        # Главное меню
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(230, 90, 421, 281))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_name_prog = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.l_name_prog.setObjectName("l_name_prog")
        self.verticalLayout.addWidget(self.l_name_prog)
        self.b_database = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.b_database.setObjectName("b_database")
        self.verticalLayout.addWidget(self.b_database)
        self.b_streams = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.b_streams.setObjectName("b_streams")
        self.verticalLayout.addWidget(self.b_streams)
        self.b_games_name = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.b_games_name.setObjectName("b_games_name")
        self.verticalLayout.addWidget(self.b_games_name)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.b_recmendation = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.b_recmendation.setObjectName("b_recmendation")
        self.verticalLayout.addWidget(self.b_recmendation)
        self.b_exit = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.b_exit.setObjectName("b_exit")
        self.verticalLayout.addWidget(self.b_exit)
        self.tabWidget.addTab(self.main_page, "")
        self.main_page.show()

        # Страница с базой данных
        self.database_page = QtWidgets.QWidget()
        self.database_page.setObjectName("database_page")
        self.label_6 = QtWidgets.QLabel(self.database_page)
        self.label_6.setGeometry(QtCore.QRect(230, 160, 251, 41))
        self.label_6.setObjectName("label_6")
        self.l_time = QtWidgets.QLabel(self.database_page)
        self.l_time.setGeometry(QtCore.QRect(460, 160, 121, 41))
        self.l_time.setObjectName("l_time")
        self.b_exit_4 = QtWidgets.QPushButton(self.database_page)
        self.b_exit_4.setGeometry(QtCore.QRect(760, 20, 91, 61))
        self.b_exit_4.setObjectName("b_exit_4")
        self.b_update_database = QtWidgets.QPushButton(self.database_page)
        self.b_update_database.setGeometry(QtCore.QRect(230, 210, 361, 61))
        self.b_update_database.setObjectName("b_uodate_database")
        self.l_per_of_comletion = QtWidgets.QLabel(self.database_page)
        self.l_per_of_comletion.setGeometry(QtCore.QRect(300, 280, 250, 31))
        self.l_per_of_comletion.setObjectName("l_per_of_comletion")
        self.tabWidget.addTab(self.database_page, '1')

        # Страница с парсером
        self.parser_page = QtWidgets.QWidget()
        self.parser_page.setObjectName("parser_page")
        self.b_games_names = QtWidgets.QPushButton(self.parser_page)
        self.b_games_names.setGeometry(QtCore.QRect(0, 510, 181, 71))
        self.b_games_names.setObjectName("b_games_names")
        self.text_name_of_game = QtWidgets.QTextEdit(self.parser_page)
        self.text_name_of_game.setGeometry(QtCore.QRect(20, 20, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_name_of_game.setFont(font)
        self.text_name_of_game.setObjectName("text_name_of_game")
        self.b_exit_3 = QtWidgets.QPushButton(self.parser_page)
        self.b_exit_3.setGeometry(QtCore.QRect(770, 0, 91, 61))
        self.b_exit_3.setObjectName("b_exit_3")
        self.b_search = QtWidgets.QPushButton(self.parser_page)
        self.b_search.setGeometry(QtCore.QRect(420, 20, 91, 41))
        self.b_search.setObjectName("b_search")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.parser_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 801, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.video1 = QtWidgets.QHBoxLayout()
        self.video1.setObjectName("video1")
        self.l_author_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_author_1.setObjectName("l_author_1")
        self.video1.addWidget(self.l_author_1)
        self.l_video_title_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_video_title_1.setObjectName("l_video_title_1")
        self.video1.addWidget(self.l_video_title_1)
        self.l_link_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.l_link_1.setObjectName("l_link_1")
        self.video1.addWidget(self.l_link_1)
        self.l_link_1.setReadOnly(True)
        self.verticalLayout_4.addLayout(self.video1)
        self.video2 = QtWidgets.QHBoxLayout()
        self.video2.setObjectName("video2")
        self.l_author_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_author_2.setObjectName("l_author_2")
        self.video2.addWidget(self.l_author_2)
        self.l_video_title_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_video_title_2.setObjectName("l_video_title_2")
        self.video2.addWidget(self.l_video_title_2)
        self.l_link_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.l_link_2.setObjectName("l_link_2")
        self.video2.addWidget(self.l_link_2)
        self.l_link_2.setReadOnly(True)
        self.verticalLayout_4.addLayout(self.video2)
        self.video3 = QtWidgets.QHBoxLayout()
        self.video3.setObjectName("video3")
        self.l_author_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_author_3.setObjectName("l_author_3")
        self.video3.addWidget(self.l_author_3)
        self.l_video_title_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_video_title_3.setObjectName("l_video_title_3")
        self.video3.addWidget(self.l_video_title_3)
        self.l_link_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.l_link_3.setObjectName("l_link_3")
        self.video3.addWidget(self.l_link_3)
        self.l_link_3.setReadOnly(True)
        self.verticalLayout_4.addLayout(self.video3)
        self.video4 = QtWidgets.QHBoxLayout()
        self.video4.setObjectName("video4")
        self.l_author_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_author_4.setObjectName("l_author_4")
        self.video4.addWidget(self.l_author_4)
        self.l_video_title_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_video_title_4.setObjectName("l_video_title_4")
        self.video4.addWidget(self.l_video_title_4)
        self.l_link_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.l_link_4.setObjectName("l_link_4")
        self.video4.addWidget(self.l_link_4)
        self.l_link_4.setReadOnly(True)
        self.verticalLayout_4.addLayout(self.video4)
        self.video5 = QtWidgets.QHBoxLayout()
        self.video5.setObjectName("video5")
        self.l_author_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_author_5.setObjectName("l_author_5")
        self.video5.addWidget(self.l_author_5)
        self.l_video_title_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_video_title_5.setObjectName("l_video_title_5")
        self.video5.addWidget(self.l_video_title_5)
        self.l_link_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.l_link_5.setObjectName("l_link_5")
        self.video5.addWidget(self.l_link_5)
        self.l_link_5.setReadOnly(True)
        self.verticalLayout_4.addLayout(self.video5)
        self.tabWidget.addTab(self.parser_page, "")

        # Страница с названиями игр
        self.games_name_page = QtWidgets.QWidget()
        self.games_name_page.setObjectName("games_name_page")
        self.textBrowser = QtWidgets.QTextBrowser(self.games_name_page)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 821, 461))
        self.textBrowser.setObjectName("textBrowser")
        self.b_exit_8 = QtWidgets.QPushButton(self.games_name_page)
        self.b_exit_8.setGeometry(QtCore.QRect(750, 10, 91, 61))
        self.b_exit_8.setObjectName("b_exit_8")
        self.b_to_parser = QtWidgets.QPushButton(self.games_name_page)
        self.b_to_parser.setGeometry(QtCore.QRect(24, 12, 211, 61))
        self.b_to_parser.setObjectName("b_to_parser")
        self.tabWidget.addTab(self.games_name_page, "")

        # Страница с рекомендациями к использованию
        self.recomendation_page = QtWidgets.QWidget()
        self.recomendation_page.setObjectName("recomendation_page")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.recomendation_page)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(60, 150, 751, 221))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.b_exit_9 = QtWidgets.QPushButton(self.recomendation_page)
        self.b_exit_9.setGeometry(QtCore.QRect(720, 10, 91, 61))
        self.b_exit_9.setObjectName("b_exit_9")
        self.tabWidget.addTab(self.recomendation_page, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 869, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.connect_buttoms()
        self.checkout_to_menu()
        # self.parser_page.show()
        # self.tabWidget.setCurrentIndex(1)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
        Application.setWindowTitle(_translate("Application", "LPAR"))
        self.l_name_prog.setText(
            _translate("Application", '      Вас приветствует программа по сбору данных о прямых трансляциях " LPAR "'))
        self.b_database.setText(_translate("Application", "Работа с базой данных"))
        self.b_streams.setText(_translate("Application", "Получение информации о трасляциях"))
        self.b_games_name.setText(_translate("Application", "Получение списка названий всех игр"))
        self.b_recmendation.setText(_translate("Application", "Рекомендации"))
        self.b_exit.setText(_translate("Application", "Выход"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_page), _translate("Application", "Menu"))
        self.label_6.setText(_translate("Application", "Последнее обновление базы данных было:"))
        self.l_time.setText(_translate("Application", self.update_last_time_update_database()))
        self.b_exit_4.setText(_translate("Application", "Назад"))
        self.b_update_database.setText(_translate("Application", "Обновить базу данных\nВнимание!!! Это займёт "
                                                                 "некоторое время, не отключайте программу"))
        self.l_per_of_comletion.setText(_translate("Application", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.database_page), _translate("Application", "Database"))
        self.b_games_names.setText(_translate("Application", "Просмотр всех названий игр"))
        self.text_name_of_game.setHtml(_translate("Application",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                  "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                                  "type=\"text/css\">\n "
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                                  "font-size:14pt; font-weight:400; font-style:normal;\">\n "
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; "
                                                  "margin-bottom:0px; margin-left:0px; margin-right:0px; "
                                                  "-qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text_name_of_game.setText("")
        self.b_exit_3.setText(_translate("Application", "Назад"))
        self.b_search.setText(_translate("Application", "Поиск"))
        self.l_author_1.setText(_translate("Application", "Автор"))
        self.l_video_title_1.setText(_translate("Application", "Название видео"))
        self.l_link_1.setText(_translate("Application", "Ссылка"))
        self.l_author_2.setText(_translate("Application", "Автор"))
        self.l_video_title_2.setText(_translate("Application", "Название видео"))
        self.l_link_2.setText(_translate("Application", "Ссылка"))
        self.l_author_3.setText(_translate("Application", "Автор"))
        self.l_video_title_3.setText(_translate("Application", "Название видео"))
        self.l_link_3.setText(_translate("Application", "Ссылка"))
        self.l_author_4.setText(_translate("Application", "Автор"))
        self.l_video_title_4.setText(_translate("Application", "Название видео"))
        self.l_link_4.setText(_translate("Application", "Ссылка"))
        self.l_author_5.setText(_translate("Application", "Автор"))
        self.l_video_title_5.setText(_translate("Application", "Название видео"))
        self.l_link_5.setText(_translate("Application", "Ссылка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.parser_page), _translate("Application", "Parser"))
        self.textBrowser.setHtml(_translate("Application",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                            "type=\"text/css\">\n "
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; "
                                            "font-size:8.25pt; font-weight:400; font-style:normal;\">\n "
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><br /></p></body></html>"))
        self.b_exit_8.setText(_translate("Application", "Назад"))
        self.b_to_parser.setText(_translate("Application", "Вернуться к парсеру"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.games_name_page),
                                  _translate("Application", "GamesName"))
        self.label_2.setText(_translate("Application",
                                        "Перед началом работы, рекомендуется обновить базу данных в пункте №1 на "
                                        "стартовом экране."))
        self.label_3.setText(_translate("Application",
                                        "Далее рекомендуется, в ситуации когда вы не помните полное название игры, "
                                        "запросить список названий игр."))
        self.label_4.setText(_translate("Application",
                                        "Если программы пишет что игры нет в списке, то возможно стримы по игре "
                                        "сейчас находятся не в топ 50 самых популярных играх."))
        self.label_5.setText(_translate("Application", "   Приятного использования программы!!!"))
        self.b_exit_9.setText(_translate("Application", "Назад"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recomendation_page),
                                  _translate("Application", "Recomendation"))
        self.textBrowser.setText(_translate("Application", self.games_name_get_in_str()))

    def exit(self):
        sys.exit()

    def connect_buttoms(self):
        # Кнопки отвечающие за переход между окнами
        self.b_exit.clicked.connect(self.exit)
        self.b_exit_3.clicked.connect(self.checkout_to_menu)
        self.b_exit_4.clicked.connect(self.checkout_to_menu)
        self.b_exit_8.clicked.connect(self.checkout_to_menu)
        self.b_exit_9.clicked.connect(self.checkout_to_menu)
        self.b_database.clicked.connect(self.checkout_to_database)
        self.b_streams.clicked.connect(self.checkout_to_parser)
        self.b_games_name.clicked.connect(self.checkout_to_games_name)
        self.b_recmendation.clicked.connect(self.checkout_to_recomendations)
        self.b_to_parser.clicked.connect(self.checkout_to_parser)
        self.b_games_names.clicked.connect(self.checkout_to_games_name)

        # Страница с базой данных
        self.b_update_database.clicked.connect(self.update_database)

        # Страница с парсером
        self.b_search.clicked.connect(self.parser_search)

    # Функции для базы данных
    def update_database(self):
        youtube.update_data()
        self.l_per_of_comletion.setText('Готова, база данных была обновлена!')
        self.update_last_time_update_database()

    def update_last_time_update_database(self):
        with open('data/youtube.json', encoding='utf-8') as file:
            data = json.load(file)
        last_update = data['last_update_time'][:-4]
        self.l_time.setText(str(last_update))

    # Поиск спарсенных стримов
    def parser_search(self):
        with open('data/youtube.json', encoding='utf-8') as file:
            data = json.load(file)
        data_youtube = data
        name = self.text_name_of_game.toPlainText()
        if name in data_youtube:
            lst = [
                [self.l_author_1, self.l_video_title_1, self.l_link_1],
                [self.l_author_2, self.l_video_title_2, self.l_link_2],
                [self.l_author_3, self.l_video_title_3, self.l_link_3],
                [self.l_author_4, self.l_video_title_4, self.l_link_4],
                [self.l_author_5, self.l_video_title_5, self.l_link_5]
            ]
            for i in range(len(lst)):
                lst[i][0].setText(f'{data_youtube[name][i]["channel name"]}')
                lst[i][1].setText(f'{data_youtube[name][i]["video title"]}')
                lst[i][2].setText(f'{data_youtube[name][i]["url"]}')
        elif name not in data_youtube and youtube.check_name_is_in_games_name(name) and name != '':
            error = QMessageBox()
            error.setWindowTitle('Предупреждение!!!')
            error.setText('Такая игра действительно существует, но, к сожалению, на данный момент в топ 50 по миру по '
                          'ней нет ни одного стрима. Попробуйте другую игру.')
            error.setIcon(QMessageBox.Warning)
            error.exec_()

        else:
            error = QMessageBox()
            error.setWindowTitle('Предупреждение!!!')
            error.setText('Вы ввели неправильное название игры, попробуйте ещё раз или '
                          'нажмите "Просмотр всех названий игр".')
            error.setIcon(QMessageBox.Warning)
            error.exec_()

    # Функции для перехода между окнами
    def checkout_to_menu(self):
        self.tabWidget.setCurrentIndex(0)

    def checkout_to_database(self):
        self.tabWidget.setCurrentIndex(1)
        self.update_last_time_update_database()

    def checkout_to_parser(self):
        self.tabWidget.setCurrentIndex(2)

    def checkout_to_games_name(self):
        self.tabWidget.setCurrentIndex(3)

    def checkout_to_recomendations(self):
        self.tabWidget.setCurrentIndex(4)

    def games_name_get_in_str(self):
        data = youtube.games_name_get()
        data.sort()
        data = data[1:]
        data2 = ''
        data1 = ''
        x = 0
        l = 0
        for i in data:
            if r"\u" in i:
                continue
            x += 1
            if len(data1) + len(i) > 130:
                data2 += data1 + '\n'
                data1 = ''

            data1 += i + ' ' * 7

        if data1 not in data2:
            data2 += data1
        return data2
