from PySide2 import QtWidgets, QtGui, QtCore
from genericki_model import GenerickiModel

class InputForma(QtWidgets.QDialog):            #TODO: promeniti sirinu forme i ostalo jos da se obezbedi sekvencijalni integritet
    def __init__(self, parent, model):
        super().__init__(parent)
        self.model = model
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
        required_check = True
        for i in range(len(self.inputs)):
            if len(self.inputs[i].text()) == 0 and i not in self.model.no_required:
                required_check = False
                break
        if not required_check:
            self.reject() # zatvori formu i odbij unos - možemo kasnije izmeniti i tu funkciju
