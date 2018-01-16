from Sections import *


class Product:

    def __init__(self, barcode=0, name="", weight=1.0, cost=0.0, section=Sections.UNDEFINED, onsale=False):
        self.barcode = barcode
        self.name = name
        self.weight=weight
        self.cost = cost
        self.section = section
        self.onsale = onsale

    def setBarcode(self, barcode):
        if isinstance(barcode, int):
            self.barcode = barcode
        else:
            raise TypeError

    def setName(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError

    def setWeight(self, weight):
        if isinstance(weight, float):
            self.weight = weight
        else:
            raise TypeError

    def setCost(self, cost):
        if isinstance(cost, float):
            self.cost = cost
        else:
            raise TypeError

    def setOnsale(self, onsale):
        if isinstance(onsale, bool):
            self.onsale = onsale
        else:
            raise TypeError

    def getBarcode(self):
        return self.barcode

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getCost(self):
        return self.cost

    def getSection(self):
        return self.section

    def getOnsale(self):
        return self.onsale


class ProductKW(Product):
    def __init__(self, barcode, name, weight, cost, onsale):
        Product.__init__(self, barcode, name, weight, cost, Sections.KW, onsale)


class ProductVERS(Product):
    def __init__(self, barcode, name, weight, cost, section, onsale):
        if section in (Sections.GROENTE, Sections.VLEES, Sections.BROOD):
            Product.__init__(self, barcode, name, weight, cost, section, onsale)
        else:
            raise TypeError
