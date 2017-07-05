class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print('Health Of ' + self.name +  ': ' + str(self.health))
        return self

animal = Animal('Gasper', 100).display_health()
animal.walk().walk().walk().display_health()
animal.run().run().display_health()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        return self
        
dog = Dog('Frida')
dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
    def fly(self):
        self.health -= 10
    def display_health(self):
        super(Dragon, self).display_health()
        print('I am a Dragon')

dragon = Dragon('Ark')
dragon.display_health()

