# разконсервация
import pickle, shelve

print("расконсервация данных");

f=open("pickles1.dat","rb")
variety=pickle.load(f)
print(variety);

shape=pickle.load(f)
print(shape);

brand=pickle.load(f)
print(brand);

f.close();

