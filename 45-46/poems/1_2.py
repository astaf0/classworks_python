class Poems:
    def __init__(self):
        self.poems = []

    def add(self, author: str, name: str, year: int):
        if not self._find(author, name):
            poem = {'name': name, 'author': author, 'year': year}
            self.poems.append(poem)

    def _find(self, author, name):
        for poem in self.poems:
            if poem['name'] == name and poem['author'] == author:
                print('уже есть')
                return True
        return False

    def get_info(self):
        print(self.poems)







poems = Poems()
poems.add('Пушкин', 'Друзьям', 1816)
poems.add('Лермонтов', 'Весна', 1830)
poems.add('Пушкин', 'План', 1888)

poems.get_info()