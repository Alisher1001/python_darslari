x = "qwertyuiopasdfghjklzxcvbnm"
y = input("Ko'rmoqchi bo'lgan qatorni ko'shinlar: \n")
for i in x:
    count = 0
    for r in y:
        if i == r:
            count += 1
    print("alfavit", i, "qatnashganlari", count)





##x = "qwertyuiopasdfghjklzxcvbnm"
##y = input("Ko'rmoqchi bo'lgan qatorni ko'shinlar: \n")
##for i in x:
##    count = 0
##    for r in y:
##        if i == r:
##            count += 1
##    if count > 0:
##        print("alfavit", i, "qatnashganlari", count)




## for i in range(start, stop, [step]):
##     print(x)


# for x in range(1, 10, 2):
#     print(x)




# for x in range(10, -10, -2):
#     print(x)




a = input("Dasturni yopish uchun Enterni bosing: \n")
