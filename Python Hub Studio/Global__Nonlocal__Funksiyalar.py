x = 5

def name():
    print(x)

name()

print("============================")


x = 5
def name():

    y = 10
    print(x)

    return y

h = name()
print(h)


print("============================")


x = 5

def name():
    x = 10
    print(x)

name()




print("============================")

x = 5
x += 95
def name():                         #  bundan ko'ra pastagi funksiya qulayroq
    x = 100
    print(x)

name()
print(x)



print("============================")

x = 5
def name():                         # aynan shu funksiya qulay
    global x
    x = 100
    print(x)

name()
print(x)



print("============================")

x = 5
def name():                         
    global x
    x = 100
    print(x)
# bungan keyingi print funksiyalari < global x > funksiyasini o'ziga o'zlashtiriyapti 
# < global x > funksiyasi 100 qiymatni beriyapti sababi pastda x = 100 funksiyasi turibdi
name()
print(x)

def name2():
    print(x)
name2()


print("============================")

x = 5
def name():                         

    x = 100
    return x

h = name()
# bu yerda print fun/i 1 marta kelgani uchun 1 marta chiqiyapti

def name2():
    print(h)
name2()

print("============================")


x = 5

def name():
    x = 100
    return name2(x)

#   Yaxshilab etbor berib o'qi bu kodni

def name2(par):
    print(par)

name()


print("============================")



x = 5

def name():
    x = 10
    def name2():
        x = 100
        print(x)

    name2()
    print(x)

name()
print(x)


print("============================")


x = 5

def name():
    x = 10
    def name2():
        nonlocal x
        x = 100
        print(x)
# bu yerda < x = 10 > fun/i < nonlocal x > fuk/i orqali 100 raqamiga o'zgartiriyapmiz
    name2()
    print(x)

name()
print(x)








a = input("Dastur yopilishi uchun Enterni bosing: \n")