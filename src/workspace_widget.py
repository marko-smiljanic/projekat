from PySide2 import QtWidgets, QtGui, QtCore

from genericki_model import GenerickiModel
from input_forma import InputForma

class WorkspaceWidget(QtWidgets.QWidget):               #predstavlja deo u main_window-u, tj. kao neki nas centralni wgt
    def __init__(self, parent, model, models):          #cemu sluzi model?
        super().__init__(parent)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()
        ##########################
        self.tabela = QtWidgets.QTableView(self.tab_widget)
        self.tabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)   #kada kliknem i vucem (dok je kliknut) po tabeli
        self.tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)    #sta da selektuje kad se klikne na red
        self.tabela.setModel(model)                                                 # main salje odgovarajuci model
        self.models = models                                                        # pamtimo sve postojece modele
        self.button = QtWidgets.QPushButton("Dodaj u glavnu tabelu")
        self.forma = InputForma(self, model)
        self.button.clicked.connect(self.button_clicked)

        self.tabela.clicked.connect(self.row_selected)         #na klik tabele se emituje odredjena metoda, treba postaviti i za ostale tabele

        self.main_layout.addWidget(self.tabela)
        self.main_layout.addWidget(self.button)
        self.main_layout.addWidget(self.tab_widget)
        
        self.setLayout(self.main_layout)

    def row_selected(self, index):                          #kada se klikne na red u tabeli
        model = self.tabela.model()                         #model glavne tabele (u kojoj smo nesto kliknuli), genericki model, koji smo joj prosledili
        selektovani_red = model.get_element(index)
        for child in self.models:           # prodjemo kroz sve modele
            for parent in child.parents:    # i medju njihovim parent-ima (ako ih ima)
                if parent["name"] == model.name:         # nadjemo sebe (tako znamo da nam je child)
                    
                    podtabela_model = child
                    for i in range(len(model.primary_key)):
                        filter_proxy_model = QtCore.QSortFilterProxyModel()
                        filter_proxy_model.setSourceModel(podtabela_model)
                        filter_proxy_model.setFilterKeyColumn(parent["columns"][i])  # u parent["columns"] pise u koje od nasih kolona se preslikava primary key kolone iz roditelja
                        filter_proxy_model.setFilterRegularExpression(selektovani_red[model.primary_key[i]]) #prolazimo krozk olone koje sacinjavaju primary_key od parent-a 
                        podtabela_model = filter_proxy_model

                    podtabela = QtWidgets.QTableView(self.tab_widget)
                    podtabela.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)  #kada kliknem i vucem (dok je kliknut) po tabeli
                    podtabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)   #sta da selektuje kad se klikne na red
                    podtabela.setModel(podtabela_model)                      # postavljamo model koji sadrzi podskup redova iz generickog modela
                    #podtabela.clicked.connect(self.row_selected)         #TODO: mozda? treba dodati clicked i ovde ali treba definisati kako da se ponasa, jer ovaj za gornju tabelu ne radi dobro
                    self.tab_widget.addTab(podtabela, QtGui.QIcon("../slike/icons8-edit-file-64"), child.name)
                    
                    break # predjemo na naredni child 

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)
        #TODO: obezbediti da za svaki model postoji samo jedan otvoreni tab (da se ne duplira prilikom otvaranja)

    def button_clicked(self):
        self.forma.show()



























    # def __init__(self, parent):
    #     super().__init__(parent)

    #     self.main_layout = QtWidgets.QVBoxLayout()
    #     self.tab_widget = None
    #     self.create_tab_widget()
    #     self.main_text = QtWidgets.QTextEdit(self)
    #     self.main_layout.addWidget(self.main_text)
    #     self.main_layout.addWidget(self.tab_widget)



        #self.podtabela1 = QtWidgets.QTableView(self.tab_widget)
        #self.podtabela2 = QtWidgets.QTableView(self.tab_widget)

    #     self.setLayout(self.main_layout)

    # def show_tabs(self):
    #     self.tab_widget.addTab(QtWidgets.QTextEdit(self.tab_widget), QtGui.QIcon("student.png"), "Prva podtabela")
    #     self.tab_widget.addTab(QtWidgets.QTextEdit(self.tab_widget), QtGui.QIcon("student.png"), "Druga podtabela")

    # def show_text(self, text):
    #     self.main_text.setText(text)

    # def student_selected(self, index):                          #kada se klikne na studenta u tabeli
    #     model = self.tabela1.model()
    #     selektovani_student = model.get_element(index)

    #     model_polozeni = PolozeniPredmetModel()                 #ovde treba da isntanciram polozeni predmeti model i nepolozeni predmeti model i setujem im podatke, tj. setujem im iz studenta odgovarajucu listu
    #     model_polozeni.polozeni_predmeti = selektovani_student.polozeni_predmeti        #onda posle podtabeli1 i podtabeli2 setujem model na ove modele koje sam instancirao i dodelio im odgovarajucu listu
    #     self.podtabela1.setModel(model_polozeni)

    #     model_nepolozeni = NepolozeniPredmetModel()
    #     model_nepolozeni.nepolozeni_predmeti = selektovani_student.nepolozeni_predmeti
    #     self.podtabela2.setModel(model_nepolozeni)

    #     self.tab_widget.addTab(self.podtabela1, QtGui.QIcon("icons8-edit-file-64"), "Prva podtabela")       #na kraju dodam da se nove tabele prikazu u novim tabovima
    #     self.tab_widget.addTab(self.podtabela2, QtGui.QIcon("icons8-edit-file-64"), "Druga podtabela")

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



# for child in model.children:                        #model iz generickog modela, iz json fajla
         #     for m in self.models:                           #ovaj miz models ima ucitano iz csv-a
         #         if child["name"] == m.name:

                    # parent = None
                    # for p in m.parents:
                    #     if p["name"] == model.name:
                    #         parent = p
                    #         break
                    #                                                             # napravimo medju-model (proxy) koji filtrira samo one redove koji zadovoljavaju neki uslov
                    # filter_proxy_model = QtCore.QSortFilterProxyModel()         # primer: "Nastavni predmeti" ispod tabele "Visokoskolska ustanova", prikazuje samo predmete iz selektovane ustanove
                    # filter_proxy_model.setSourceModel(m)                        # "child" model, iz kog modela vuce podatke, povezan je sa glavnim (generickim) modelom
                    # filter_proxy_model.setFilterKeyColumn(child["column"])      # u kojem modelu se nalazi oznaka "parent" modela
                    # filter_proxy_model.setFilterRegularExpression(selektovani_red[parent["column"]]) # u kojoj koloni u "parent" modelu se nalazi ta oznaka
                    #                                                             #proverava da li je oznaka ustanove (iz ustanove) jednaka ustanovi (iz nastavnog predmeta)
                    #                                                             # filtriranje