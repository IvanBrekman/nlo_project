import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtCore import Qt, QRect


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.can_paint = True

        self.size = 1.0
        self.step = 10
        self.x = self.y = 0
        self.screen_size = (800, 500)

        self.image = QImage('images/nlo.png')
        self.image_size = (int(self.image.width() * self.size), int(self.image.height() * self.size))

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Управление НЛО')
        self.setFixedSize(*self.screen_size)
        self.setMouseTracking(True)

    def paintEvent(self, event) -> None:
        if self.can_paint:
            painter = QPainter()

            painter.begin(self)
            painter.drawImage(QRect(self.x, self.y, *self.image_size), self.image)
            painter.end()

            self.can_paint = False

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Up:
            self.y -= self.step
        elif event.key() == Qt.Key_Down:
            self.y += self.step
        elif event.key() == Qt.Key_Left:
            self.x -= self.step
        elif event.key() == Qt.Key_Right:
            self.x += self.step
        else:
            return

        if self.x < 0:
            self.x = self.screen_size[0] - self.image_size[0]
        elif self.x > self.screen_size[0] - self.image_size[0]:
            self.x = 0
        elif self.y < 0:
            self.y = self.screen_size[1] - self.image_size[1]
        elif self.y > self.screen_size[1] - self.image_size[1]:
            self.y = 0

        self.can_paint = True
        self.repaint()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = Window()
    wnd.show()

    sys.excepthook = except_hook
    sys.exit(app.exec())
