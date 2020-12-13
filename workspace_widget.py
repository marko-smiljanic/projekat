from PySide2 import QtWidgets, QtGui, QtCore

from student import Student
from student_model import StudentModel
from polozeni_predmet import PolozeniPredmet
from nepolozeni_predmet import NepolozeniPredmet
from polozeni_predmet_model import PolozeniPredmetModel
from nepolozeni_predmet_model import NepolozeniPredmetModel
from genericki_model import GenerickiModel

class WorkspaceWidget(QtWidgets.QWidget):               #predstavlja deo u main_window-u, tj. kao neki nas centralni wgt
    def __init__(self, parent, model):
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()
        ##########################
        self.tabela1 = QtWidgets.QTableView(self.tab_widget)
        self.tabela1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabela1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabela1.setModel(model)  # main salje odgovarajuci model

        self.tabela1.clicked.connect(self.student_selected)         #na klik tabele se emituje odredjena metoda

        self.podtabela1 = QtWidgets.QTableView(self.tab_widget)
        self.podtabela2 = QtWidgets.QTableView(self.tab_widget)

        self.main_layout.addWidget(self.tabela1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def student_selected(self, index):                          #kada se klikne na studenta u tabeli
        model = self.tabela1.model()
        selektovani_student = model.get_element(index)

        model_polozeni = PolozeniPredmetModel()                 #ovde treba da isntanciram polozeni predmeti model i nepolozeni predmeti model i setujem im podatke, tj. setujem im iz studenta odgovarajucu listu
        model_polozeni.polozeni_predmeti = selektovani_student.polozeni_predmeti        #onda posle podtabeli1 i podtabeli2 setujem model na ove modele koje sam instancirao i dodelio im odgovarajucu listu
        self.podtabela1.setModel(model_polozeni)

        model_nepolozeni = NepolozeniPredmetModel()
        model_nepolozeni.nepolozeni_predmeti = selektovani_student.nepolozeni_predmeti
        self.podtabela2.setModel(model_nepolozeni)

        self.tab_widget.addTab(self.podtabela1, QtGui.QIcon("icons8-edit-file-64"), "Prva podtabela")       #na kraju dodam da se nove tabele prikazu u novim tabovima
        self.tab_widget.addTab(self.podtabela2, QtGui.QIcon("icons8-edit-file-64"), "Druga podtabela")

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_dummy_model(self):
        student_model = StudentModel()
        student_model.students = [
            Student("2019000000", "Marko Markovic", 
                [PolozeniPredmet("OOP1", "", 6), PolozeniPredmet("SIMS", "", 7)], 
                [NepolozeniPredmet("BP", "", 3), NepolozeniPredmet("AR", "", 2)]),
            
            Student("2019011111", "Petar Petrovic", 
                [PolozeniPredmet("OOP2", "", 8), PolozeniPredmet("OP", "", 8)],
                [NepolozeniPredmet("BP", "", 1), NepolozeniPredmet("AR", "", 1)]),
            
            Student("2019777777", "Janko Jankovic", 
                [PolozeniPredmet("OOP2", "", 9), PolozeniPredmet("OP", "", 10)],
                [NepolozeniPredmet("Matematika", "", 2), NepolozeniPredmet("Diskretna Matematika", "", 1)]),
            
            Student("2019555555", "Stefan Stefanovic", 
                [PolozeniPredmet("Engleski jezik 11", "", 6), PolozeniPredmet("OP", "", 6)],
                [NepolozeniPredmet("BP", "", 4), NepolozeniPredmet("OOP1", "", 2)]),
            
            Student("2019222222", "Ivan Ivanovic", 
                [PolozeniPredmet("Web dizajn", "", 7), PolozeniPredmet("OP", "", 8)],
                [NepolozeniPredmet("Matematika", "", 2), NepolozeniPredmet("AR", "", 1)])
        ]
        return student_model

    #def create_model(self, index):


























    # def __init__(self, parent):
    #     super().__init__(parent)

    #     self.main_layout = QtWidgets.QVBoxLayout()
    #     self.tab_widget = None
    #     self.create_tab_widget()
    #     self.main_text = QtWidgets.QTextEdit(self)
    #     self.main_layout.addWidget(self.main_text)
    #     self.main_layout.addWidget(self.tab_widget)
    #     self.setLayout(self.main_layout)

    # def show_tabs(self):
    #     self.tab_widget.addTab(QtWidgets.QTextEdit(self.tab_widget), QtGui.QIcon("student.png"), "Prva podtabela")
    #     self.tab_widget.addTab(QtWidgets.QTextEdit(self.tab_widget), QtGui.QIcon("student.png"), "Druga podtabela")

    # def show_text(self, text):
    #     self.main_text.setText(text)



    # def create_table(self, rows, columns):
    #     table_wgt = QtWidgets.QTableWidget(rows, columns, self)
    #     for i in range(0, rows):
    #         for j in range(0, columns):
    #             table_wgt.setItem(i, j, QtWidgets.QTableWidgetItem("Celija " + str(i) + str(j)))
        
    #     labels = []
    #     for i in range(0, columns):
    #         labels.append("Kolona: " + str(i))

    #     table_wgt.setHorizontalHeaderLabels(labels)
    #     return table_wgt


