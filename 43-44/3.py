class Programmer():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.all_time = 0
        self.all_income = 0
        self.extra_income = 0

        self.salary = {'junior': 10, 'middle': 15, 'senior': 20}

    def work(self, time):
        self.all_time += time
        current_salary = self.salary[self.grade]
        income = (current_salary + self.extra_income) * time
        self.all_income += income

    def info(self):
        print(f'{self.name}, {self.all_time}ч., {self.all_income}тгр.')

    def rise(self):
        if self.grade == 'junior':
            self.grade = 'middle'
        elif self.grade == 'middle':
            self.grade = 'senior'
        else:
            self.extra_income += 1


prog = Programmer('Антон', 'junior')
prog.work(10)
prog.info()

prog.rise()
prog.work(10)
prog.info()

prog.rise()
prog.work(10)
prog.info()

prog.rise()
prog.work(10)
prog.info()
