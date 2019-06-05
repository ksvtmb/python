# исследуем функции

def display(message):
    print(message);
    
def give5():
    five=5;
    return five;
    
def ask(question):
    """ Задает вопрос с ответом yes или no"""
    response=None;
    while response not in ("y","n"):
        response=input(question).lower();
    return response;
    
# Основная часть программы

display("Вам сообщение\n");

number=give5();
print("функция give5() возвратила следующий результат: ",number);

answer=ask("\n Пожалуйства! введите 'y' или 'n': ");
print("Спасибо! Вы ввели: ",answer);