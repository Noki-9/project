import sys
import os
import uuid
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QEvent
from template_main_load import Ui_LoadWindow
from template_main_window import Ui_MainWindow
from json_manager import KingdomJSON


class Load_window(QMainWindow, Ui_LoadWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        # Подключаем обработчики нажатия кнопок
        self.create_kingdom.clicked.connect(self.open_main_window)
        self.load_kingdom.clicked.connect(self.open_file_dialog)
        self.exit_btn.clicked.connect(self.close_application)

    def setupUi(self, parent):
        super().setupUi(parent)

    def open_main_window(self):
        """Открывает главное окно и закрывает текущее окно загрузки"""
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Закрываем окно загрузки

    def open_file_dialog(self):
        """Открывает диалог выбора файла королевства"""
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Выберите файл королевства",
            "./saves",  # Текущая директория
            "JSON файлы (*.json);;Все файлы (*)"
        )

        if file_path:
            # Извлекаем имя королевства из имени файла
            filename = os.path.basename(file_path)
            if filename.startswith("kingdom_") and filename.endswith(".json"):
                kingdom_name = filename[8:-5]  # Удаляем "kingdom_" и ".json"
                self.load_and_open_kingdom(kingdom_name)
            else:
                QMessageBox.warning(self, "Ошибка", "Неверный формат файла!")
        else:
            QMessageBox.information(self, "Отмена", "Файл не выбран.")

    def load_and_open_kingdom(self, kingdom_name):
        """Загружает королевство и открывает главное окно"""
        # Создаём главное окно
        self.main_window = MainWindow()

        # Загружаем данные
        data = KingdomJSON.load_kingdom(kingdom_name)
        if data:
            self.main_window.current_kingdom_name = kingdom_name
            self.main_window.load_data_from_dict(data)
            self.main_window.is_saved = False
            self.main_window.show()
            self.close()  # Закрываем окно загрузки
        else:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить королевство '{kingdom_name}'")

    def close_application(self):
        """Закрывает приложение"""
        self.close()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        # Значение экономики
        self.true_economy_kazna_value = 0

        self.current_kingdom_name = None
        self.is_saved = False

    def setupUi(self, parent):
        super().setupUi(self)

        self.economy_profit.setEnabled(False)
        self.trade_out.setEnabled(False)
        self.trade_out_kingdom.setEnabled(False)
        self.level.setEnabled(False)

        # Стартовые функции и подключения
        self.set_start_value()
        self.clicked_connect()

    def clicked_connect(self):
        # Подключаем кнопку диалога королевства к методу загрузки изображения
        self.kingdom_dialog_btn.clicked.connect(self.load_image)
        # Подключение кнопки обновления ходов
        self.economic_next_btn.clicked.connect(self.update_economy)
        self.economy_kazna.editingFinished.connect(self.on_economy_kazna_edited)
        self.request_input_btn.clicked.connect(self.request_connector)
        self.request_output.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.request_output.customContextMenuRequested.connect(self.on_request_context_menu)
        self.request_output.itemClicked.connect(self.on_request_item_clicked)
        self.kingdom_name.editingFinished.connect(self.set_name)
        self.people.editingFinished.connect(self.level_cheak)
        self.institut.editingFinished.connect(self.level_cheak)

    def level_cheak(self):
        try:
            people = int(self.people.text())
            institut = int(self.institut.text())
        except ValueError:
            self.statusbar.showMessage("Неверные данные")
            return

        if people == institut * 10 and int(self.level.text()) != institut:
            self.level.setText(f'{int(self.level.text()) + 1}')

    def set_name(self):
        self.current_kingdom_name = self.kingdom_name.text().strip().split(' ')[0]

    def on_request_item_clicked(self, item):
        """
        Обрабатывает клик по элементу в request_output.
        Извлекает name и count, заполняет поля trade_out_kingdom и trade_out.
        """
        text = item.text()

        # Парсим строку формата: name---------object-count
        # Ищем последний дефис (перед count)
        last_dash_pos = text.rfind('-')
        if last_dash_pos == -1:
            return  # Не нашли дефис — некорректный формат

        # Извлекаем count (всё после последнего дефиса)
        count = text[last_dash_pos + 1:]

        # Остаток строки до последнего дефиса
        remaining = text[:last_dash_pos]

        # Ищем первый фрагмент до дефисов (это name)
        # Дефисы идут после name, поэтому ищем первую последовательность без дефисов
        name = ""
        for char in remaining:
            if char != '-':
                name += char
            else:
                break  # Первый дефис после name — останавливаемся

        if not name or not count:
            return  # Данные не найдены

        # Заполняем поля
        self.trade_out_kingdom.setText(name)
        self.trade_out.setText(count)

    def on_request_context_menu(self, position):
        # Получаем элемент под курсором
        item = self.request_output.itemAt(position)
        if not item:
            return  # Если клик вне элемента — ничего не делаем

        # Создаём меню
        menu = QMenu(self)

        # Действие «Удалить»
        delete_action = menu.addAction("Удалить запрос")
        delete_action.triggered.connect(lambda: self.remove_request_item(item))

        # Показываем меню в позиции клика
        menu.exec(self.request_output.mapToGlobal(position))

    def remove_request_item(self, item):
        row = self.request_output.row(item)
        self.request_output.takeItem(row)

        # Сообщение в статусбар
        self.statusbar.showMessage("Запрос удалён", 3000)

    def request_connector(self):
        request = self.request_input.text().strip()

        # Проверка на пустой ввод
        if not request:
            self.statusbar.showMessage("Запрос не создан: поле пусто", 3000)
            return

        parts = request.split()
        # Проверка на 3 компонента
        if len(parts) != 3:
            self.statusbar.showMessage(
                "Ошибка: введите ровно 3 значения — name object count",
                3000
            )
            return

        name, object_name, count_str = parts

        # Проверка count на число
        if not count_str.isdigit() or int(count_str) <= 0:
            self.statusbar.showMessage(
                "Ошибка: count должен быть положительным числом",
                3000
            )
            return

        count = count_str  # оставляем строкой для вывода

        total_width = 40

        # Вычисляем длину фиксированной части
        fixed_part_length = len(object_name) + len(count) + 1  # +1 за дефис перед count
        available_dashes = total_width - len(name) - fixed_part_length

        # Формируем строку
        if available_dashes > 0:
            dashes = '-' * available_dashes
            result = f"{name}{dashes}{object_name}-{count}"
        else:
            # Если места недостаточно — компактный формат
            result = f"{name}-{object_name}-{count}"

        # Добавляем в список
        self.request_output.addItem(result)

        # Очищаем поле ввода
        self.request_input.clear()

        # Сообщение в статусбар
        self.statusbar.showMessage(f"Запрос добавлен: {result}", 3000)

    def on_economy_kazna_edited(self):
        current_value = self.economy_kazna.text().strip()

        try:
            current_value = list(map(int, current_value.replace(' ', '').replace('+', '-').split('-')))
        except Exception:
            self.statusbar.showMessage("Неверный ввод")
            self.economy_kazna.setText(self.true_economy_kazna_value)

        for i in range(len(current_value)):
            if current_value[i] == int(self.true_economy_kazna_value):
                current_value.pop(i)
                break

        self.true_economy_kazna_value = self.true_economy_kazna_value - sum(current_value)
        self.economy_kazna.setText(f'{self.true_economy_kazna_value}')

    def update_economy(self):
        try:
            plus = list(map(int, self.economy_plus.text().replace(' ', '').replace('-', '+').split('+')))
            minus = list(map(int, self.economy_minus.text().replace(' ', '').replace('+', '-').split('-')))
            people = int(self.people.text())
            gold = int(self.gold.text())
            level = int(self.level.text())
        except Exception:
            QMessageBox.critical(self, "Ошибка", f"Неверно заполнены поля")
            self.economy_plus.setText('0')
            self.economy_minus.setText('0')
            plus = minus = [0]
            people = 0
            gold = 1
            level = 1

        minus_num = sum(minus)
        if level <= 3:
            minus_num *= 1
        elif level > 3:
            minus_num *= 2
        elif level > 6:
            minus_num *= 3
        else:
            minus_num *= 4

        result = ((people * gold) + sum(plus)) - minus_num
        self.true_economy_kazna_value = int(self.economy_kazna.text()) + int(self.economy_profit.text())
        self.economy_kazna.setText(f"{int(self.economy_kazna.text()) + int(self.economy_profit.text())}")
        self.economy_profit.setText(str(result))

    def load_image(self):
        """Загружает изображение через диалоговое окно и отображает его в QLabel"""
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Выберите изображение для королевства",
            "",
            "Изображения (*.png *.jpg *.jpeg *.bmp *.gif *.tiff);;Все файлы (*)"
        )

        if file_path:
            try:
                pixmap = QPixmap(file_path)

                if not pixmap.isNull():
                    # Фиксированные максимальные размеры, основанные на структуре интерфейса
                    # Ширина: примерно равна ширине кнопки "выбрать фото" + отступы
                    max_width = 200  # Подбирается под размер кнопки

                    # Высота: чтобы не заходить ниже секции ресурсов (где находится stone_info)
                    max_height = 300  # Подбирается чтобы оставалось место для кнопки и названия королевства

                    # Масштабируем изображение с сохранением пропорций
                    scaled_pixmap = pixmap.scaled(
                        max_width,
                        max_height,
                        Qt.AspectRatioMode.KeepAspectRatio,
                        Qt.TransformationMode.SmoothTransformation
                    )

                    self.image.setPixmap(scaled_pixmap)
                    self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.statusbar.showMessage(f"Изображение загружено: {file_path.split('/')[-1]}", 3000)

                else:
                    QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение. Файл может быть поврежден.")

            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при загрузке изображения: {str(e)}")
        else:
            self.statusbar.showMessage("Выбор изображения отменен", 2000)

    def closeEvent(self, event: QEvent):
        """Обрабатывает закрытие окна — сохраняет данные, если есть изменения"""
        if self.current_kingdom_name and not self.is_saved:
            reply = QMessageBox.question(
                self,
                "Сохранить изменения",
                f"Сохранить королевство '{self.current_kingdom_name}' перед выходом?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel
            )

            if reply == QMessageBox.StandardButton.Yes:
                if self.save_kingdom():
                    event.accept()  # Закрываем окно
                else:
                    event.ignore()  # Не закрываем, если ошибка сохранения
            elif reply == QMessageBox.StandardButton.No:
                event.accept()  # Закрываем без сохранения
            else:
                event.ignore()  # Отменяем закрытие
        else:
            event.accept()  # Закрываем, если нет данных или уже сохранено

    def save_kingdom(self):
        """Сохраняет текущее состояние королевства (вызывается при закрытии)"""
        if not self.current_kingdom_name:
            name = self.kingdom_name.text().strip()
            if not name:
                QMessageBox.warning(self, "Ошибка", "Введите имя королевства!")
                return False
            self.current_kingdom_name = name

        data = self.collect_data()  # Собираем все данные

        if KingdomJSON.save_kingdom(self.current_kingdom_name, data):
            self.is_saved = True
            QMessageBox.information(self, "Сохранено", "Королевство сохранено")
            return True
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить данные!")
            return False

    def collect_data(self):
        """Собирает все данные интерфейса в словарь"""
        return {
            "name": self.current_kingdom_name if self.current_kingdom_name else self.kingdom_name.text().strip(),
            "resources": {
                "wheat": self.wheat.text(),
                "wood": self.wood.text(),
                "factor": self.factor.text(),
                "stone": self.stone.text(),
                "gold": self.gold.text(),
                "iron": self.iron.text()
            },
            "population": {
                "people": self.people.text(),
                "happy": self.happy.text(),
                "institut": self.institut.text(),
                "level": self.level.text()
            },
            "units": {
                "war": self.war_unit_input.text(),
                "arrow": self.arrow_unit_input.text(),
                "mag": self.mag_unit_input.text(),
                "town": self.town_unit_input.text(),
                "war_ship": self.war_ship_unit_input.text(),
                "war_ride": self.war_ride_unit_input.text(),
                "weapon": self.weapon_unit_input.text(),
                "ride": self.ride_unit_input.text(),
                "logic": self.logic_unit_input.text(),
                "cheast": self.cheast_unit_input.text()
            },
            "economy": {
                "profit": self.economy_profit.text(),
                "kazna": self.economy_kazna.text(),
                "plus": self.economy_plus.text(),
                "minus": self.economy_minus.text(),
                "true": str(self.true_economy_kazna_value)
            },
            "trade": {
                "out": self.trade_out.text(),
                "kingdom": self.trade_out_kingdom.text()
            },
            "requests": [
                self.request_output.item(i).text()
                for i in range(self.request_output.count())
            ],
            "image_path": self.get_image_path()
        }

    def get_image_path(self):
        """Получает путь к изображению или None"""
        pixmap = self.image.pixmap()
        if pixmap and not pixmap.isNull():
            # Сохраняем во временный файл с уникальным именем
            temp_path = f"temp_{uuid.uuid4().hex}.png"
            try:
                pixmap.save(f'saves/{temp_path}', "PNG")
                return temp_path
            except Exception as e:
                print(f"Ошибка сохранения изображения: {e}")
                return None
        return None

    def load_data_from_dict(self, data):
        """Заполняет интерфейс данными из словаря"""
        # Имя королевства
        self.kingdom_name.setText(data.get("name", ""))

        # Ресурсы
        res = data.get("resources", {})
        self.wheat.setText(res.get("wheat", ""))
        self.wood.setText(res.get("wood", ""))
        self.factor.setText(res.get("factor", ""))
        self.stone.setText(res.get("stone", ""))
        self.gold.setText(res.get("gold", ""))
        self.iron.setText(res.get("iron", ""))

        # Население
        pop = data.get("population", {})
        self.people.setText(pop.get("people", ""))
        self.happy.setText(pop.get("happy", ""))
        self.institut.setText(pop.get("institut", ""))
        self.level.setText(pop.get("level", ""))

        # Юниты
        units = data.get("units", {})
        self.war_unit_input.setText(units.get("war", ""))
        self.arrow_unit_input.setText(units.get("arrow", ""))
        self.mag_unit_input.setText(units.get("mag", ""))
        self.town_unit_input.setText(units.get("town", ""))
        self.war_ship_unit_input.setText(units.get("war_ship", ""))
        self.war_ride_unit_input.setText(units.get("war_ride", ""))
        self.weapon_unit_input.setText(units.get("weapon", ""))
        self.ride_unit_input.setText(units.get("ride", ""))
        self.logic_unit_input.setText(units.get("logic", ""))
        self.cheast_unit_input.setText(units.get("cheast", ""))

        # Экономика
        eco = data.get("economy", {})
        self.economy_profit.setText(eco.get("profit", ""))
        self.economy_kazna.setText(eco.get("kazna", ""))
        self.economy_plus.setText(eco.get("plus", ""))
        self.economy_minus.setText(eco.get("minus", ""))
        self.true_economy_kazna_value = int(eco.get("true", ""))

        # Торговля
        trade = data.get("trade", {})
        self.trade_out.setText(trade.get("out", ""))
        self.trade_out_kingdom.setText(trade.get("kingdom", ""))

        # Запросы
        requests = data.get("requests", [])
        self.request_output.clear()
        for req in requests:
            if isinstance(req, dict):
                self.request_output.addItem(req.get("item", ""))
            else:
                self.request_output.addItem(req)

        # Изображение
        image_path = data.get("image_path")
        if image_path:
            # Формируем полный путь: saves/имя_файла.png
            full_path = os.path.join("saves", image_path)

            # Проверяем существование папки и файла
            if os.path.exists("saves") and os.path.isfile(full_path):
                try:
                    pixmap = QPixmap(full_path)
                    if not pixmap.isNull():
                        max_width = 200
                        max_height = 300
                        scaled_pixmap = pixmap.scaled(
                            max_width,
                            max_height,
                            Qt.AspectRatioMode.KeepAspectRatio,
                            Qt.TransformationMode.SmoothTransformation
                        )
                        self.image.setPixmap(scaled_pixmap)
                        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
                        os.remove(full_path)
                    else:
                        print(f"Не удалось загрузить изображение: файл пуст или некорректен ({full_path})")
                except Exception as e:
                    print(f"Ошибка загрузки изображения из {full_path}: {e}")
            else:
                print(f"Файл изображения не найден: {full_path}")
        else:
            print("Путь к изображению не указан в данных")

    def set_start_value(self):
        self.economy_profit.setText("10")
        self.economy_kazna.setText("0")
        self.economy_plus.setText("0")
        self.economy_minus.setText("0")
        self.gold.setText("1")
        self.people.setText("17")
        self.level.setText('1')
        self.institut.setText('1')
        self.happy.setText('100')
        self.factor.setText('20')
        self.iron.setText('0')
        self.stone.setText('100')
        self.wheat.setText('30')
        self.wood.setText('100')
        self.war_unit_input.setText('0')
        self.arrow_unit_input.setText('0')
        self.mag_unit_input.setText('0')
        self.town_unit_input.setText('0')
        self.war_ship_unit_input.setText('0')
        self.war_ride_unit_input.setText('0')
        self.weapon_unit_input.setText('0')
        self.ride_unit_input.setText('0')
        self.logic_unit_input.setText('0')
        self.cheast_unit_input.setText('0')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Load_window()
    window.show()
    sys.exit(app.exec())
