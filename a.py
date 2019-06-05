# property

class A(object):
    
    def __init__(self,var):
        self.__var=var;
        print ("переменой __var присвоено значение: ",var);
        
    @property
    def v(self):
        return self.__var;
        
    @v.setter
    def v(self,var):
        
        if var==100:
            print ("смени значение");
        else:
            self.__var=var;
                    
    @v.deleter
    def v(self):
        del self.__var
        
    # def talk(self):
        # print ("значение переменой __var сейчас значение: ",self.v);
        

        
b=A("10");
# b.talk();
print ("значение переменой __var сейчас значение:",  b.v)
b.v=101;
print ("значение переменой __var сейчас значение:",  b.v)
del b.v
try:
    print ("значение переменой __var сейчас значение:",  b.v)
except:
    print ("похоже нет атрибута");