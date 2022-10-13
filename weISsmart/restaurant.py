# Derek Johnson, David Murdock, Ella Nanto, Jared Bare
# IS403 - Section 003
# This program adds customers to a line and randomly gives them a 
# certain number of burgers. We then aggregate their orders and 
# give a summary at the end of the program

import random
import math

# Declaring classes
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
    def __init__(self) :
        super().__init__()
        self.order = Order()


# Initialize variables
queueOfCustomers = list()
customerInfo = dict()

# Begin program. Adding customers to the line and getting their info
for iCount in range(0,100) :
    queueOfCustomers.append(Customer())

for customer in queueOfCustomers :
    if customer.customer_name in customerInfo :
        customerInfo[customer.customer_name] += customer.order.burger_count
    else :
        customerInfo[customer.customer_name] = customer.order.burger_count
        
# Sorting the customer info we obtained
listSortedCustomers = sorted(customerInfo.items(), key=lambda x: x[1], reverse=True)

# Print results
for customer in listSortedCustomers :
    print(customer[0].ljust(19) + '\t' + str(customer[1]))