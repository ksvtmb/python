# привередливая программа

count=0;

while True:
    count+=1;
    if count>10:
        break;
    # skip 5
    if count==5:
        continue;
    print(count);    