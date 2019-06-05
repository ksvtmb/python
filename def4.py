# def4 область. видимости

def read_global():
    print("в области видимости read_global() значение value равно: ",value);
    
def shadow_global():
    value=-10;
    print("в области видимости shadow_global() значение value равно: ",value);
    
def change_global():
    global value;
    value=-10;
    print("в области видимости change_global() значение value равно: ",value);
    
# основная часть
# value - это глобальная переменная. потому что мы сейчас находимся в глобальной области видимости

value=10;

print("в глобально области видимости значение value равно: ",value);
read_global();
print("Вернемся в глобальную область видимости значение value равно все равно: ",value);
shadow_global();
print("Вернемся в глобальную область видимости значение value равно все равно: ",value);
change_global();
print("Вернемся в глобальную область видимости значение value изменилось и оно составляет: ",value);