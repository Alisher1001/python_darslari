x = (9, 8, 7, 6)
print(type(x))


x = 9, 8, 7, 6
print(type(x))


x = tuple('stroka')
print(x)

print("============================")


x = (9, 8, 7, 6)
print(x[0]) 
print(x)

print("============================")


x = (9, 8, 7, 6)
print(x[0] + 5) 
print(x)


x = (9, 8, 7)
z, c, b = x
print(x)      # har bir harfga raqam berdi



x = (9, 8, 7)
z, c, b = x
print(x)      # har bir harfga raqam berdi



r = 5,
u = 7,

r, u = u, r
print(r, u)
print(type(r))
print(type(u))


x = (9, 8, 7, 6, 5, 4, 3)
print(x[1:5])




x = [9, 8, 7, 6, 5, 4, 3]
for i in range(len(x)):
    x[i] += 3
              # 7 ta raqamni o'zgartirmasdan x o'zgaruvchisiga 3 ta raqamni qo'shiyapti
print(x)      # qo'shgandan keyin ham katta raqamlar bilan qo'shiyabti

print("============================")


x = (9, 8, 7, 6, 5, 4, 3)
y = []
for i in range(len(x)):
    y.append(x[i] + 3)
              
              # 7 ta raqamni o'zgartirmasdan x o'zgaruvchisiga 3 ta raqamni qo'shiyapti
print(x)      # qo'shgandan keyin ham katta raqamlar bilan qo'shiyabti
print(y)

print("============================")


t = list(x)
t[0] = 10
x = tuple(t)
print(x)

print("============================")

x = (9, 8, 7, 6, 9, 5, 4, 3)
print(x.count(9))


x = (9, 8, 7, 6, 9, 5, 4, 3)
print(x.index(9))


h = (1, 2, 3)
h += (4, 5)
print(h)


h = (1, 2, 3)
g = h
h += (4, 5)
print(h)
print(g)


a = input("Dastur yopilishi uchun Enterni bosing: \n")