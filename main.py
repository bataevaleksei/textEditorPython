from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Редактор текста")
        self.setGeometry(300, 250, 750, 600)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):

        # Создаём полоску меню
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        # Создаём кнопку в менюшке
        fileMenu = QMenu("&Файл", self)
        self.menuBar.addMenu(fileMenu)

        # Добавляем кнопки действия при нажатии на кнопку fileMenu = "Файл"
        fileMenu.addAction('Открыть', self.action_clicked)
        fileMenu.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot() # Аннотация для обработки нажатия кнопок меню
    def action_clicked(self):
        action = self.sender()
        if action.text() == "Открыть":
            fname = QFileDialog.getOpenFileName(self, filter = "Text files (*.txt);;All files()")[0]
            # [0] Захватываем только первый выбранный файл, если выбранно много

            try:
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)

                f.close()
            except FileNotFoundError:
                print("No such file")

        elif action.text() == "Сохранить":
            fname = QFileDialog.getSaveFileName(self, filter = "Text files (*.txt);;All files()")[0]
            # [0] Захватываем только первый выбранный файл, если выбранно много
            try:

                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("No such file")





def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    application()