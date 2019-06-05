# моя зверушка

class Critter(object):
    """ Виртуальный питомец """
    def __init__(self, name, hunger=0, boredom=0):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom
        
    def __pass_time(self):
        self.hunger  +=1
        self.boredom +=1
        
    @property
    def mood(self):
        unhappiness=self.hunger+self.boredom
        
        if unhappiness<5:
            m="прекрасно";
        elif 5 <= unhappiness<=10:
            m="неплохо";
        elif 11 <= unhappiness<=15:
            m="не сказать чтобы хорошо";
        else:
            m="ужасно";
            
        return m;
        
    def talk(self):
        print ("Меня зовут: ",self.name,", и сейчас я чувствую себя:", self.mood," сейчас \n");
        self.__pass_time();
                
    def eat(self, food=4):
        print ("Мрр, спасибо!");
        self.hunger -=food;
        if self.hunger<0:
            self.hunger=0;
        self.__pass_time();
        
    def play(self, fun=4):
        print ("Уииии!");
        self.boredom -=fun;
        if self.boredom<0:
            self.boredom=0;
        self.__pass_time();
    
def main():
    crit_name=input("как вы назовете свою зверушку? ");
    crit=Critter(crit_name);
            
    choise=None;
            
    while choise!="0":
        print \
        (""" 
        Моя зверушка
        0-Выйти
        1-Узнать о самочувствии
        2-Покормить зверушку
        3-Поиграть со зверушкой
        """)
                    
        choise=input("Ващ выбор ");
        print();
                    
        # обработка выхода
                    
        if choise=="0":
            print ("до свидания");
        # беседа
        elif choise=="1":
            crit.talk();
        # кормление
        elif choise=="2":
            crit.eat();
        # игра
        elif choise=="3":
            crit.play();
        # не понятный пользовательский код
        else:
            print ("Извините! но такого пункта нет!", choise);
                
main();
input("\n\n Нажмите, чтобы выйти");
            
                