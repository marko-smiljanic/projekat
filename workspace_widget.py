from PySide2 import QtWidgets, QtGui, QtCore

from student import Student
from student_model import StudentModel
from polozeni_predmet import PolozeniPredmet
from nepolozeni_predmet import NepolozeniPredmet
from polozeni_predmet_model import PolozeniPredmetModel
from nepolozeni_predmet_model import NepolozeniPredmetModel
from genericki_model import GenerickiModel

class WorkspaceWidget(QtWidgets.QWidget):               #predstavlja deo u main_window-u, tj. kao neki nas centralni wgt
    def __init__(self, parent, model, models):
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()
        ##########################
        self.tabela = QtWidgets.QTableView(self.tab_widget)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabela.setModel(model)  # main salje odgovarajuci model
        self.models = models        # pamtimo sve postojece modele

        self.tabela.clicked.connect(self.row_selected)         #na klik tabele se emituje odredjena metoda

        #self.podtabela1 = QtWidgets.QTableView(self.tab_widget)
        #self.podtabela2 = QtWidgets.QTableView(self.tab_widget)

        self.main_layout.addWidget(self.tabela)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def row_selected(self, index):                          #kada se klikne na red u tabeli
        model = self.tabela.model()                         #model glavne tabele (u kojoj smo nesto kliknuli)
        selektovani_red = model.get_element(index)
        for child in model.children:
            for m in self.models:
                if child["name"] == m.name:

                    # napravimo medju-model (proxy) koji filtrira samo one redove koji zadovoljavaju neki uslov
                    # npr. podtabela "Nastavni predmeti" ispod tabele "Visokoskolska ustanova", prikazuje samo predmete iz selektovane ustanove
                    filter_proxy_model = QtCore.QSortFilterProxyModel()
                    filter_proxy_model.setSourceModel(m) # "child" model
                    filter_proxy_model.setFilterKeyColumn(child["column"])
                    filter_proxy_model.setFilterRegularExpression(selektovani_red[0])
                    
                    # filtriranje
                    
                    # postavljamo model koji sadrzi podskup redova iz generickog modela
                    podtabela = QtWidgets.QTableView(self.tab_widget)
                    podtabela.setModel(filter_proxy_model)
                    self.tab_widget.addTab(podtabela, QtGui.QIcon("icons8-edit-file-64"), m.name)
                    
                    break # predjemo na naredni child

        # model_polozeni = PolozeniPredmetModel()                 #ovde treba da isntanciram polozeni predmeti model i nepolozeni predmeti model i setujem im podatke, tj. setujem im iz studenta odgovarajucu listu
        # model_polozeni.polozeni_predmeti = selektovani_student.polozeni_predmeti        #onda posle podtabeli1 i podtabeli2 setujem model na ove modele koje sam instancirao i dodelio im odgovarajucu listu
        # self.podtabela1.setModel(model_polozeni)

        # model_nepolozeni = NepolozeniPredmetModel()
        # model_nepolozeni.nepolozeni_predmeti = selektovani_student.nepolozeni_predmeti
        # self.podtabela2.setModel(model_nepolozeni)

        # self.tab_widget.addTab(self.podtabela1, QtGui.QIcon("icons8-edit-file-64"), "Prva podtabela")       #na kraju dodam da se nove tabele prikazu u novim tabovima
        # self.tab_widget.addTab(self.podtabela2, QtGui.QIcon("icons8-edit-file-64"), "Druga podtabela")

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)
        #TODO: obezbediti da za svaki model postoji samo jedan otvoreni tab (da se ne duplira prilikom otvaranja)

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


