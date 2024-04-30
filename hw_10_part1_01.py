import pickle
class Seznam_cisel:
    def __init__(self):
        self.seznam = []

    def pridat_cislo(self, cislo):
        if cislo not in self.seznam:
            self.seznam.append(cislo)
            print(f'Číslo {cislo} bylo přidáno do seznamu.')
        else:
            print(f'Číslo {cislo} již v seznamu existuje.')

