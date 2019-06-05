# zver3

class Critter(object):
    """ Виртуальный питомец """
    def __init__(self,name):
        print("Появилась новая зверушка!");
        self.name=name;
    def __str__(self):
        rep="Обьект класса Critter()\n";
        rep+="Имя: "+self.name+"\n";
        return rep;
        
    def talk(self):
        print("Привет. Меня зовут", self.name,"\n");
        
# main

crit1=Critter("Бобик");
crit1.talk();

crit2=Critter("Мурзик");
crit2.talk();
print("Вывод обьекта crit1 на экран");
print(crit1);

print("Непосредственный доступ к атрибуту crit1.name");
print(crit1.name);