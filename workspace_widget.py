from PySide2 import QtWidgets, QtGui, QtCore
from student import Student
from student_model import StudentModel
from polozeni_predmet import PolozeniPredmet
from nepolozeni_predmet import NepolozeniPredmet

class WorkspaceWidget(QtWidgets.QWidget):               #predstavlja deo u main_window-u, tj. kao neki nas centralni wgt
    def __init__(self, parent):
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()

        self.tabela1 = QtWidgets.QTableView(self.tab_widget)
        self.tabela1.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabela1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.student_model = self.create_dummy_model()
        self.tabela1.setModel(self.student_model)

        self.tabela1.clicked.connect(self.student_selected)

        self.podtabela1 = QtWidgets.QTableView(self.tab_widget)
        self.podtabela2 = QtWidgets.QTableView(self.tab_widget)

        self.main_layout.addWidget(self.tabela1)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)


    def student_selected(self, index):             #kada se klikne na studenta u tabeli
        model = self.tabela1.model()            #sta je ovo model?
        selektovani_student = model.get_element(index)
        #ovde treba da isntanciram polozeni predmeti model i nepolozeni predmeti model i setujem im podatke
        #onda posle podtabela1 set model polozeni predmeti model
        #podtabela2 set model nepolozeni predmeti model

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
                [PolozeniPredmet("OOP1", "", 7), PolozeniPredmet("SIMS", "", 8)],
                [NepolozeniPredmet("BP", "", 3), NepolozeniPredmet("AR", "", 2)]),
            
            Student("2019011111", "Petar Petrovic", 
                [PolozeniPredmet("OOP2", "", 7), PolozeniPredmet("OP", "", 8)],
                [NepolozeniPredmet("BP", "", 3), NepolozeniPredmet("AR", "", 2)]),
            
            Student("2019777777", "Janko Jankovic", 
                [PolozeniPredmet("OOP2", "", 7), PolozeniPredmet("OP", "", 8)],
                [NepolozeniPredmet("Matematika", "", 2), NepolozeniPredmet("Diskretna Matematika", "", 1)]),
            
            Student("2019555555", "Stefan Stefanovic", 
                [PolozeniPredmet("Engleski jezik 11", "", 7), PolozeniPredmet("OP", "", 8)],
                [NepolozeniPredmet("BP", "", 3), NepolozeniPredmet("OOP1", "", 2)]),
            
            Student("2019222222", "Ivan Ivanovic", 
                [PolozeniPredmet("Web dizajn", "", 7), PolozeniPredmet("OP", "", 8)],
                [NepolozeniPredmet("Matematika", "", 3), NepolozeniPredmet("AR", "", 2)])
        ]
        return student_model










































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


