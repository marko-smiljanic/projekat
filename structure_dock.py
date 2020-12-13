from PySide2 import QtWidgets, QtGui, QtCore

class StructureDock(QtWidgets.QDockWidget):
    kliknut = QtCore.Signal(str)                #signali (koje mi pravimo) moraju da budu atributi klase, ne u konstruktoru

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(QtCore.QDir.currentPath() + "/data")
        
        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QtCore.QDir.currentPath() + "/data"))
        self.tree.clicked.connect(self.file_clicked)
        self.setWidget(self.tree)

    def file_clicked(self, index):
        print(self.model.filePath(index))
        print(self.model.fileName(index))
        path = self.model.filePath(index)
        self.kliknut.emit(path)