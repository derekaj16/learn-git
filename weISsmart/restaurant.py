import random
import math

class Order :
    burger_count = 0

    def randomBurgers(self) :
        return math.ceil(random.randint(1,20))

    def __init__(self) :
        self.burger_count = self.randomBurgers()

class Person :
    customer_name = ''

    def randomName(self) :
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return asCustomers[math.floor(random.randint(0,8))]
    
    def __init__(self) :
        self.customer_name = self.randomName()

class Customer(Person) :
    order = 0
    def __init__(self) :
        super().__init__()
        self.order = Order()



queueOfCustomers = list()
customerInfo = dict()

for iCount in range(0,100) :
    newCustomer = Customer()
    additionalBurgers = newCustomer.order.burger_count
    queueOfCustomers.append(newCustomer)
    customerInfo[newCustomer.customer_name] += additionalBurgers

listSortedCustomers = sorted(customerInfo.items(), key=lambda x: x[1], reverse=True)


