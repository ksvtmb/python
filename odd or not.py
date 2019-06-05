# определяем число четное или нет )


n=1;
chet=0;
nechet=0;

import random;

while n<=100:
    # print (n);
    chislo=int(random.randint(0,1));
    if (chislo%2)==0:
        # print(chislo,"четное");
        chet+=1;
    elif (chislo%2)==1:
        # print(chislo,"не четное");
        nechet+=1;
    
     
    n+=1;
    
print("за 100 подбрасываний монеток. выпало орлов:",chet,"решек",nechet);