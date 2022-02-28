print("Funksiyadan oldin")

def show():
    print("funksiya")
show()

print("Funksiyadan keyin")

show()

print("============================")

def show():
    print("funksiya")

def show2():
    x = 7
    return x     # return funksiyasi < x > ni qiymatini keyingi show2 funksiyasiga qatariyapdi

y = show2()
print(y)

show()

print("============================")

def show():
    print("funksiya")

def show2():
    x = 7
    return x    # return funksiyasi < x > ni qiymatini keyingi show2 funksiyasiga qatariyapdi

y = show2() + 9


print(y)

show()


print("============================")


def show():
    print("funksiya")

def show2():
    x = 7 + z
    return x    # return funksiyasi < x > ni qiymatini keyingi show2 funksiyasiga qatariyapdi


z = 7
y = show2()

print(y)

show()



print("============================")



def show():
    print("funksiya")

def show2():
    x = 7 + z
    return x    # return funksiyasi < x > ni qiymatini keyingi show2 funksiyasiga qatariyapdi

z = 7

print(show2())
# y = show2()     # 2 funksiyani ham ishlashi bir xil yani bittasi qisqartirilgan variyant
# print(y)

z = 9
print(show2())
# t = show2()
# print(t)

show()

a = input("Dastur topilishi uchun Enterni bosing: \n")