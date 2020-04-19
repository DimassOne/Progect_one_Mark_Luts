class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


if __name__ == '__main__':
    bob = Person('Bobbi')
    jim = Person('Jimmi','Svarnoy',45000)
    print(bob.name, bob.job, bob.pay)
    print(jim.name, jim.job, jim.pay)
    jim.pay *=1.3
    print('%.3f' % jim.pay)





