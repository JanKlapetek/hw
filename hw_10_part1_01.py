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

def main():
    muj_seznam = Seznam_cisel()
    while True:
        print('\nNabídka:')
        print('1. Přidat nové číslo do seznamu.')
        print('2. Odstranit číslo ze seznamu.')
        print('3. Zobrazit obsah seznamu.')
        print('4. Uložit seznam do souboru.')
        print('5. Načíst seznam ze souboru.')
        volba = input('Zadejte číslo akce (1-5) nebo (end) pro ukončení programu: ')

        if volba == '1':
            cislo = int(input('Zadejte číslo, které chcete přidat do seznamu: '))
            muj_seznam.pridat_cislo(cislo)

        elif volba == '2':
            cislo = int(input('Zadejte číslo, které chcete odstranit ze seznamu: '))
            muj_seznam.odstranit_cislo(cislo)

        elif volba == '3':
            volba2 = input('Napiš (vzestupne) nebo (sestupne): ')
            if volba2 == 'sestupne':
                muj_seznam.zobrazit_obsah(sestupne=True)
            elif volba2 == 'vzestupne':
                muj_seznam.zobrazit_obsah()
            else:
                print('Neplatná volba. Zadejte (vzestupne) nebo (sestupne).')

        elif volba == '4':
            soubor = input('Zadejte název souboru pro uložení seznamu: ')
            muj_seznam.ulozit_do_souboru(soubor)

        elif volba == '5':
            soubor = input('Zadejte název souboru pro načtení seznamu: ')
            muj_seznam.nacist_ze_souboru(soubor)

        elif volba.lower() == 'end':
            break

        else:
            print('Neplatná volba. Zadejte číslo od 1 do 5 nebo napište end.')

if __name__ == '__main__':
    main()