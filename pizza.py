# are you  like pizza?

word="пицца"
print(
"""    
0   1   2   3   4   5
+---+---+---+---+---+
| П | И | Ц | Ц | А |
+---+---+---+---+---+
 -5  -4  -3  -2  -1
"""
)

print("Введите начальный и конечные индексы для среза 'пиццы', который желаете получить!")
start=None
while start !="":
    start=input("\nНачальная позиция: ")
    if start:
        start=int(start)
        finish=int(input("Конечная позиция: "))
        print("Срез слова word[",start,":",finish,"] выглядит как", end=" ")
        print(word[start:finish])
input("press any key")
