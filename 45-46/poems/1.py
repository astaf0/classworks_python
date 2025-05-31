class Poems:
    def __init__(self):
        self.poems = []

    def add(self, author: str, name: str, year: int):

        find = False
        for poem in self.poems:
            if poem['name'] == name and poem['author'] == author:
                find = True
                print('уже есть')
                break

        poem = {'name': name, 'author': author, 'year': year}
        if not find:
            self.poems.append(poem)

    def get_info(self):
        print(self.poems)



poems = Poems()
poems.add('Пушкин', 'Друзьям', 1816)
poems.add('Лермонтов', 'Весна', 1830)
poems.add('Пушкин', 'План', 1888)

poems.get_info()