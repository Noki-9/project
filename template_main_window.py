from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Основные настройки главного окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 745)  # Установка размеров окна

        # Создание центрального виджета и основного layout
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Основной контейнер для всех элементов интерфейса
        self.main_layout = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_layout.setObjectName("main_layout")
        self.gridLayout = QtWidgets.QGridLayout(self.main_layout)
        self.gridLayout.setObjectName("gridLayout")

        # === ПОЛЕ ДЛЯ НАЗВАНИЯ КОРОЛЕВСТВА ===
        self.kingdom_name = QtWidgets.QLineEdit(parent=self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kingdom_name.sizePolicy().hasHeightForWidth())
        self.kingdom_name.setSizePolicy(sizePolicy)
        self.kingdom_name.setObjectName("kingdom_name")
        self.gridLayout.addWidget(self.kingdom_name, 5, 1, 1, 1)

        # === СЕКЦИЯ РЕСУРСОВ ===
        self.res_layout = QtWidgets.QGridLayout()
        self.res_layout.setObjectName("res_layout")

        # Пшеница
        self.wheat = QtWidgets.QLineEdit(parent=self.main_layout)
        self.wheat.setObjectName("wheat")
        self.res_layout.addWidget(self.wheat, 0, 0, 1, 1)
        self.wheat_info = QtWidgets.QLabel(parent=self.main_layout)
        self.wheat_info.setObjectName("wheat_info")
        self.res_layout.addWidget(self.wheat_info, 0, 1, 1, 1)

        # Дерево
        self.wood = QtWidgets.QLineEdit(parent=self.main_layout)
        self.wood.setObjectName("wood")
        self.res_layout.addWidget(self.wood, 0, 2, 1, 1)
        self.wood_info = QtWidgets.QLabel(parent=self.main_layout)
        self.wood_info.setObjectName("wood_info")
        self.res_layout.addWidget(self.wood_info, 0, 3, 1, 1)

        # Производство
        self.factor = QtWidgets.QLineEdit(parent=self.main_layout)
        self.factor.setObjectName("factor")
        self.res_layout.addWidget(self.factor, 1, 0, 1, 1)
        self.factor_info = QtWidgets.QLabel(parent=self.main_layout)
        self.factor_info.setObjectName("factor_info")
        self.res_layout.addWidget(self.factor_info, 1, 1, 1, 1)

        # Камень
        self.stone = QtWidgets.QLineEdit(parent=self.main_layout)
        self.stone.setObjectName("stone")
        self.res_layout.addWidget(self.stone, 1, 2, 1, 1)
        self.stone_info = QtWidgets.QLabel(parent=self.main_layout)
        self.stone_info.setObjectName("stone_info")
        self.res_layout.addWidget(self.stone_info, 1, 3, 1, 1)

        # Золото
        self.gold = QtWidgets.QLineEdit(parent=self.main_layout)
        self.gold.setObjectName("gold")
        self.res_layout.addWidget(self.gold, 2, 0, 1, 1)
        self.gold_info = QtWidgets.QLabel(parent=self.main_layout)
        self.gold_info.setObjectName("gold_info")
        self.res_layout.addWidget(self.gold_info, 2, 1, 1, 1)

        # Железо
        self.iron = QtWidgets.QLineEdit(parent=self.main_layout)
        self.iron.setObjectName("iron")
        self.res_layout.addWidget(self.iron, 2, 2, 1, 1)
        self.iron_info = QtWidgets.QLabel(parent=self.main_layout)
        self.iron_info.setObjectName("iron_info")
        self.res_layout.addWidget(self.iron_info, 2, 3, 1, 1)

        self.gridLayout.addLayout(self.res_layout, 5, 0, 1, 1)

        # === СЕКЦИЯ НАСЕЛЕНИЯ ===
        self.people_layout = QtWidgets.QGridLayout()
        self.people_layout.setObjectName("people_layout")

        # Количество людей
        self.people = QtWidgets.QLineEdit(parent=self.main_layout)
        self.people.setObjectName("people")
        self.people_layout.addWidget(self.people, 0, 0, 1, 1)
        self.people_info = QtWidgets.QLabel(parent=self.main_layout)
        self.people_info.setObjectName("people_info")
        self.people_layout.addWidget(self.people_info, 0, 1, 1, 1)

        # Счастье населения
        self.happy = QtWidgets.QLineEdit(parent=self.main_layout)
        self.happy.setObjectName("happy")
        self.people_layout.addWidget(self.happy, 0, 2, 1, 1)
        self.happy_info = QtWidgets.QLabel(parent=self.main_layout)
        self.happy_info.setObjectName("happy_info")
        self.people_layout.addWidget(self.happy_info, 0, 3, 1, 1)

        # Институты (наука)
        self.institut = QtWidgets.QLineEdit(parent=self.main_layout)
        self.institut.setObjectName("institut")
        self.people_layout.addWidget(self.institut, 1, 0, 1, 1)
        self.institut_info = QtWidgets.QLabel(parent=self.main_layout)
        self.institut_info.setObjectName("institut_info")
        self.people_layout.addWidget(self.institut_info, 1, 1, 1, 1)

        # Уровень развития
        self.level = QtWidgets.QLineEdit(parent=self.main_layout)
        self.level.setObjectName("level")
        self.people_layout.addWidget(self.level, 1, 2, 1, 1)
        self.level_info = QtWidgets.QLabel(parent=self.main_layout)
        self.level_info.setObjectName("level_info")
        self.people_layout.addWidget(self.level_info, 1, 3, 1, 1)

        self.gridLayout.addLayout(self.people_layout, 7, 0, 1, 1)

        # === СЕКЦИЯ ВОЙСК (ЮНИТОВ) ===
        self.unit_layout = QtWidgets.QGridLayout()
        self.unit_layout.setObjectName("unit_layout")

        # Воины
        self.war_unit = QtWidgets.QLabel(parent=self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.war_unit.sizePolicy().hasHeightForWidth())
        self.war_unit.setSizePolicy(sizePolicy)
        self.war_unit.setObjectName("war_unit")
        self.unit_layout.addWidget(self.war_unit, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.war_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.war_unit_input.sizePolicy().hasHeightForWidth())
        self.war_unit_input.setSizePolicy(sizePolicy)
        self.war_unit_input.setObjectName("war_unit_input")
        self.unit_layout.addWidget(self.war_unit_input, 0, 1, 1, 1)

        # Лучники
        self.arro_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.arro_unit.setObjectName("arro_unit")
        self.unit_layout.addWidget(self.arro_unit, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.arrow_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.arrow_unit_input.setObjectName("arrow_unit_input")
        self.unit_layout.addWidget(self.arrow_unit_input, 1, 1, 1, 1)

        # Волшебники
        self.mag_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.mag_unit.setObjectName("mag_unit")
        self.unit_layout.addWidget(self.mag_unit, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.mag_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.mag_unit_input.setObjectName("mag_unit_input")
        self.unit_layout.addWidget(self.mag_unit_input, 2, 1, 1, 1)

        # Пушки
        self.weapon_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.weapon_unit.setObjectName("weapon_unit")
        self.unit_layout.addWidget(self.weapon_unit, 3, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.weapon_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.weapon_unit_input.setObjectName("weapon_unit_input")
        self.unit_layout.addWidget(self.weapon_unit_input, 3, 1, 1, 1)

        # Военные корабли
        self.war_ship_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.war_ship_unit.setObjectName("war_ship_unit")
        self.unit_layout.addWidget(self.war_ship_unit, 4, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.war_ship_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.war_ship_unit_input.setObjectName("war_ship_unit_input")
        self.unit_layout.addWidget(self.war_ship_unit_input, 4, 1, 1, 1)

        # Военный транспорт
        self.war_ride_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.war_ride_unit.setObjectName("war_ride_unit")
        self.unit_layout.addWidget(self.war_ride_unit, 5, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.war_ride_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.war_ride_unit_input.setObjectName("war_ride_unit_input")
        self.unit_layout.addWidget(self.war_ride_unit_input, 5, 1, 1, 1)

        # Башни
        self.town_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.town_unit.setObjectName("town_unit")
        self.unit_layout.addWidget(self.town_unit, 6, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.town_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.town_unit_input.setObjectName("town_unit_input")
        self.unit_layout.addWidget(self.town_unit_input, 6, 1, 1, 1)

        # Транспорт
        self.ride_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.ride_unit.setObjectName("ride_unit")
        self.unit_layout.addWidget(self.ride_unit, 7, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.ride_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.ride_unit_input.setObjectName("ride_unit_input")
        self.unit_layout.addWidget(self.ride_unit_input, 7, 1, 1, 1)

        # Пункты (логистика)
        self.logic_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.logic_unit.setObjectName("logic_unit")
        self.unit_layout.addWidget(self.logic_unit, 8, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.logic_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.logic_unit_input.setObjectName("logic_unit_input")
        self.unit_layout.addWidget(self.logic_unit_input, 8, 1, 1, 1)

        # Склады
        self.cheast_unit = QtWidgets.QLabel(parent=self.main_layout)
        self.cheast_unit.setObjectName("cheast_unit")
        self.unit_layout.addWidget(self.cheast_unit, 9, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.cheast_unit_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.cheast_unit_input.setObjectName("cheast_unit_input")
        self.unit_layout.addWidget(self.cheast_unit_input, 9, 1, 1, 1)

        self.gridLayout.addLayout(self.unit_layout, 7, 1, 2, 1)

        # === СЕКЦИЯ ТОРГОВЛИ ===
        self.trade_layout = QtWidgets.QGridLayout()
        self.trade_layout.setObjectName("trade_layout")

        # Информация о торговле
        self.trade_info = QtWidgets.QLabel(parent=self.main_layout)
        self.trade_info.setObjectName("trade_info")
        self.trade_layout.addWidget(self.trade_info, 0, 0, 1, 1)
        self.trade_out = QtWidgets.QLineEdit(parent=self.main_layout)
        self.trade_out.setObjectName("trade_out")
        self.trade_layout.addWidget(self.trade_out, 0, 1, 1, 1)
        self.trade_kingdom_info = QtWidgets.QLabel(parent=self.main_layout)
        self.trade_kingdom_info.setObjectName("trade_kingdom_info")
        self.trade_layout.addWidget(self.trade_kingdom_info, 0, 2, 1, 1)
        self.trade_out_kingdom = QtWidgets.QLineEdit(parent=self.main_layout)
        self.trade_out_kingdom.setObjectName("trade_out_kingdom")
        self.trade_layout.addWidget(self.trade_out_kingdom, 0, 3, 1, 1)

        # Список торговых запросов
        self.request_out_info = QtWidgets.QLabel(parent=self.main_layout)
        self.request_out_info.setObjectName("request_out_info")
        self.trade_layout.addWidget(self.request_out_info, 1, 0, 1, 1)
        self.request_output = QtWidgets.QListWidget(parent=self.main_layout)
        self.request_output.setObjectName("request_output")
        self.trade_layout.addWidget(self.request_output, 1, 1, 1, 3)

        # Создание нового торгового запроса
        self.request_input = QtWidgets.QLineEdit(parent=self.main_layout)
        self.request_input.setObjectName("request_input")
        self.trade_layout.addWidget(self.request_input, 2, 0, 1, 2)
        self.request_input_btn = QtWidgets.QPushButton(parent=self.main_layout)
        self.request_input_btn.setObjectName("request_input_btn")
        self.trade_layout.addWidget(self.request_input_btn, 2, 2, 1, 2)

        self.gridLayout.addLayout(self.trade_layout, 8, 0, 1, 1)

        # === КНОПКА ВЫБОРА ФОТО ===
        self.kingdom_dialog_btn = QtWidgets.QPushButton(parent=self.main_layout)
        self.kingdom_dialog_btn.setObjectName("kingdom_dialog_btn")
        self.gridLayout.addWidget(self.kingdom_dialog_btn, 4, 1, 1, 1)

        # === СЕКЦИЯ ЭКОНОМИКИ ===
        self.economic_layout = QtWidgets.QGridLayout()
        self.economic_layout.setObjectName("economic_layout")

        # Прибыль
        self.economy_profit_info = QtWidgets.QLabel(parent=self.main_layout)
        self.economy_profit_info.setObjectName("economy_profit_info")
        self.economic_layout.addWidget(self.economy_profit_info, 0, 3, 1, 1)
        self.economy_profit = QtWidgets.QLineEdit(parent=self.main_layout)
        self.economy_profit.setObjectName("economy_profit")
        self.economic_layout.addWidget(self.economy_profit, 0, 4, 1, 1)

        # Казна
        self.economy_kazna_info = QtWidgets.QLabel(parent=self.main_layout)
        self.economy_kazna_info.setObjectName("economy_kazna_info")
        self.economic_layout.addWidget(self.economy_kazna_info, 1, 3, 1, 1)
        self.economy_kazna = QtWidgets.QLineEdit(parent=self.main_layout)
        self.economy_kazna.setObjectName("economy_kazna")
        self.economic_layout.addWidget(self.economy_kazna, 1, 4, 1, 1)

        # Кнопка следующего хода
        self.economic_next_btn = QtWidgets.QPushButton(parent=self.main_layout)
        self.economic_next_btn.setObjectName("economic_next_btn")
        self.economic_layout.addWidget(self.economic_next_btn, 2, 3, 1, 2)

        # Расходы
        self.economy_minus = QtWidgets.QLineEdit(parent=self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.economy_minus.sizePolicy().hasHeightForWidth())
        self.economy_minus.setSizePolicy(sizePolicy)
        self.economy_minus.setObjectName("economy_minus")
        self.economic_layout.addWidget(self.economy_minus, 0, 2, 3, 1)

        # Доходы
        self.economy_plus = QtWidgets.QLineEdit(parent=self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.economy_plus.sizePolicy().hasHeightForWidth())
        self.economy_plus.setSizePolicy(sizePolicy)
        self.economy_plus.setObjectName("economy_plus")
        self.economic_layout.addWidget(self.economy_plus, 0, 1, 3, 1)

        # Общая информация об экономике
        self.economy_info = QtWidgets.QLabel(parent=self.main_layout)
        self.economy_info.setObjectName("economy_info")
        self.economic_layout.addWidget(self.economy_info, 0, 0, 3, 1)

        self.gridLayout.addLayout(self.economic_layout, 0, 0, 5, 1)

        # === ИЗОБРАЖЕНИЕ КОРОЛЕВСТВА ===
        self.image = QtWidgets.QLabel(parent=self.main_layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMaximumSize(QtCore.QSize(390, 16777215))  # Ограничение по ширине
        self.image.setText("")  # Изначально пустое
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 1, 4, 1)

        # Добавление основного layout в центральный виджет
        self.horizontalLayout.addWidget(self.main_layout)
        MainWindow.setCentralWidget(self.centralwidget)

        # Создание меню и статусбара
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Инициализация текстовых элементов и подключение слотов
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Метод для установки текстовых значений всех элементов интерфейса"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "kingdom_helper"))

        # Установка текстов для секции ресурсов
        self.wheat_info.setText(_translate("MainWindow", "Пшеница"))
        self.wood_info.setText(_translate("MainWindow", "Дерево"))
        self.factor_info.setText(_translate("MainWindow", "Производство"))
        self.stone_info.setText(_translate("MainWindow", "Камень"))
        self.gold_info.setText(_translate("MainWindow", "Золото"))
        self.iron_info.setText(_translate("MainWindow", "Железо"))

        # Установка текстов для секции населения
        self.people_info.setText(_translate("MainWindow", "Люди"))
        self.happy_info.setText(_translate("MainWindow", "Счастье"))
        self.institut_info.setText(_translate("MainWindow", "Институты"))
        self.level_info.setText(_translate("MainWindow", "Уровень"))

        # Установка текстов для секции войск
        self.war_unit.setText(_translate("MainWindow", "воин"))
        self.arro_unit.setText(_translate("MainWindow", "Лучники"))
        self.mag_unit.setText(_translate("MainWindow", "волшебник"))
        self.weapon_unit.setText(_translate("MainWindow", "Пушка"))
        self.war_ship_unit.setText(_translate("MainWindow", "Военный корабль"))
        self.war_ride_unit.setText(_translate("MainWindow", "Военный транспорт"))
        self.town_unit.setText(_translate("MainWindow", "Башни"))
        self.ride_unit.setText(_translate("MainWindow", "Транспорт"))
        self.logic_unit.setText(_translate("MainWindow", "Пункты"))
        self.cheast_unit.setText(_translate("MainWindow", "Склады"))

        # Установка текстов для секции торговли
        self.trade_info.setText(_translate("MainWindow", "Цена"))
        self.trade_kingdom_info.setText(_translate("MainWindow", "Королевство"))
        self.request_out_info.setText(_translate("MainWindow", "Запросы"))
        self.request_input_btn.setText(_translate("MainWindow", "Создать запрос"))

        # Установка текстов для кнопок и экономики
        self.kingdom_dialog_btn.setText(_translate("MainWindow", "выбрать фото"))
        self.economy_profit_info.setText(_translate("MainWindow", "Получит"))
        self.economy_kazna_info.setText(_translate("MainWindow", "Имеется"))
        self.economic_next_btn.setText(_translate("MainWindow", "Сделать ход"))
        self.economy_info.setText(_translate("MainWindow", "Экономика"))
