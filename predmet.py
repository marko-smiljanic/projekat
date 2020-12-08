from abc import ABC, abstractmethod   #nemam gde da koristim

class Predmet():
    def __init__(self, naziv, silabus=""):
        self.naziv = naziv
        self.silabus = silabus
