class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price 
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print('Price of bike: $' + str(self.price) + ' Max speed of bike: ' + self.max_speed + ' Total miles on bike: ' + str(self.miles)) 
    def ride(self):
        print('Riding')
        self.miles += 10
    def reverse(self):
        print('Reversing')
        if(self.miles == 0):
            print('There are no miles on the bike!')
        else:
            self.miles -= 5



bike1 = Bike(200, '25mph')    
bike2 = Bike(300, '34mph')
bike3 = Bike(400, '67mph')

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()