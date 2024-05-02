# Doplňte třídu Car o možnost zabalit a rozbalit data pomocí json a pickle.
import pickle
import json

class Car():
    def __init__(self, znacka, model, rok):
        self.znacka = znacka
        self.model = model
        self.rok = rok

    def zobraz(self):
        print(f'Značka auta je: {self.znacka}')
        print(f'Model auta je: {self.model}')
        print(f'Rok výroby auta je: {self.rok}')


    def to_json(self):
        return json.dumps({
            'znacka': self.znacka,
            'model': self.model,
            'rok': self.rok
        })

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_json(cls,json_data):
        data = json.loads(json_data)
        return cls(data['znacka'] ,data['model'], data['rok'])

    @classmethod
    def from_pickle(cls,pickle_data):
        return pickle.loads(pickle_data)

my_car = Car('Škoda', 'Octavia2rs', 2013)
show_car = Car.zobraz(my_car)


def main():
    while True:
        print('\nMenu:')
        print('1. Serializace do JSON')
        print('2. Serializace do Pickle')
        print('3. Deserializace z JSON')
        print('4. Deserializace z Pickle')
        print('5. Ukončení programu')

        volba = input('Zvolte číslo operace: ')

        if volba == '1':
            car_json = my_car.to_json()
            print(f'Serializované auto (JSON): {car_json}')

        elif volba == '2':
            car_pickle = my_car.to_pickle()
            print(f'Serializované auto (Pickle): {car_pickle}')

        elif volba == '3':
            load_car_json = Car.from_json(car_json)
            print(f'Deserializované auto (z JSON): {load_car_json.znacka} {load_car_json.model} ({load_car_json.rok})')

        elif volba == '4':
            load_car_pickle = Car.from_pickle(car_pickle)
            print(
                f'Deserializované auto (z Pickle): {load_car_pickle.znacka} {load_car_pickle.model} ({load_car_pickle.rok})')

        elif volba == '5':
            print('Konec programu.')
            break

        else:
            print('Neplatná volba! Zadej číslo v rozmezí (1-5).')

if __name__ == '__main__':
    main()


