start=finish=step =0
print (start)

start=input("начальная цифра: ")
start=int(start)

finish=input("конечная цифра: ")
finish=int(finish)

step=input("шаг счета: ")
step=int(step)
if not step or step==0:
    step=1

chislo=0

for i in range(start,finish,step):
    chislo+=i

print("число: ", chislo)