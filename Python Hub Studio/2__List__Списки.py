x = [9, 8, 7, 6, 5]
x.append(4)
print(x)

x.insert(1, 7)
print(x)

print(x.count(7))

x.sort()
print(x)

x.reverse()
print(x)

y = x.pop(0)
print(y)   # bu x o'zgaruvchisidagi <0> index raqamidagi raqamni <y> o'zgfaruvchisiga o'tgaz degani

x.pop(0)
print(x)



x.remove(7)
print(x)

x.clear()
print(x)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9,]
x.extend(y)
print(x)

h = x.copy()
print(h)

n = list(range(10))
m = []




n = list(range(10))
m = []

for i in n:
    if i == 8:
        continue
    m.append(i)

else:
    print(m)



n = list(range(1, 21))
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)

print("============================")

n = list(range(1, 21))
b = n
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
print(b)


print("============================")

n = list(range(1, 21))
b = n.copy()
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)

print(b)



print("============================")

n = list(range(1, 21))
b = n[::]     # [start:stop:step] ko'rinishining qisqartmasi
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)

print(b)


print("============================")

n = list(range(1, 21))
b = n[0::2]   # bu bilan n.remove(i) funksiyasining vazifalari bir xil
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        # n.remove(i)

else:
    print(n)
    print(m)

print(b)


print("============================")

n = list(range(1, 21))
b = n[1::2]   # bu bilan m.append(i) funksiyasining vazifalari bir xil
m = []

for i in n:
    if i % 2 == 0:
        # m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)

print(b)




print("============================")

n = list(range(1, 21))
b = n[5:]   # buni manabunday ko'rinishlari bor [:5], [5:9], [-1:-5], [::-1]
m = []

for i in n:
    if i % 2 == 0:
        m.append(i)
        # n.remove(i)

else:
    print(n)
    print(m)

print(b)




a = input("Dastur yopilishi uchun Enterni bosing: \n")