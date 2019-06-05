# cl4.py oop

class Critter(object):
    """ виртуальный питомец """
    total=0;
    @staticmethod
    def status():
        print("\n Всего зверушек сейчас:", Critter.total);
        
    def __init__(self,name):
        print("Появилась новая зверушка");
        self.name=name;
        Critter.total+=1;
        
    @staticmethod
    def ura():
        return 1;
        
# main

# print("Нахожу значение атрибута класса Critter.total: ",end=" ");
# print (Critter.total);
# print("Создаю зверушек!");

# crit1=Critter("Зверушка 1");
# crit2=Critter("Зверушка 2");
# crit3=Critter("Зверушка 3");
# Critter.status();
print(Critter.ura());
# Critter.status()
# print("\nОбращаюсь к аттрибуту класса через объект: ", end=" ");
# print(crit1.total);