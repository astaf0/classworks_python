countries_data = [
    {'name': 'Россия', 'capital': 'Москва', 'population': 12000000},
    {'name': 'Китай', 'capital': 'Пекин', 'population': 23000000},
]

counter = 0
for country in countries_data:
    print(f'/countries/{counter} {country['name']}')
    counter += 1