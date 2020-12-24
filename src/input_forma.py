from PySide2 import QtWidgets, QtGui, QtCore
from genericki_model import GenerickiModel

class InputForma(QtWidgets.QDialog):            #TODO: promeniti sirinu forme
    def __init__(self, parent, model, models):
        super().__init__(parent)
        self.model = model
        self.models = models                          #za poroveru sekvencijalnog integriteta
        self.inputs = []
        self.createFormGroupBox()
        buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)         #obe (accept i reject) po default-u zatvaraju formu, obe su iz QDialog
        buttonBox.rejected.connect(self.reject)
        
        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle(model.name + ": novi unos")
        
    def createFormGroupBox(self):
        self.formGroupBox = QtWidgets.QGroupBox("Unesite podatke")
        layout = QtWidgets.QFormLayout()
        for name in self.model.column_names:
            text_input = QtWidgets.QLineEdit()
            layout.addRow(QtWidgets.QLabel(name), text_input)
            self.inputs.append(text_input)
        self.formGroupBox.setLayout(layout)

    #override
    def accept(self):
        # provera: da li su popunjena obavezna polja
        required_check = True
        for i in range(len(self.inputs)):
            if len(self.inputs[i].text()) == 0 and i not in self.model.not_required:
                required_check = False
                break
        if not required_check:
            self.reject()
            return                           #zatvori formu i odbij unos - mozemo kasnije izmeniti i tu funkciju
        # provera: da li je ocuvan sekvencijalni integritet (da li uneseni strani kljuc(evi)) postoje u parent modelu
        # for parent in self.model.parents:
        #     for m in self.models: 
        #         if m.name == parent["name"]:     #nasli smo parent model
                    #TODO: nekako obezbediti sekvencijalni integritet???
                    #ne znam kako da proverim vrednosti iz parent["columns"] sa primary_key iz parent modela
        new_row = []
        for input_value in self.inputs:
            new_row.append(input_value.text())            #izvadimo tekst iz (value) input polja
        self.model.add_data(new_row)
        super().accept() # da je prihvacen rezultat dijaloga, zovemo QDialog.accept()
                    



