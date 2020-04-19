ЗАКОНЧИЛ КНИГУ НА 71 СТРАНИЦЕ
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
    
class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def gitveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent+bonus)

if __name__ == '__main__':
    bob = Person('Dmitrii Rogonian')
    sue = Person('Vlad Rogonian','Svarnoy',45000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones',50000)
    tom.gitveRaise(.10)
    print(tom.lastName())
    print(tom)
    print('--Полное дерево--')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)





