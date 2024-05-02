# Existuje slovník, ve kterém jsou uloženy názvy zemí a jejich hlavní města. Jako klíč se používá název země, jako hodnota hlavní město.
# Implementujte následující funkce: přidávání dat, mazání dat, vyhledávání dat, úpravy dat, ukládání a načítání dat (pomocí zabalení a rozbalení).

import json

class Capitals:
    def __init__(self):
        self.slovnik = {}

    def pridej_mesto(self, stat, mesto):
        """
        Přidá město do slovníku pod daný stát.
        """
        if stat in self.slovnik:
            self.slovnik[stat].append(mesto)
        else:
            self.slovnik[stat] = [mesto]

    def vypis_slovnik(self):
        """
        Vypíše obsah slovníku.
        """
        for stat, mesta in self.slovnik.items():
            print(stat, mesta)

# Příklad použití
slovnik_mest = Capitals()
slovnik_mest.pridej_mesto('Czech', 'Prague')
slovnik_mest.pridej_mesto('France', 'Paris')
slovnik_mest.pridej_mesto('Germany', 'Berlin')
slovnik_mest.pridej_mesto('Italy', 'Rome')

slovnik_mest.vypis_slovnik()
