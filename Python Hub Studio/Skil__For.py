for i in 'Stroka text':
    print(i)

print("Dastur ishlashda davom etsin")



m = "Stroka text"

for i in m:
    if i == "t":
        print("Bu qatorda < t > harfi bor")

else:
    print("Skil yakunlandi")

print("Dastur ishlashda davom etsin")





m = "Stroka text"
count = 0


for i in m:
    if i == "t":
        print("Bu qatorda < t > harfi bor")
        count += 1
else:
    print("Skil yakunlandi, < t > harfi bor", count, "ta")

print("Dastur ishlashda davom etsin")



m = "Stroka text"
count = 0


for i in m:
    if i == "t":
        print("Bu qatorda < t > harfi bor")
        count += 1

    if i == "a":       # bu buyruq < m > o'zgaruvchisini -a- harfigacha ishla degani
        break
else:
    print("Skil yakunlandi, < t > harfi bor", count, "ta")

print("Dastur ishlashda davom etsin")





m = "Stroka text"
count = 0


for i in m:
    if i == "t":
        continue
        print("Bu qatorda < t > harfi bor")
        count += 1
    print(i)
else:
    print("Skil yakunlandi, < t > harfi bor", count, "ta")

print("Dastur ishlashda davom etsin")











m = "Dunyodagi eng kuchli dasturchi"

count = 0
for i in m:
    if i == "u":
        print("Bu qator < u > harfi bor")
        count += 1


else:
    print("Skil yakunlandi, < u > harfi bor", count, "ta")


count = 0
for i in m:
    if i == "i":
        print("Bu qatorda < i > harfi bor")
        count += 1

else:
    print("Skil yakunlandi, < i > harfi bor", count, "ta")


print("Dastur ishlashda davom etsin")










m = "Dunyodagi eng kuchli dasturchi"

count = 0
for i in m:
    if i == "u":
        continue
        print("Bu qator < u > harfi bor")
        count += 1
    print(i)


else:
    print("Skil yakunlandi, < u > harfi bor", count, "ta")


count = 0
for i in m:
    if i == "i":
        continue
        print("Bu qatorda < i > harfi bor")
        count += 1
    print(i)

else:
    print("Skil yakunlandi, < i > harfi bor", count, "ta")


print("Dastur ishlashda davom etsin")






a = input("Dastur yopilishi uchun Enterni bosing: \n")