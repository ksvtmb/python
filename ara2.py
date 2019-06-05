# обработка элементов массива в python

scores=[]
choise=None

while choise!=False:
    print(""" 
    
    Рекорды
    0-Выход
    1-Показать рекорды
    2-Добавить рекорд
    3-Удалить
    4-Сортировка списка
    """);
    
    choise=int(input("Ващ выбор: "));
    print();
    
    # обработка выхода
    if choise==0:
        print("Да звидания!");
        
     # вывод результатов на экран
    elif choise==1:
        print("Рекорды");
        for score in scores:
            print(score);
     
        
    # добавление записи
    elif choise==2:
        score=int(input("Впиши свой рекорд: "));
        if score in scores:
            print("такой рекорд уже есть в списке!");
        else:
            scores.append(score);
        
    
    # удаление записи
    elif choise==3:
        score=int(input("Каакой из рекордов нужно удалить?: "));
        if score in scores:
            scores.remove(score);
        else:
            print("Результат",score, "не содержится в списке рекордов");
    
    # сортировка рекордов
    elif choise==4:
        scores.sort(reverse=True)
        
    # обработка ошибочного ввода пользователя
    else:
        print ("в меню нет пункта", choise);