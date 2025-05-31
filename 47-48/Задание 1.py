import datetime
from datetime import datetime

class Model:
    def add_task(self, task_name, price):
        buys = []
        current_datetime = datetime.now()
        with open('task.txt', 'a', encoding='utf-8') as f:
            buys.append(task_name)
            buys.append(price)
            buys.append(str(current_datetime))
            f.write(f'{buys[0]} - {buys[1]} - руб. - {buys[2]}\n')
            print('Покупка добавлена')
    def get_tasks(self):
            return self.load_from_file()

    def load_from_file(self):
        with open('task.txt', 'r', encoding='utf-8') as f:
            tasks = f.readlines()
            return tasks

    def show_tasks(self, tasks):
        self.view.show_tasks(tasks)

    def all_buys(self, n):
        with open('task.txt', 'r', encoding='utf-8') as inp:
            res = [i.strip().split('-') for i in inp.readlines()]
            print(res)
            def sort_col_int(i):
                return int(i[n])
            def sort_col(i):
                return i[n]
            if n == 0:
                res.sort(key=sort_col)
                count = 0
                for i in res:
                    count += 1
                    if count <= 5:
                        print(f"{count}. {i[n]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")

            if n == 1:
                res.sort(key=sort_col_int, reverse=True)
                count = 0
                for i in res:
                    count += 1
                    if count <= 5:
                        print(f"{count}. {i[0]} - {i[n]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")


class View:
    def show_tasks(self, tasks):
        for index, task in enumerate(tasks, start=1):
            print(index, task)


class Controller:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

    def add_task(self, task_name, price):
        print(task_name)
        self.model.add_task(task_name, price)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)

    def load_from_file(self):
        self.model.load_from_file()

    def get_tasks(self):
        self.model.get_tasks()

    def all_buys(self, n):
        self.model.all_buys(n)


model = Model()
view = View()
cont = Controller(model, view)

while True:
    print('1.Добавить покупку\n2.Показать все покупки\n3.Показать 5 самых дорогих покупок\n4.Выход')
    answer = input('Выбери действие: ')
    if answer == '1':
        task = input('Введи название товара: ')
        price = input('Введи стоимость товара: ')
        cont.add_task(task, price)
    elif answer == '2':
        cont.show_tasks()
    elif answer == '3':
        n = input('Сортировать по названию (1),По стоимости (2)')
        n = int(n) - 1
        cont.all_buys(n)
    elif answer == '4':
        break
