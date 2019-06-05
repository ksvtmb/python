# сериализация данных

import pickle, shelve

print("консервация или сериализация")

variety=["огурцы", "помидоры", "капуста"]
shape=["целые", "кубиками", "соломкой"]
brand=["Главпродукт", "Чумак","Бондюэль"]
f=open("pickles1.dat","wb");

pickle.dump(variety, f);
pickle.dump(shape, f);
pickle.dump(brand, f);

f.close();