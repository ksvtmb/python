# отгадай число

print("отгадай число");

import random;

the_number=int(random.randint(1,100));
guess=int(input("Ваше предложение: "));
tries=1;

# цикл отгадывания

while the_number!=guess:
    if guess>the_number:
        print("Меньше!..");
    else:
        print("Больше!..");
        
    guess=int(input("Ваше предложение: "));
    tries+=1;
    
print ("Ура! Вам удалось отгадать число! Это в самом деле:", the_number);    
print("Вы затратили на это упражнение", tries, "попыток\n");