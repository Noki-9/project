from PyQt6 import QtCore, QtWidgets


class Ui_LoadWindow(object):
    def setupUi(self, MainWindow):
        # Основные настройки главного окна
        MainWindow.setObjectName("Kingdom helper")
        MainWindow.resize(241, 219)  # Установка размеров окна

        # Создание центрального виджета
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Основной горизонтальный layout для центрального виджета
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Внутренний виджет для группировки элементов
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setObjectName("widget")

        # Вертикальный layout для кнопок и метки
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Метка с названием приложения
        self.name_label = QtWidgets.QLabel(parent=self.widget)
        self.name_label.setObjectName("name_label")
        # Выравнивание метки по центру
        self.verticalLayout.addWidget(self.name_label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Кнопка "Создать королевство"
        self.create_kingdom = QtWidgets.QPushButton(parent=self.widget)
        self.create_kingdom.setObjectName("create_kingdom")
        self.verticalLayout.addWidget(self.create_kingdom)

        # Кнопка "Загрузить королевство"
        self.load_kingdom = QtWidgets.QPushButton(parent=self.widget)
        self.load_kingdom.setObjectName("load_kingdom")
        self.verticalLayout.addWidget(self.load_kingdom)

        # Кнопка выхода
        self.exit_btn = QtWidgets.QPushButton(parent=self.widget)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)

        # Добавление виджета с кнопками в горизонтальный layout
        self.horizontalLayout.addWidget(self.widget)

        # Установка центрального виджета для главного окна
        MainWindow.setCentralWidget(self.centralwidget)

        # Создание меню бара
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 241, 21))  # Позиция и размеры
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Создание статус бара
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Инициализация текстовых элементов
        self.retranslateUi(MainWindow)
        # Автоматическое подключение слотов по именам
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """Метод для установки текстовых значений всех элементов интерфейса"""
        _translate = QtCore.QCoreApplication.translate

        # Установка заголовка окна
        MainWindow.setWindowTitle(_translate("MainWindow", "Kingdom helper"))

        # Настройка метки с названием приложения
        self.name_label.setToolTip(_translate("MainWindow", "<html><head/><body><p "
                                                            "align=\"center\"><span style=\" font-size:18pt;\">"
                                                            "Помошник в Kingdom</span></p></body></html>"))
        # Установка основного текста метки
        self.name_label.setText(_translate("MainWindow",
                                           "<html><head/><body><p align=\"center\">"
                                           "<span style=\" font-size:16pt;\">Помошник в Kingdom"
                                           "</span></p></body></html>"))

        # Установка текста кнопок
        self.create_kingdom.setText(_translate("MainWindow", "Создать"))
        self.load_kingdom.setText(_translate("MainWindow", "Загрузить"))
        self.exit_btn.setText(_translate("MainWindow", "выход"))
