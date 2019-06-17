# игра в слова по анаграма

import random
# константа
WORDS=("питон","гадюка", "кобра","мамба")
# выбираем один элемент с кортежа рандомно
word=random.choice(WORDS)
# записываем корректное выбраное словов в отдельную переменную
correct=word

# пустая анаграма
jumble=""

# после третьего фейла даем подсказку
p=0
# количество полученных подсказок
pod=0


# начинаем цикл
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]

print("чувак отгадай загадку. вот тебе анаграма: ",jumble,"\nОтгадай исходное слово")

guess=input("давай вариант: ")
while guess!=correct and guess!="":
    p+=1
    print("не угадали, трай эген")
    guess=input("еще раз вариант: ")

    if p==2:
        yes_or_no=input("Чувак хочешь подсказку ? (y/n): ")
        if yes_or_no=="y":
            print("подсказка такая: в загадном слове, первая буква:", correct[0],"последняя буква:",correct[-1])
            pod+=1
            p=-1
        else:
            p=-1            

if guess==correct and pod==0:
    print("bingo! ты угадал ! без подсказок")
elif guess==correct and pod>0:
    print("bingo! ты угадал ! хоть юзая подсказки")

print("game over")