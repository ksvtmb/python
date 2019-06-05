# ловим исключения

try:
    num=float(input("Введите число: "));
except ValueError as e:
    print("Похоже! это не число");
    print(e);
else:
    print("вы ввели число: ", num)
