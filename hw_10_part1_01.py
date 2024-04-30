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

    def ulozit_do_souboru(self, soubor):
        with open(soubor, 'wb') as f:
            pickle.dump(self.seznam, f)
            print(f'Seznam byl uložen do souboru {soubor}.')

    def nacist_ze_souboru(self, soubor):
        try:
            with open(soubor, 'rb') as f:
                self.seznam = pickle.load(f)
                print(f'Seznam byl načten ze souboru {soubor}.')
        except FileNotFoundError:
            print(f'Soubor {soubor} neexistuje.')

