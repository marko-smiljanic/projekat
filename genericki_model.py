from PySide2 import QtWidgets, QtGui, QtCore

class GenerickiModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lista_objekata = []

    #pomocna metoda
    def get_element(self, index):           #index ima oznacen red i kolonu, a jedan student je jedan red, index je qmodel index objekat
        return self.lista_objekata[index.row()]   #vrati iz liste studenata na poziciji koja je jednaka redu indeksa

    #moramo da redefinisemo
    def rowCount(self, index):           #jedan red u tabeli ce biti jedan student
        return len(self.lista_objekata)

    def columnCount(self, index):
        if self.rowCount(index) > 0:                  #hocemo samo ime i index da prikazujemo
            return self.lista_objekata[0].get_no_columns() # dummy funkcija
        else:
            return 0

    def data(self, index, role=QtCore.Qt.DisplayRole):
        student = self.get_element(index)
        if(index.column() == 0 and role == QtCore.Qt.DisplayRole):  #displayRole je uloga za prikazivanje
            return student.broj_indeksa
        elif(index.column() == 1 and role == QtCore.Qt.DisplayRole):
            return student.ime_prezime
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):             #za labele
        if(section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole):
            return "Broj indeksa"
        elif(section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole):
            return "Ime i prezime"
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        student = self.get_element(index)
        if(value == ""):
            return False
        if(index.column() == 0 and role == QtCore.Qt.EditRole):
            student.broj_indeksa = value
            return True
        elif(index.column() == 1 and role == QtCore.Qt.EditRole):
            student.ime_prezime = value
            return True
        return False

    def flags(self, index):                                     #zadrzimo sve stare flegove i dodamo novi
        return super().flags(index) | QtCore.Qt.ItemIsEditable  #| == or nad bitovima, zadrzimo stare flegove i dodamo novi da je editable