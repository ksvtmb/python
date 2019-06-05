# class2 работаем с конструктором

class Critter(object):
    """ construct """
    def __init__(self):
        print("Явилась на свет зверюга! конструктор");
        
    def talk(self,dig):
        print("\n",dig)
        
crit1=Critter();
crit1.talk("lalal")
crit1.talk("TrtR")
crit2=Critter();
crit2.talk("ololo");