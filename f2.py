# Запись файлов

print("создаю текстовый файл методом write()");

text_file=open("write_it.txt","w",encoding='utf-8');

text_file.write("Строка 1\n");
text_file.write("Это строка 2\n");
text_file.write("Этой строке достался номер 3\n");

text_file.close();

print("проверки для, читаю весь файл целиком");

text_file=open("write_it.txt","r",encoding='utf-8');\
print(text_file.read());
text_file.close();