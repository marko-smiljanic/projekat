from PySide2 import QtWidgets, QtGui, QtCore

import csv
import pathlib

# TODO: napisati metodu save_data() i pozivati je gde je potrebno, jos par modela u metadata + njihovi csv-ovi, s u visokoskolskim ustanovama


class GenerickiModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):  # data sadrzi metapodatke o tome kako model izgleda
        super().__init__(parent)
        self.lista_objekata = []

        # self.lista_objekata = [
        #   ["TF", "Tehnicki Fakultet",         "Novi Sad"],
        #   ["PO", "Poljoprivredni Fakultet",   "Novi Sad"],
        #   ...
        #]

        self.name = data["name"]
        self.source = data["source"]
        self.column_names = data["column_names"]           # lista naziva svih kolona (za GUI)
        self.load_data()

    #pomocna metoda
    def get_element(self, index):           #index ima oznacen red i kolonu, a jedan objekat je jedan red, index je qmodel index objekat
        return self.lista_objekata[index.row()]   #vrati iz liste objekata na poziciji koja je jednaka redu indeksa

    #moramo da redefinisemo
    def rowCount(self, index):           #jedan red u tabeli ce biti jedan objekat (recnik)
        return len(self.lista_objekata)

    def columnCount(self, index):                 #hocemo samo ime i index da prikazujemo
        return len(self.column_names)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if(role == QtCore.Qt.DisplayRole):  # proveriti indeks kolone?
            objekat = self.get_element(index)  # proveriti indeks reda?
            return objekat[index.column()]  # npr. objekat[0] -> dohvatamo Oznaku
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):             #za labele 
        if(orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole):      #TODO: Dodati utf-8
            return self.column_names[section]
        return None

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if(role == QtCore.Qt.EditRole and value != ""):
            objekat = self.get_element(index)
            objekat[index.column()] = value         #sacuvace prvu o ubojektu pa tu novu vrednostu setuje toj (izmenjenoj) koloni, sacuvance takodje u self.lista_objekata jer ga gadja po referenci
            self.save_data()
            return True
        return False

    def flags(self, index):                                     #zadrzimo sve stare flegove i dodamo novi
        return super().flags(index) | QtCore.Qt.ItemIsEditable  #| == or nad bitovima, zadrzimo stare flegove i dodamo novi da je editable\

    def load_data(self):
        input_csv = open("data/" + self.source)
        csv_reader = csv.reader(input_csv, delimiter=",")
        for row in csv_reader:
            self.lista_objekata.append(row)
        input_csv.close()

    def save_data(self):
        input_csv = open("data/" + self.source, 'w', newline='')
        csv_writer = csv.writer(input_csv, delimiter=",")
        csv_writer.writerows(self.lista_objekata)
        input_csv.close()
