import random
import math

class Order :
    burger_count = 0

    def randomBurgers(self) :
        return math.ceil(random.randint(1,20))

    def __init__(self) :
        self.burger_count = self.randomBurgers()
print('hello')
class Person :
    customer_name = ''

    def randomName() :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return asCustomers[math.floor(random.randint(0,8))]
    
    def __init__(self) :
        self.customer_name = self.randomName()

class Customer(Person) :
    order = Order()

    def __init__(self) :
        super().__init__()



queue = list()
dictionary = dict()

for iCount in range(0,100) :
    queue.append(Customer())

