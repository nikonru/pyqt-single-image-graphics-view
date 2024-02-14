from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView


class SingleImageGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__aspectRatioMode = Qt.KeepAspectRatio
        self.__initVal()

    def __initVal(self):
        self._scene = QGraphicsScene()
        self._p = QPixmap()
        self._item = ''

    def setFilename(self, filename: str):
        self._p = QPixmap(filename)
        self._setPixmap(self._p)

    def setPixmap(self, p):
        self._setPixmap(p)

    def _set_scene(self):
        p = self._p.scaled(self.width(), self.height(), self.__aspectRatioMode, Qt.SmoothTransformation)
        self._scene = QGraphicsScene()
        self._item = self._scene.addPixmap(p)
        self._scene.addItem(self._item)
        self.setScene(self._scene)

    def setAspectRatioMode(self, mode):
        self.__aspectRatioMode = mode

    def resizeEvent(self, e):
        if self._item:
            self._set_scene()
        return super().resizeEvent(e)