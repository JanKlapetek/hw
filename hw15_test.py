import pytest
from hw15 import MnozinaCisel

@pytest.fixture
def mnozina():
    return MnozinaCisel()





if __name__ == '__main__':
    pytest.main()