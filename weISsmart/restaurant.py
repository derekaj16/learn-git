#Derek Johnson, David Murdock, Ella Nanto, Jared Bare

# Creating a class for Orders
# You are the owner of a very successful hamburger restaurant. Your faithful customers
# line up every day and eat dozens of burgers. You are writing a program to track exactly
# how many hamburgers each customer eats. 


import random
import math

class Order :
    burger_count = 0

    def randomBurgers(self) :
        return math.ceil(random.randint(1,20))

    def __init__(self) :
        self.burger_count = self.randomBurgers()


# Creating a class for Orders
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

    if newCustomer.customer_name in customerInfo :
        customerInfo[newCustomer.customer_name] += newCustomer.order.burger_count
    else :
        customerInfo[newCustomer.customer_name] = newCustomer.order.burger_count
        

listSortedCustomers = sorted(customerInfo.items(), key=lambda x: x[1], reverse=True)

for customer in listSortedCustomers :
    print(customer[0].ljust(19) + '\t' + str(customer[1]))


# for iCount in range(0, len(queueOfCustomers)) :
#     print(queueOfCustomers[iCount].customer_name)

