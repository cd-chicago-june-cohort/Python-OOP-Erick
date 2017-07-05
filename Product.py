class Product(object):
    def __init__(self, Price, Item_Name, Weight, Brand):
        self.Price = Price
        self.Item_Name = Item_Name
        self.Weight = Weight
        self.Brand = Brand
        self.Status = 'For Sale'
    def sell(self):
        self.Status = 'Sold'
        return self
    def addTax(self, Tax):
        self.Price = self.Price + (self.Price * Tax)
        return self
    def Return(self, reason):
        if(reason == 'Defective'):
            self.Status = 'Defective'
            self.Price = 0
        elif(reason == 'No use'):
            self.Status = 'For Sale'
        elif(reason == 'Opened'):
            self.Status = 'Used'
            self.Price = self.Price - (self.Price * 0.20)
        return self
    def displayInfo(self):
        print('Product Details')
        print('Item Name: ' + self.Item_Name)
        print('Price: $' + str(self.Price))
        print('Brand: ' + self.Brand)
        print('Weight: ' + str(self.Weight) + 'lbs')
        print('Status: ' + self.Status + '\n')

radio = Product(200, 'SONO', 20, 'Sony')
radio.addTax(0.09).sell().displayInfo()
radio.Return('Defective').displayInfo()
