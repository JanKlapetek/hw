# Existuje slovník, ve kterém jsou uloženy názvy zemí a jejich hlavní města. Jako klíč se používá název země, jako hodnota hlavní město.
# Implementujte následující funkce: přidávání dat, mazání dat, vyhledávání dat, úpravy dat, ukládání a načítání dat (pomocí zabalení a rozbalení).

import json
capitals = {
    'Italy': 'Rome',
    'France': 'Paris',
    'Czech': 'Prague'
}
serialized = json.dumps(capitals)
print(serialized)

deserialized = json.loads(serialized)
print(deserialized)