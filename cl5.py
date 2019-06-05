# cl5. private attribite

class Pri(object):
    
    pub=1;
    __nepub=2;
    
    def h1(self):
        return 10;
        
    def __h2(self):
        return 20;
        
    def h3(self):
        
        return self.__h2()+self.__nepub;
        
    def __private_method(self):
        print("это закрытый метод");
        
    def public_method(self):
        print ("Это публичный метод");
        self.__private_method()
        
        

class A1(object):
    a=1;

    def am(self,b):
        self.a=b;
    
b=A1();
print (b.a)
b.a=10;
print (b.a)

b.am(100)
print (b.a)
        
#main theme

# a=Pri();

# a.public_method();

