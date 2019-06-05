# эксклюзивная сеть

security=0;
username="";
password="";

while not username:
    username=input("Login: ");

while not password:
    password=input("Password: ");

    
if username=="dawson" and password=="1234":
    print("hello mike")
    security=5
elif username=="meier" and password=="civil":
    print("hello sid")
    security=3
elif username=="miyamoto" and password=="mario":
    print ("hello sigery")
    security=3
elif username=="wright" and password=="sims":
    print("how you do mr. Will?")
    security=3
elif username=="guest" or password=="guest":
    print("Добро пожаловать к нам в гости");
    security=1
elif username=="kas" and password=="kas":
    print("hello owner");
    security=7;
else:
    print("не удалось вас опознать")