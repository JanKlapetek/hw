import pytest
from hw15 import MnozinaCisel

@pytest.fixture
def mnozina():
    return MnozinaCisel()
def test_soucet(mnozina):
    mnozina.pridat(1)
    mnozina.pridat(2)
    assert mnozina.soucet() == 3

def test_prumer(mnozina):
    mnozina.pridat(2)
    mnozina.pridat(4)
    assert mnozina.prumer() == 3

def test_maximum(mnozina):
    mnozina.pridat(2)
    mnozina.pridat(50)
    mnozina.pridat(99)
    mnozina.pridat(-99)
    assert mnozina.maximum() == 99

def test_minimum(mnozina):
    mnozina.pridat(50)
    mnozina.pridat(9)
    mnozina.pridat(7)
    assert mnozina.minimum() == 7


if __name__ == '__main__':
    pytest.main()