# Гибель пришельца

class Player(object):
    """ игрок в экшн игры """
    
    @property
    def cry(self):
        return "из бластера";
    
    
    def blast(self, enemy):
        print("Игрок стреляет во врага", self.cry,"\n")
        enemy.die();
        

        
class Alien(object):
    """ действия пришельца """
    def die(self):
        print ("Пришелец умирает");
        
print ("Гибель прищельца. скачать без смс");

hero =Player();
invaider=Alien();
hero.blast(invaider);