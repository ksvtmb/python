class Class1(object):
    @staticmethod
    def sum1(x, y):              
# Статический метод
        return x + y
    def sum2(self, x, y):        
# Обычный метод в классе
        return x + y
    def sum3(self, x, y):
        return Class1.sum1(x, y) 
# Вызов из метода класса
 
a=Class1()
print (Class1.sum1(10, 20))

# c1 = Class1()
# print (c1.sum2(15, 6))        
