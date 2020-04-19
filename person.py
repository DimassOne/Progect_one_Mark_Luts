class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay*(1+percent))
    def __repr__(self):
        return f"[Person: {self.name}, Зарплата: {self.pay}]"#'[Person: %s, %s]' % (self.name, self.pay)


if __name__ == '__main__':
    bob = Person('Dmitrii Rogonian')
    sue = Person('Vlad Rogonian','Svarnoy',45000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)





