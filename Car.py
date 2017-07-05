class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        if(self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
    def display_all(self):
        print('Price: ' + str(self.price))
        print('Speed: ' + str(self.speed) + 'mph')
        print('Fuel: ' + 'Full')
        print('Mileage: ' + str(self.mileage) + 'mpg')
        print('Tax: ' + str(self.tax) + '\n')
        
nissan = Car(20000, 200, 'Full', 23)
nissan.display_all()
nissan = Car(9000, 189, 'Half Full', 13)
nissan.display_all()
nissan = Car(2000, 150, 'Almost Full', 20)
nissan.display_all()
nissan = Car(25000, 189, 'Half', 22)
nissan.display_all()
nissan = Car(30000, 250, 'Close To Empty', 33)
nissan.display_all()
nissan = Car(4000, 90, 'Full', 11)
nissan.display_all()