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

    def odstranit_cislo(self, cislo):
        if cislo in self.seznam:
            self.seznam.remove(cislo)
            print(f'Číslo {cislo} bylo odstraněno ze seznamu.')
        else:
            print(f'Číslo {cislo} není v seznamu.')

    def zobrazit_obsah(self, sestupne=False):
        if self.seznam:
            print('Obsah seznamu:')
            sorted_seznam = sorted(self.seznam, reverse=sestupne)
            for cislo in sorted_seznam:
                print(cislo)
        else:
            print('Seznam je prázdný.')
