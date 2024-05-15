class Boty:
    def __init__(self, typ, barva, cena, znacka, velikost):
        self.typ = typ
        self.barva = barva
        self.cena = cena
        self.znacka = znacka
        self.velikost = velikost

class ShoesView:
    @staticmethod
    def zobraz_botu(bota):
        print(f'Typ: {bota.typ}')
        print(f'Barva: {bota.barva}')
        print(f'Cena: {bota.cena:.2f} Kč')
        print(f'Značka: {bota.znacka}')
        print(f'Velikost: {bota.velikost}\n')

class ShoesController:
    def __init__(self, bota):
        self.bota = bota

    def aktualizuj_cenu_barvu(self, nova_cena, nova_barva):
        print('Změna ceny a barvy:')
        self.bota.barva = nova_barva
        self.bota.cena = nova_cena


if __name__ == '__main__':
    moje_bota = Boty('Tenisky', 'Bílá', 2900, 'Puma', 38)
    moje_bota2 = Boty('Tenisky', 'Černá', 2300, 'Nike', 43)

    view = ShoesView()
    view.zobraz_botu(moje_bota)
    view.zobraz_botu(moje_bota2)

    #aktualizace ceny a barvy
    controller = ShoesController(moje_bota2)
    controller.aktualizuj_cenu_barvu(1200,'Modrá')
    view.zobraz_botu(moje_bota2)
