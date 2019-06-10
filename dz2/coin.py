# подбрось монетку 100 раз и посчитай, сколько решек а сколько орлов

# переменные решек и орлов создать ты должен, падаван

reshka=0
orel=0
count=100

import random

while True:
    guess=random.randint(0,1)
    if guess==0:
        reshka+=1
    else:
        orel+=1
    # print (count)
    count-=1
    if count==0:
        break
print("\tподкинув монетку 100 раз мы узнали:")
print("Решек выппало: ",reshka, "раз(а)")
print("Ну а Орлов выпало: ",orel, "раз(а)")