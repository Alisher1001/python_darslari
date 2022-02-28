x = 0

while x < 5:
    x += 1
    print(x)





x = 0

while x < 5:
    x += 1

else:
    print(x)






# bu doimiy dastur
while True:
    x = int(input())
    a = 0
    y = 1

    while a < x:
        a += 1
        y *= a

    else:
        print(y)






x = ''      # bu yerda hech qanday o'zgaruvchi kerak emas hatto prabel ham  
            # prabel qo'yilsa len 4 marta sanaydi

while len(x) < 5:
    y = input("Ma'na malumot: ")



    x += y
else:
    print(x)








x = ''      # bu yerda hech qanday o'zgaruvchi kerak emas hatto prabel ham  
            # prabel qo'yilsa len 4 marta sanaydi
            
while len(x) < 5:
    y = input("Ma'na malumot: ")
    if y == "o":
        continue


    x += y
else:
    print(x)






x = ''

while len(x) < 5:
    y = input("Ma'na malumot: ")
    if y == "o":
        continue
    if y == "l":
        break

    x += y
else:
    print(x)

print("Dastur ishlashda davom etsin")





a = input("Dasturni yopish uchun Enterni bosing: \n")