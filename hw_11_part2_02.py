# Doplňte třídu Kniha o možnost zabalit a rozbalit data pomocí json a pickle.
import pickle
import json

class Book():
    def __init__(self, nazev, autor, rok):
        self.nazev = nazev
        self.autor = autor
        self.rok = rok

    def zobraz(self):
        print(f'Název knihy je: {self.nazev}')
        print(f'Autor knihy je: {self.autor}')
        print(f'Rok vydání knihy je: {self.rok}')

    def to_json(self):
        return json.dumps({
            'nazev': self.nazev,
            'autor': self.autor,
            'rok': self.rok
        })

    def to_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def from_json(cls,json_data):
        data = json.loads(json_data)
        return cls(data['nazev'] ,data['autor'], data['rok'])

    @classmethod
    def from_pickle(cls,pickle_data):
        return pickle.loads(pickle_data)

my_book = Book('Steve Jobs', 'Walter Isaacson', 2000)
show_book = Book.zobraz(my_book)


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
            book_json = my_book.to_json()
            print(f'Serializovaná kniha (JSON): {book_json}')

        elif volba == '2':
            book_pickle = my_book.to_pickle()
            print(f'Serializovaná kniha (Pickle): {book_pickle}')

        elif volba == '3':
            load_book_json = Book.from_json(book_json)
            print(f'Deserializovaná kniha (z JSON): {load_book_json.nazev} {load_book_json.autor} ({load_book_json.rok})')

        elif volba == '4':
            load_book_pickle = Book.from_pickle(book_pickle)
            print(
                f'Deserializovaná kniha (z Pickle): {load_book_pickle.nazev} {load_book_pickle.autor} ({load_book_pickle.rok})')

        elif volba == '5':
            print('Konec programu.')
            break

        else:
            print('Neplatná volba! Zadej číslo v rozmezí (1-5).')

if __name__ == '__main__':
    main()