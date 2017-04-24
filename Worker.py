class Worker:

    def __init__(self, name, pay):  # inialize when created
        self.name = name  # self is the new object
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]  # split string on blanks

    def giveRaise(self, percent):
        self.pay *= (1. + (percent / 100))  # update pay in place

fabio = Worker('Fabio Reis', 5000)

print (fabio.lastName())
print (fabio.name)
fabio.giveRaise(10)
print(fabio.pay)