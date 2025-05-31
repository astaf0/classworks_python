import json

class Calc:
    def __init__(self, logger):
        self.logger = logger

    def add(self, number1, number2):
        res = number1 + number2
        self.logger.log(number1, number2, res, 'Сумма')
        return res


class Logger:

    def log(self, number1, number2, res, operation):
        with open('logs.txt', 'a', encoding='utf-8') as f:
            f.write(self._format_string(number1, number2, res, operation))

    def _format_string(self, number1, number2, res, operation):
        return f'{operation} - {number1, number2} Результат: {res}\n'


class JsonLogger(Logger):
    def log(self, number1, number2, res, operation):
        with open('logs.json', 'a', encoding='utf-8') as f:
            json.dump(self._format_string(number1, number2, res, operation), f)


logger = JsonLogger()
calc = Calc(logger)
print(calc.add(9, 12))