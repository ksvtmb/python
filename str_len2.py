import random

word="индекс"

print("В перемененной word хранится слово: ", word)
hight=len(word)
low=-len(word)

for i in range(10):
    position=random.randrange(low, hight)
    print("word[",position,"]\t",word[position])
input("press any key")        
