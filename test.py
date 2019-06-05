def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        
        

gena=createGenerator();
# print (gena);

# for i in gena:
    # print(i)
    
print(gena.__next__());
print(gena.__next__());
print(gena.__next__());
