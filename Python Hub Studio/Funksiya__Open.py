##import os
##
##list_paths = []
##
##for adress, papka, file in os.walk('C:\\'):
##        for i in file:
##                full_path = os.path.join(adress, i)
##                list_paths.append(full_path)
                







##"r" открить для чтения (по умолчанию)!!!
##"t" открить в текстовом режиме (по умолчанию)!!!
##"w" открить для записи,содержимое файла удаляется, если файла нет создается новый!!!
##"a" открить для дозаписи в конец файлаб если нет создается новый!!!
##"b" открить в бинарном режиме!!!
##"+" открить для чтения и записи "r+" "w+" "a+"!!!






r = open('text3.txt')
u = r.read()
print(u)
r.close()






r = open('text.txt')
for i in r:
        if 'read.py' in i:
                print(i)



##r = open('text3.txt')
##r.write('Ctroka texta')
##print(r)
##r.colse()
##
##
##h = open('text2.txt')
##print(h.read())




##r = open("text.txt", 'w')
##for x in list_paths:
##        r.write(x + '\n')
##r.close()




































########   bunday fayl mavjud emas \exe\

######r = open('e.exe', 'rb')
######y = open('Kopiya e.exe', 'wb')
######
######while True:
######        var = r.read(1048576)
######        print(var.__sizeof__())
######
######        y.write(var)
######
######
######
######        
######print('Kontrol')
######
######r.close()
######y.close()

##r = open('23.txt')
##h = r.read()
##print(h)
##
##
a = input("Dastur yopilishi uchun Enterni bosing: \n")






