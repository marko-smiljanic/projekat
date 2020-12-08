from PySide2 import QtWidgets, QtGui, QtCore

class StudentModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.students = []

    #pomocna metoda
    def get_element(self, index):           #index ima oznacen red i kolonu, a jedan student je jedan red, index je qmodel index objekat
        return self.students[index.row()]   #vrati iz liste studenata na poziciji koja je jednaka redu indeksa

    #moramo da redefinisemo
    def rowCount(self, inex):           #jedan red u tabeli ce biti jedan student
        return len(self.students)

    def columnCount(self, index):
        return 2                    #hocemo samo ime i index da prikazujemo

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
        