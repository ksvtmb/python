#выводим слово наоборот

string=input("введи слово, которое стоит выверуть!: " )
print("слово:",string)

change_string=""

dlina=-len(string)

n=-1
while n>=dlina:
    # print(n)
    change_string+=string[n]
    n-=1


print("слово наоборот: ",change_string)