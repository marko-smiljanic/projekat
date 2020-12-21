from PySide2 import QtWidgets, QtGui, QtCore

class StructureDock(QtWidgets.QDockWidget):
    kliknut = QtCore.Signal(str)                #signali (koje mi pravimo) moraju da budu atributi klase, ne u konstruktoru

    def __init__(self, title, parent):
        super().__init__(title, parent)

        data_path = QtCore.QDir.currentPath()
        data_path = data_path[:data_path.rfind('/')] + '/data'

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(data_path)  
        
        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(data_path))
        self.tree.clicked.connect(self.file_clicked)
        self.setWidget(self.tree)

    def file_clicked(self, index):
        print(self.model.filePath(index))
        print(self.model.fileName(index))
        path = self.model.filePath(index)
        self.kliknut.emit(path)