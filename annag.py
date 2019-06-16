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

# начинаем цикл
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]

print("чувак отгадай загадку. вот тебе анаграма: ",jumble,"\nОтгадай исходное слово")

guess=input("давай вариант: ")
while guess!=correct and guess!="":
    print("не угадали, трай эген")
    guess=input("еще раз вариант: ")

if guess==correct:
    print("bingo! ты угадал")

print("game over")
input("press any key")