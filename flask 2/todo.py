from flask import Flask, render_template_string, render_template, request, redirect

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

@app.route('/countries/<string:country_name>')
def countries_detail(country_name):
    for country in countries_data:
        if country['name'] == country_name:
            return render_template('countries_detail.html', country=country)
    return 'такой страницы нет'


@app.route('/countries/add', methods=['POST'])
def countries_add():
    countries_data.append(request.form)
    return redirect('/countries')

app.run(debug=True)