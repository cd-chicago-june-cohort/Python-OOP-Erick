from types import *

class MathDojo(object):
    def __init__(self):
        self.total = 0
    def add(self, *nums):
        for i in nums:
            self.total += i
        return self
    def subtract(self, *nums):
        for i in nums:
            self.total -= i
        return self
    def result(self):
        print self.total

math1 = MathDojo().add(2).add(2, 5).subtract(3, 2).result()