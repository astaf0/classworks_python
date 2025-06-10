from flask import Flask, render_template_string, render_template

app = Flask(__name__)

todo = ['Погулять', 'Посмотреть фильм', 'Выучить джаваскрипт']
todo = [
    {'name': 'Погулять', 'status': 'Не выполнено'},
    {'name': 'Посмотреть фильм', 'status': 'Не выполнено'}
]

countries_data = [
    {'name': 'Россия', 'capital': 'Москва', 'population': 12000000},
    {'name': 'Китай', 'capital': 'Пекин', 'population': 23000000},
]


@app.route('/')
def index():
    return render_template('index.html', data=todo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/countries')
def countries():
    return render_template('countries.html', countries=countries_data)

@app.route('/countries/<int:country_index>')
def countries_detail(country_index):
    country = countries_data[country_index]
    return render_template('countries_detail.html', country=country)

# @app.route('/countries/china')
# def countries_detail2():
#     country = countries_data[1]
#     return render_template('countries_detail.html', country=country)

app.run(debug=True)