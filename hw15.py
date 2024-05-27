import pytest

class MnozinaCisel:
    def __init__(self):
        self.prvky = set()

    def pridat(self, cislo):
        """Přidá celé číslo do množiny."""
        self.prvky.add(cislo)

    def soucet(self):
        """Spočítá součet prvků v množině."""
        return sum(self.prvky)

    def prumer(self):
        """Spočítá aritmetický průměr prvků v množině."""
        if not self.prvky:
            return 0
        return sum(self.prvky) / len(self.prvky)

    def maximum(self):
        """Najde největší hodnotu v množině."""
        if not self.prvky:
            return None
        return max(self.prvky)

    def minimum(self):
        """Najde nejmenší hodnotu v množině."""
        if not self.prvky:
            return None
        return min(self.prvky)

# Příklad použití:
moje_mnozina = MnozinaCisel()
moje_mnozina.pridat(20)
moje_mnozina.pridat(40)
moje_mnozina.pridat(60)
moje_mnozina.pridat(80)
moje_mnozina.pridat(100)

print(f"Součet: {moje_mnozina.soucet()}")
print(f"Průměr: {moje_mnozina.prumer()}")
print(f"Největší: {moje_mnozina.maximum()}")
print(f"Nejmenší: {moje_mnozina.minimum()}")
