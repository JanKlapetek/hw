'''
Task1
# Aplikace po spuštění spustí tři vlákna. První vlákno vyplní seznam náhodnými čísly. Další dvě vlákna čekají.
# Jakmile je seznam naplněn, spustí se obě vlákna. První vlákno zjistí součet prvků seznamu, druhé vlákno zjistí průměr v tomto seznamu.
# Obdržený seznam, součet a průměr se zobrazí na obrazovce.
'''
import random
import threading

class ZpracovaniSeznamuCisel:
    def __init__(self, pocet_prvku):
        self.pocet_prvku = pocet_prvku
        self.seznam_cisel = []
        self.soucet_vysledek = None
        self.prumer_vysledek = None

    def napln_seznam(self):
        self.seznam_cisel = [random.randrange(0,1000) for _ in range(self.pocet_prvku)]

    def spocitej_soucet(self):
        self.soucet_vysledek = sum(self.seznam_cisel)

    def spocitej_prumer(self):
        self.prumer_vysledek = sum(self.seznam_cisel) / self.pocet_prvku

    def spust_vlakna(self):
        vlakno_naplneni = threading.Thread(target=self.napln_seznam)
        vlakno_soucet = threading.Thread(target=self.spocitej_soucet)
        vlakno_prumer = threading.Thread(target=self.spocitej_prumer)

        vlakno_naplneni.start()
        vlakno_naplneni.join()

        vlakno_soucet.start()
        vlakno_prumer.start()

        vlakno_soucet.join()
        vlakno_prumer.join()

    def zobraz_vysledky(self):
        print(f'Vygenerovaný seznam {self.pocet_prvku} náhodných čísel: {self.seznam_cisel}')
        print(f'Součet prvků seznamu: {self.soucet_vysledek}')
        print(f'Průměr prvků seznamu: {self.prumer_vysledek:.3f}')


if __name__ == '__main__':
    pocet_prvku = 50
    zpracovani = ZpracovaniSeznamuCisel(pocet_prvku)
    zpracovani.spust_vlakna()
    zpracovani.zobraz_vysledky()