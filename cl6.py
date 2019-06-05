# zver prop

class Critter(object):
    """ виртуальный питомец """
    
    def __init__(self,name):
        print ("Появилась на свет новая зверушка!");
        self.__name=name;
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self,new_name):
        if new_name=="":
            print("Имя зверушки не должно быть пустой строкой!")
            
        else:
            self.__name=new_name;
            print("Имя успешно заменено!");
            
    def talk(self):
        print ("\nПривет!. меня зовут: ",self.name);
        
        
# main theme

crit=Critter("Бобик");
crit.talk();

print ("\n Попробую поменять имя зверушки!");
crit.name="Мурзик"

print ("Мою зверушку зовут", end=" ");
print (crit.name)

print ("Пробую моменять имя на пустоту");
crit.name=""

print ("Мою зверушку зовут", end=" ");
print (crit.name)
