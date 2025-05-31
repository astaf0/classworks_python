# Напишите класс Shop. Он должен содержать методы: -
# buy() - купить продукт, если он есть в базе данных - -
# add_product() - добавить продукт в базу данных
# get_info() - узнать итоговую сумму покупок и количество чеков
# В виде базы данных может быть обычный словарь вида {“Название
# товара”: Цена}
# Дефолтные цены: {'Молоко': 10, 'Колбаса': 20}

class Shop:
    def __init__(self):
        self.data =  {'Молоко': 10, 'Колбаса': 20}

    def buy(self, product):
        if product in self.data:
            print(f'{product} куплен')
        else:
            print('продукта нет в базе')

    def add_product(self):
        pass

    def get_info(self):
        pass





s = Shop()
s.buy('молоко')
s.buy('яйца')
s.buy('колбаса')
# s.add_product('яйца', 100)
# s.buy('яйца')
# s.get_info()