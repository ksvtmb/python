# его величество рандом

import random

mood=random.randint(1,3)

if mood==1:
    print("огонь настроение")
elif mood==2:
    print("нормуль настроение")
elif mood==3:
    print ("так себе чота!")
else:
    print ("хз как это у тебя получилось")

input("press any key")