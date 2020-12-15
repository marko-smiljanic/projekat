import sys
from PySide2 import QtWidgets, QtGui, QtCore

from structure_dock import StructureDock
from workspace_widget import WorkspaceWidget
from genericki_model import GenerickiModel
import json


def delete_tab(index):
    central_widget.removeTab(index)

def open_file(index):
    path = dock_wgt.model.filePath(index)
    with open(path) as f:
        # TODO: proveriti da li postoji otvoren tab za ovaj fajl (da bi podaci bili azurni)
        #   - proci kroz tabove->workspace->model->source   #nisam nasao kako da iterisem kroz tabove, tj. kako da vidim koji su sve tabovi tu
        #       - ako postoji tab u kojem model.source == file_name: prebacimo fokus na njega
        #       - u suprotnom: kreiramo novi workspace i tab (kao ispod) i prebacimo fokus na njega
        #text = f.read()
        model = None  # izaberemo odgovarajuci model u zavisnosti od naziva file-a
        file_name = path.split("/")[-1]
        for m in models:                        #kako on ovde dohvati models kada je models definisano skroz dole?
            if m.source == file_name:
                model = m
                break
        if(model is not None):
            new_workspace = WorkspaceWidget(central_widget, model, models)
            central_widget.addTab(new_workspace, model.name)  #ovde setujemo ime novog taba, tj. splitujemo putanju i uzmemo poslednji element
            central_widget.setCurrentWidget(new_workspace)    #sa ovim smo promenili fokus na novootvoreni tab
        #new_workspace.show_text(text)
        #print(f.read())



if __name__ == "__main__":                                  #ako pokrecemo skruiptu izvrsice se telo, ako je importujemo nece je pokrenuti!!!
    app = QtWidgets.QApplication(sys.argv)                  #obavezan pocetak... pravljenje aplikacije i main prozora
    main_window = QtWidgets.QMainWindow()
    main_window.resize(1000, 700)                            #main prozor mora da se zatvori i izmedju se pise sav kod
    
    ###pocetak

    app.setWindowIcon(QtGui.QIcon("icons8-edit-file-64"))
    main_window.setWindowTitle("Editor generickih podataka")
    
    menu_bar = QtWidgets.QMenuBar(main_window)              #kao parent mora da se prosledi main_window!!!
    
    menu_file = QtWidgets.QMenu("File")                     #mogu da pravim posebne objekte tipa Menu, ili samo nad menu bar da pozovem ad menu i u parametru napravim novi meni
    menu_bar.addMenu(menu_file)
    menu_bar.addMenu(QtWidgets.QMenu("Edit", menu_bar))     #parent mu je menu_bar jer se nalazi u njemu !!
    menu_bar.addMenu(QtWidgets.QMenu("View", menu_bar))     #parent moze da se doda ali i ne mora, za ove jednostavne primere bar
    menu_bar.addMenu(QtWidgets.QMenu("Help", menu_bar))
    main_window.setMenuBar(menu_bar)                        #uglavnom sve sto se dodaje moramo dodati u main window, tj da mu setujemo sta smo dodali
    
    tool_bar = QtWidgets.QToolBar("Tool bar dodat.", main_window)   #klasika...napravimo tool bar i setujemo ga u main_window
    main_window.addToolBar(tool_bar)

    # text_editor_wgt = QtWidgets.QTextEdit("Unesite tekst", main_window)
    # main_window.setCentralWidget(text_editor_wgt)

    status_bar = QtWidgets.QStatusBar(main_window)
    status_bar.showMessage("Status bar prikazan.")
    main_window.setStatusBar(status_bar)
    
    # dock_wgt = QtWidgets.QDockWidget("Dock!!!", main_window)
    # main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock_wgt)   #mora se importovati QtCOre!!!
    
    # obican_wgt = QtWidgets.QWidget(main_window)                         #napravimo obican (genericki) widget, setujemo layout i na kraju ga postavimo za centralni
    # layout = QtWidgets.QVBoxLayout()                                    #u konstruktru se odredjuje jel horizontalan ili vertikalan, u ovom slucaju H-horizontalan ili V-vertikalan
    # text_edit_wgt1 = QtWidgets.QTextEdit("Unesite tekst", main_window)
    # text_edit_wgt2 = QtWidgets.QTextEdit("Unesite tekst", main_window)
    # layout.addWidget(text_edit_wgt1)
    # layout.addWidget(text_edit_wgt2)
    # obican_wgt.setLayout(layout)                                        #obican widget, jer nije nam bitno koji je u ovom slucaju jer svaki moze da ima layout
    # main_window.setCentralWidget(obican_wgt)

    dock_wgt = StructureDock("Structure Dock", main_window)
    dock_wgt.tree.clicked.connect(open_file)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock_wgt)

    ###ucitavamo metadata
    metadata_file = open("metadata.json", encoding='utf-8')  #ENCODING se dodaje u citanju json-a jer nema podeseno po default-u UTF-8
    metadata = json.load(metadata_file)
    models = []
    for data in metadata:
        models.append(GenerickiModel(data))

    central_widget = QtWidgets.QTabWidget(main_window)
    workspace = WorkspaceWidget(central_widget, None, models)
    # workspace.show_tabs()
    central_widget.addTab(workspace, QtGui.QIcon("student.png"), "Naslov")
    central_widget.setTabsClosable(True)
    central_widget.tabCloseRequested.connect(delete_tab)
  
    main_window.setCentralWidget(central_widget)
    
    ###kraj

    main_window.show()
    sys.exit(app.exec_())
