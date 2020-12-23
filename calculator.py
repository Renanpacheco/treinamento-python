# calculator class with the values passed in the instantiation of the class
'''
class Calculator:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def sum(self):
        return self.x + self.y
    
    def subtration(self):
        return self.x - self.y
    
    def multiplication(self):
        return self.x * self.y
    
    def division(self):
        return self.x / self.y

result=Calculator(10,2)
print(result.y)
print(result.sum())
print(result.subtration())
print(result.multiplication())
print(result.division())
'''

# calculator class with the values passed in the function call

class Calculator:
    '''
    def __init__(self):
        pass
    '''
    def sum(self, x, y):
        return x + y
    
    def subtration(self, x, y):
        return x - y
    
    def multiplication(self, x, y):
        return x * y
    
    def division(self, x, y):
        return x / y

result=Calculator()
print(result.sum(5,2))
print(result.subtration(3,3))
print(result.multiplication(5,5))
print(result.division(5,2))
