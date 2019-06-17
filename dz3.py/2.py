#выводим слово наоборот

string=input("введи слово, которое стоит выверуть: " )
change_string=""
n=-1

while n>=-len(string):
    change_string+=string[n]
    n-=1

print("слово наоборот: ",change_string)