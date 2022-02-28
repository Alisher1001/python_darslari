##import os
##
##
##for i in os.walk("C:\\Users\Algaritm\Desktop\для примера"):
##    print(i)
## 
##
##
##
##
##
##
##
##
##
##import os
##
##
##for i in os.walk("C:\\Users\Algaritm\Desktop\для примера"):
##    print(i)
##    break
##
##
##
##
##
##
##
##
##
##
##
##import os
##('C:\\Users\\Algaritm\\Desktop\\для примера',
## ['папка 1', 'папка 2'],
## ['файл 1.txt.txt', 'файл 2.txt.txt', 'файл 3.txt.txt'])
##
##
##for adress, dirs, files in os.walk("C:\\Users\Algaritm\Desktop\для примера"):
##    print(i)
##    break
##
##







##import os
##('C:\\Users\\Algaritm\\Desktop\\для примера',
## ['папка 1', 'папка 2'],
## ['файл 1.txt.txt', 'файл 2.txt.txt', 'файл 3.txt.txt'])
##
##spisok = []
##
##for adress, dirs, files in os.walk("C:\\Users\Algaritm\Desktop\для примера"):
##    spisok.append(adress)
##
##
##print(spisok)
##    



##import os
##('C:\\Users\\Algaritm\\Desktop\\для примера',
## ['папка 1', 'папка 2'],
## ['файл 1.txt.txt', 'файл 2.txt.txt', 'файл 3.txt.txt'])
##
##spisok = []
##
##for adress, dirs, files in os.walk("C:\\Users\Algaritm\Desktop\для примера"):
##    for file in files:
##       spisok.append(os.path.join(adress, file))
##
##
##print(spisok)
##
##



##import os
##import time
##('C:\\Users\\Algaritm\\Desktop\\для примера',
## ['папка 1', 'папка 2'],
## ['файл 1.txt.txt', 'файл 2.txt.txt', 'файл 3.txt.txt'])
##
##spisok = []
##
##for adress, dirs, files in os.walk("C:\\Users\Algaritm\Desktop\для примера"):
##    for file in files:
##        full = os.path.join(adress, file)
##        if time.time() - os.path.getctime(full) < 86400:
##            spisok.append(full)
##
##
##print(spisok)
##





a = input("Dastur yopilishi uchun Enterni bosing: \n")


