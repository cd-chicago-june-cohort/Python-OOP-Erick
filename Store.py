class Store(object):
    def __init__(self, arr, location, owner):
        self.arrOfProducts = arr
        self.location = location
        self.owner = owner
    def add_product(self, product):
        self.arrOfProducts.append(product)
        return self
    def remove_product(self, product):
        for i in self.arrOfProducts:
            if(i == product):
                self.arrOfProducts.remove(i)
        return self
    def show_inventory(self):
        print('List of products in ' + self.owner + "'s " + self.location + ' store:')
        for i in self.arrOfProducts:
            print(' - ' + i )
        return self

items = ['Shovel', 'Table', 'Desk']
hardware = Store(items, 'Chicago', 'Erick')

hardware.add_product('Stool').show_inventory()

hardware.remove_product('Stool').show_inventory()

food = ['pasta', 'apple', 'orange', 'chicken', 'pizza']
foodStore = Store(food, 'Food Market', 'Erick').show_inventory()

foodStore.add_product('turkey').show_inventory()

foodStore.remove_product('orange').show_inventory()

