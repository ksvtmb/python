## show and manage records!

scores=[]
choise=None

# show menu

while choise!="0":
    print("""
    RECORDS:
    0 - exit programm
    1 - show records
    2 - add record
    3 - delete record
    4 - sort records 
    """)
    choise=input("you choise: ")
    print()

# exit from programm

    if choise=="0":
        print("good luck!")
    elif choise=="1":
        print("thats is a all records:")
        for score in scores:
            print(score)
    elif choise=="2":
        score=int(input("add you record: "))
        scores.append(score)
        print("scores is added by new values")
    elif choise=="3":
        score=int(input("which record must delete?: "))
        if score in scores:
            scores.remove(score)
            print("Done! record", score,"deleted")
        else:
            print("record:", score,"is not found")
    elif choise=="4":
        scores.sort(reverse=True)
        print("scores is sorted!")
    else:
        print("incorect choose!")