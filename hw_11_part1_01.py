import json

class Capitals:
    def __init__(self):
        self.slovnik = {}

    def pridej_mesto(self, stat, mesto):
        if stat in self.slovnik:
            self.slovnik[stat].append(mesto)
            print(f'Město {mesto} bylo přidáno do slovníku.')
        else:
            self.slovnik[stat] = [mesto]
            print(f'Stát {stat} a město {mesto} byly přidány do slovníku.')

    def odstran_mesto(self, stat, mesto):
        if stat in self.slovnik and mesto in self.slovnik[stat]:
            self.slovnik[stat].remove(mesto)
            if not self.slovnik[stat]:
                del self.slovnik[stat]  # Odstranění položky státu, pokud nejsou žádná města

    def najdi_mesta(self, stat):
        return self.slovnik.get(stat, [])

    def uprav_mesto(self, stat, stare_mesto, nove_mesto):
        if stat in self.slovnik and stare_mesto in self.slovnik[stat]:
            index = self.slovnik[stat].index(stare_mesto)
            self.slovnik[stat][index] = nove_mesto

    def uloz_do_souboru(self, soubor):
        with open(soubor, 'w') as f:
            json.dump(self.slovnik, f)

    def nacti_z_souboru(self, soubor):
        try:
            with open(soubor, 'r') as f:
                self.slovnik = json.load(f)
        except FileNotFoundError:
            print('Soubor neexistuje.')

    def zobraz(self):
        print('\nSlovník států a měst:')
        for stat, mesta in self.slovnik.items():
            print(f"{stat}: {', '.join(mesta)}")

def main():
    mesta = Capitals()

    while True:
        print('\nMenu:')
        print('1. Přidat město')
        print('2. Odstranit město')
        print('3. Vyhledat města')
        print('4. Upravit město')
        print('5. Uložit data do souboru')
        print('6. Načíst data ze souboru')
        print('7. Zobraz státy a města')
        print('8. Konec')

        volba = input('Zvolte číslo operace: ')

        if volba == '1':
            stat = input('Zadejte název státu: ')
            mesto = input('Zadejte název města: ')
            mesta.pridej_mesto(stat, mesto)
        elif volba == '2':
            stat = input('Zadejte název státu: ')
            mesto = input('Zadejte název města k odstranění: ')
            mesta.odstran_mesto(stat, mesto)
        elif volba == '3':
            stat = input('Zadejte název státu: ')
            print(f"Hlavní město {stat} je: {', '.join(mesta.najdi_mesta(stat))}")
        elif volba == '4':
            stat = input('Zadejte název státu: ')
            stare_mesto = input('Zadejte stávající název města: ')
            nove_mesto = input('Zadejte nový název města: ')
            mesta.uprav_mesto(stat, stare_mesto, nove_mesto)
        elif volba == '5':
            soubor = input('Zadejte název souboru pro uložení: ')
            mesta.uloz_do_souboru(soubor)
            print(f'Data byla uložena do souboru {soubor}')
        elif volba == '6':
            soubor = input('Zadejte název souboru pro načtení: ')
            mesta.nacti_z_souboru(soubor)
            print(f'Načtená data: {mesta.slovnik}')
        elif volba == '7':
            mesta.zobraz()
        elif volba == '8':
            break
        else:
            print('Neplatná volba. Zvolte číslo od 1 do 8.')


if __name__ == '__main__':
    main()
