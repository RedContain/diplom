import os
import sys
import shutil
from datetime import datetime
from PySide6.QtCore import Qt, QPointF, QPoint
from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPixmap, QPen, QBrush, QColor, QFont, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox, QFileDialog, QGraphicsScene, QGraphicsPixmapItem, QGraphicsEllipseItem

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader

from ui_plane import Ui_MainWindow
from python_files.database.database_handler import DatabaseHandler


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.db = DatabaseHandler()
        self.current_map_id = None
        self.current_scene = None
        self.current_scene_display = None
        self.marker_items = []  # Точки на сцене настроек
        self.marker_items_display = []  # Точки на сцене показа

        # Режимы работы
        self.is_edit_mode = False
        self.pending_marker = None  # Временная точка ожидающая привязки

        # Переменная для хранения ID выбранной комнаты из таблицы
        self.selected_room_id = None

        # Настраиваем статус бар для сообщений
        self.status_label = QtWidgets.QLabel()
        self.status_label.setStyleSheet("QLabel { color: green; font-weight: bold; padding: 2px; }")
        self.statusbar.addPermanentWidget(self.status_label)
        self.show_status("Готов к работе")

        self.load_branches_to_combobox()
        self.connect_signals()

        # Подключаем двойной клик по таблице для выбора комнаты
        self.tableView.doubleClicked.connect(self.on_table_double_click)

    def show_status(self, message, is_error=False):
        """Показывает сообщение в статусбаре"""
        self.status_label.setText(f"  {message}  ")
        if is_error:
            self.status_label.setStyleSheet("QLabel { color: red; font-weight: bold; padding: 2px; }")
        else:
            self.status_label.setStyleSheet("QLabel { color: green; font-weight: bold; padding: 2px; }")

    def connect_signals(self):
        # Вкладка Настройки
        self.comboBox.currentIndexChanged.connect(self.on_branch_changed_settings)
        self.spinBox.valueChanged.connect(self.on_floor_changed_settings)
        self.pushButton.clicked.connect(self.on_load_map_clicked)
        self.pushButton_2.clicked.connect(self.on_edit_map_clicked)
        self.pushButton_3.clicked.connect(self.on_delete_map_clicked)
        self.pushButton_8.clicked.connect(self.on_save_map_clicked)

        # Вкладка Показ
        self.comboBox_2.currentIndexChanged.connect(self.on_branch_changed_display)
        self.spinBox_2.valueChanged.connect(self.on_floor_changed_display)
        self.pushButton_6.clicked.connect(self.on_export_all_pdf)
        self.pushButton_7.clicked.connect(self.on_export_floor_pdf)

    def load_branches_to_combobox(self):
        """Загрузка филиалов в комбобоксы"""
        branches = self.db.get_all_branches()
        for combo in [self.comboBox, self.comboBox_2]:
            combo.clear()
            combo.addItem("Выберите филиал", None)
            for branch in branches:
                combo.addItem(branch['name'], branch['branch_id'])
        self.show_status(f"Загружено {len(branches)} филиалов")

    def show_message(self, title, text, icon=QMessageBox.Information):
        """Оставляем только для критических ошибок"""
        if icon == QMessageBox.Critical:
            msg = QMessageBox()
            msg.setIcon(icon)
            msg.setWindowTitle(title)
            msg.setText(text)
            msg.exec_()
        else:
            self.show_status(text)

    def clear_graphics_view(self, graphics_view):
        """Очистка graphics view"""
        graphics_view.setScene(None)

    # ========== МЕТОДЫ ДЛЯ ВКЛАДКИ НАСТРОЙКИ ==========

    def on_branch_changed_settings(self, index):
        """Смена филиала в настройках"""
        self.clear_graphics_view(self.graphicsView)
        self.current_scene = None
        self.marker_items = []
        self.current_map_id = None
        self.spinBox.setValue(1)
        self.load_rooms_to_table()

    def on_floor_changed_settings(self, floor):
        """Смена этажа в настройках"""
        self.load_rooms_to_table()
        branch_id = self.comboBox.currentData()
        if branch_id:
            self.display_map_settings(branch_id, floor)

    def load_rooms_to_table(self):
        """Загрузка комнат в таблицу"""
        branch_id = self.comboBox.currentData()
        floor = self.spinBox.value()

        if not branch_id:
            return

        rooms = self.db.get_rooms_by_branch_and_floor(branch_id, floor)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['ID', 'Номер', 'Название', 'Вместимость'])

        for room in rooms:
            id_item = QStandardItem(str(room['room_id']))
            num_item = QStandardItem(room['room_number'])
            name_item = QStandardItem(room['room_name'])
            capacity_item = QStandardItem(str(room['capacity']))

            id_item.setEditable(False)
            num_item.setEditable(False)
            name_item.setEditable(False)
            capacity_item.setEditable(False)

            model.appendRow([id_item, num_item, name_item, capacity_item])

        self.tableView.setModel(model)
        self.tableView.setColumnHidden(0, True)  # Скрываем колонку с ID
        self.show_status(f"Загружено {len(rooms)} комнат")

    def on_table_double_click(self, index):
        """Двойной клик по таблице - выбор комнаты для привязки"""
        if not self.pending_marker:
            self.show_status("Сначала поставьте точку на схеме!", True)
            return

        model = self.tableView.model()
        row = index.row()
        room_id = model.data(model.index(row, 0))
        room_number = model.data(model.index(row, 1))
        room_name = model.data(model.index(row, 2))

        # Привязываем комнату к точке
        self.pending_marker.setBrush(QBrush(QColor(0, 255, 0, 180)))  # Зеленая - привязана
        self.pending_marker.setData(0, room_id)  # Сохраняем ID комнаты

        # Добавляем текст с номером комнаты рядом с точкой
        font = QFont("Arial", 8)
        text = self.current_scene.addText(f"{room_number}", font)
        text.setPos(self.pending_marker.rect().center().x() + 15,
                    self.pending_marker.rect().center().y() - 10)
        text.setData(0, room_id)

        self.marker_items.append(self.pending_marker)
        self.marker_items.append(text)

        self.pending_marker = None
        self.show_status(f"Точка привязана к комнате {room_number} - {room_name}")

    def on_load_map_clicked(self):
        """Загрузка схемы этажа"""
        branch_id = self.comboBox.currentData()
        floor = self.spinBox.value()

        if not branch_id:
            self.show_status("Сначала выберите филиал!", True)
            return

        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите схему этажа", "", "Images (*.png *.jpg *.jpeg)")
        if not file_path:
            return

        maps_dir = "floor_maps"
        os.makedirs(maps_dir, exist_ok=True)

        file_ext = os.path.splitext(file_path)[1]
        new_file_name = f"branch_{branch_id}_floor_{floor}{file_ext}"
        new_file_path = os.path.join(maps_dir, new_file_name)
        shutil.copy2(file_path, new_file_path)

        self.db.save_floor_map(branch_id, floor, new_file_path)
        self.display_map_settings(branch_id, floor)
        self.show_status("Схема загружена и сохранена!")

    def on_edit_map_clicked(self):
        """Включение/выключение режима редактирования"""
        if not self.current_map_id:
            self.show_status("Сначала загрузите схему для этого этажа!", True)
            return

        self.is_edit_mode = not self.is_edit_mode

        if self.is_edit_mode:
            self.pushButton_2.setText("Выключить редактирование")
            self.graphicsView.setCursor(Qt.CrossCursor)
            self.show_status("Режим: кликните на схеме чтобы поставить точку, затем выберите комнату в таблице")
        else:
            self.pushButton_2.setText("Редактировать схему")
            self.graphicsView.setCursor(Qt.ArrowCursor)
            self.pending_marker = None  # Сбрасываем ожидающую точку
            self.show_status("Режим редактирования выключен")

    def on_delete_map_clicked(self):
        """Удаление схемы или точек"""
        if not self.current_map_id:
            self.show_status("Нет загруженной схемы для удаления!", True)
            return

        dialog = QMessageBox(self)
        dialog.setWindowTitle("Удаление")
        dialog.setText("Что вы хотите удалить?")
        delete_all_btn = dialog.addButton("Всю схему с точками", QMessageBox.YesRole)
        delete_markers_btn = dialog.addButton("Только точки", QMessageBox.NoRole)
        cancel_btn = dialog.addButton("Отмена", QMessageBox.RejectRole)

        dialog.exec_()

        if dialog.clickedButton() == delete_all_btn:
            self.db.delete_full_map(self.current_map_id)
            self.clear_graphics_view(self.graphicsView)
            self.current_map_id = None
            self.current_scene = None
            self.marker_items = []
            self.show_status("Схема и точки удалены")
        elif dialog.clickedButton() == delete_markers_btn:
            self.db.delete_markers_by_map(self.current_map_id)
            branch_id = self.comboBox.currentData()
            floor = self.spinBox.value()
            self.display_map_settings(branch_id, floor)
            self.show_status("Все точки удалены")

    def on_save_map_clicked(self):
        """Сохранение всех точек в БД"""
        if not self.current_map_id or not self.current_scene:
            return

        saved_count = 0
        for item in self.marker_items:
            if isinstance(item, QGraphicsEllipseItem):
                room_id = item.data(0)
                if room_id:  # Сохраняем только привязанные точки
                    rect = item.rect()
                    center = item.mapToScene(rect.center())
                    x, y = center.x(), center.y()

                    self.db.add_marker(self.current_map_id, room_id, x, y)
                    saved_count += 1

        if saved_count > 0:
            self.show_status(f"Сохранено {saved_count} точек")
        else:
            self.show_status("Нет точек для сохранения", True)

    def mousePressEvent(self, event):
        """Обработка кликов мыши"""
        super(MainWindow, self).mousePressEvent(event)

        # Проверяем режим редактирования и клик левой кнопкой
        if not self.is_edit_mode or event.button() != Qt.LeftButton:
            return

        # Проверяем что есть загруженная схема
        if not self.current_scene:
            self.show_status("Сначала загрузите схему!", True)
            return

        # Получаем координаты клика относительно graphicsView
        view_pos = self.graphicsView.mapFromGlobal(event.globalPosition().toPoint())
        scene_pos = self.graphicsView.mapToScene(view_pos)

        # Проверяем что клик был в пределах сцены
        if not self.graphicsView.sceneRect().contains(scene_pos):
            return

        # Создаем временную синюю точку
        self.create_temp_marker(scene_pos.x(), scene_pos.y())

    def create_temp_marker(self, x, y):
        """Создание временной синей точки"""
        if not self.current_scene:
            return

        # Если есть предыдущая непривязанная точка - удаляем её
        if self.pending_marker:
            self.current_scene.removeItem(self.pending_marker)

        # Создаем новую точку
        pen = QPen(Qt.blue)
        pen.setWidth(2)
        brush = QBrush(QColor(0, 0, 255, 180))  # Синяя

        ellipse = QGraphicsEllipseItem(x - 8, y - 8, 16, 16)
        ellipse.setPen(pen)
        ellipse.setBrush(brush)
        ellipse.setFlag(QGraphicsEllipseItem.ItemIsMovable, True)
        ellipse.setFlag(QGraphicsEllipseItem.ItemIsSelectable, True)
        ellipse.setData(0, None)  # Пока без комнаты

        self.current_scene.addItem(ellipse)
        self.pending_marker = ellipse

        self.show_status("Точка поставлена, выберите комнату в таблице двойным кликом")

    def display_map_settings(self, branch_id, floor):
        """Отображение карты в настройках"""
        self.clear_graphics_view(self.graphicsView)

        map_info, markers = self.db.get_map_data(branch_id, floor)
        if not map_info:
            return

        self.current_map_id = map_info['map_id']
        scene = QGraphicsScene()
        self.current_scene = scene

        # Загружаем картинку
        pixmap = QPixmap(map_info['image_path'])
        if pixmap.isNull():
            self.show_status("Не удалось загрузить изображение схемы", True)
            return

        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        # Рисуем сохраненные маркеры
        self.marker_items = []
        for marker in markers:
            x, y, room_id, room_name, room_number = marker

            # Точка
            pen = QPen(Qt.green)
            pen.setWidth(2)
            brush = QBrush(QColor(0, 255, 0, 180))

            ellipse = QGraphicsEllipseItem(x - 8, y - 8, 16, 16)
            ellipse.setPen(pen)
            ellipse.setBrush(brush)
            ellipse.setFlag(QGraphicsEllipseItem.ItemIsMovable, True)
            ellipse.setFlag(QGraphicsEllipseItem.ItemIsSelectable, True)
            ellipse.setData(0, room_id)
            scene.addItem(ellipse)
            self.marker_items.append(ellipse)

            # Текст
            font = QFont("Arial", 8)
            text = scene.addText(f"{room_number}", font)
            text.setPos(x + 12, y - 8)
            text.setData(0, room_id)
            self.marker_items.append(text)

        self.graphicsView.setScene(scene)
        self.graphicsView.fitInView(pixmap_item, Qt.KeepAspectRatio)
        self.show_status(f"Загружено {len(markers)} точек")

    # ========== МЕТОДЫ ДЛЯ ВКЛАДКИ ПОКАЗ ==========

    def on_branch_changed_display(self, index):
        """Смена филиала в показе"""
        branch_id = self.comboBox_2.currentData()
        if branch_id:
            self.spinBox_2.setValue(1)
            self.display_map_display(branch_id, 1)

    def on_floor_changed_display(self, floor):
        """Смена этажа в показе"""
        branch_id = self.comboBox_2.currentData()
        if branch_id:
            self.display_map_display(branch_id, floor)

    def display_map_display(self, branch_id, floor):
        """Отображение карты в показе (только для просмотра)"""
        self.clear_graphics_view(self.graphicsView_2)

        map_info, markers = self.db.get_map_data(branch_id, floor)
        if not map_info:
            self.show_status(f"Нет схемы для этажа {floor}", True)
            return

        scene = QGraphicsScene()

        # Загружаем картинку
        pixmap = QPixmap(map_info['image_path'])
        if pixmap.isNull():
            self.show_status("Не удалось загрузить изображение", True)
            return

        pixmap_item = QGraphicsPixmapItem(pixmap)
        scene.addItem(pixmap_item)

        # Рисуем маркеры
        for marker in markers:
            x, y, room_id, room_name, room_number = marker

            # Точка (синяя, маленькая, неактивная)
            pen = QPen(Qt.blue)
            pen.setWidth(2)
            brush = QBrush(QColor(0, 0, 255, 100))

            ellipse = QGraphicsEllipseItem(x - 8, y - 8, 16, 16)
            ellipse.setPen(pen)
            ellipse.setBrush(brush)
            ellipse.setData(0, room_id)
            ellipse.setToolTip(f"{room_number} - {room_name}")
            # Убираем возможность выделения
            ellipse.setFlag(QGraphicsEllipseItem.ItemIsSelectable, False)
            ellipse.setFlag(QGraphicsEllipseItem.ItemIsMovable, False)
            scene.addItem(ellipse)

            # Текст (только номер)
            font = QFont("Arial", 6)
            text = scene.addText(room_number, font)
            text.setPos(x + 6, y - 6)
            text.setFlag(QGraphicsEllipseItem.ItemIsSelectable, False)

        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.fitInView(pixmap_item, Qt.KeepAspectRatio)
        self.show_status(f"Показан этаж {floor}, {len(markers)} помещений")

    # ========== МЕТОДЫ ДЛЯ PDF ==========

    def on_export_all_pdf(self):
        """Экспорт всех этажей в PDF"""
        branch_id = self.comboBox_2.currentData()
        if not branch_id:
            self.show_status("Выберите филиал!", True)
            return

        branch = self.db.get_branch(branch_id)
        if not branch:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить отчет", f"отчет_{branch['name']}.pdf", "PDF Files (*.pdf)"
        )
        if not file_path:
            return

        try:
            self.show_status("Генерация PDF...")
            from reportlab.lib.pagesizes import A4, landscape
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.lib import colors
            from reportlab.lib.units import mm

            doc = SimpleDocTemplate(file_path, pagesize=landscape(A4))
            story = []
            styles = getSampleStyleSheet()

            # Заголовок
            story.append(Paragraph(f"Филиал: {branch['name']}", styles['Title']))
            story.append(Paragraph(f"Адрес: {branch['address']}", styles['Normal']))
            story.append(Paragraph(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}", styles['Normal']))
            story.append(Spacer(1, 10*mm))

            for floor in range(1, branch['floors_count'] + 1):
                # Заголовок этажа
                story.append(Paragraph(f"Этаж {floor}", styles['Heading2']))
                story.append(Spacer(1, 5*mm))

                map_info, markers = self.db.get_map_data(branch_id, floor)

                # Схема
                if map_info and os.path.exists(map_info['image_path']):
                    img = Image(map_info['image_path'])
                    img.drawHeight = 80*mm
                    img.drawWidth = 120*mm
                    story.append(img)
                    story.append(Spacer(1, 5*mm))

                # Таблица с кабинетами
                if markers:
                    data = [['№', 'Кабинет', 'Название', 'Вместимость']]
                    for i, marker in enumerate(markers, 1):
                        room = self.db.get_room(marker['room_id'])
                        data.append([
                            str(i),
                            marker['room_number'],
                            marker['room_name'],
                            str(room['capacity'] if room else '')
                        ])

                    table = Table(data, colWidths=[20*mm, 30*mm, 70*mm, 30*mm])
                    table.setStyle(TableStyle([
                        ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ]))
                    story.append(table)

                story.append(Spacer(1, 10*mm))

            doc.build(story)
            self.show_status(f"Отчет сохранен: {os.path.basename(file_path)}")

        except Exception as e:
            self.show_status(f"Ошибка создания PDF: {str(e)}", True)

    def on_export_floor_pdf(self):
        """Экспорт текущего этажа в PDF"""
        branch_id = self.comboBox_2.currentData()
        floor = self.spinBox_2.value()

        if not branch_id:
            self.show_status("Выберите филиал!", True)
            return

        branch = self.db.get_branch(branch_id)
        if not branch:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить отчет", f"отчет_{branch['name']}_этаж_{floor}.pdf", "PDF Files (*.pdf)"
        )
        if not file_path:
            return

        try:
            self.show_status("Генерация PDF...")
            from reportlab.lib.pagesizes import A4, landscape
            from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
            from reportlab.lib.styles import getSampleStyleSheet
            from reportlab.lib import colors
            from reportlab.lib.units import mm

            doc = SimpleDocTemplate(file_path, pagesize=landscape(A4))
            story = []
            styles = getSampleStyleSheet()

            # Заголовок
            story.append(Paragraph(f"Филиал: {branch['name']}", styles['Title']))
            story.append(Paragraph(f"Адрес: {branch['address']}", styles['Normal']))
            story.append(Paragraph(f"Дата: {datetime.now().strftime('%d.%m.%Y %H:%M')}", styles['Normal']))
            story.append(Spacer(1, 10*mm))

            # Заголовок этажа
            story.append(Paragraph(f"Этаж {floor}", styles['Heading2']))
            story.append(Spacer(1, 5*mm))

            map_info, markers = self.db.get_map_data(branch_id, floor)

            # Схема
            if map_info and os.path.exists(map_info['image_path']):
                img = Image(map_info['image_path'])
                img.drawHeight = 80*mm
                img.drawWidth = 120*mm
                story.append(img)
                story.append(Spacer(1, 5*mm))

            # Таблица с кабинетами
            if markers:
                data = [['№', 'Кабинет', 'Название', 'Вместимость']]
                for i, marker in enumerate(markers, 1):
                    room = self.db.get_room(marker['room_id'])
                    data.append([
                        str(i),
                        marker['room_number'],
                        marker['room_name'],
                        str(room['capacity'] if room else '')
                    ])

                table = Table(data, colWidths=[20*mm, 30*mm, 70*mm, 30*mm])
                table.setStyle(TableStyle([
                    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                    ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ]))
                story.append(table)

            doc.build(story)
            self.show_status(f"Отчет сохранен: {os.path.basename(file_path)}")

        except Exception as e:
            self.show_status(f"Ошибка создания PDF: {str(e)}", True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())