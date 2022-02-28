m = [1, 2, 3, 4, 5]
print(m[-1])



m = [1, 2, 3, 4, 5, 'a', [1, 2], ['a', 'f']]
print(m[-1])



m = [1, 2, 3, 4, 5, 'a', [1, 2], ['a', 'f']]
print(m[-1][0])


v = [[5, 6], [1, 2], ['a', 'f']]
print(len(v))



v = [[5, 6], [1, 2], ['a', 'f']]
print(len(v[0]))      # bu yerda 0 indexdagi listda 2 ta raqam bor degani



n = [[5, 6], [1, 2], ['a', 'f']]
n[0] = 9
print(n)     

n[0] = n[0] + 2
print(n)


h = [[5, 6], [1, 2], ['a', 'f']]

h[1], h[2] = h[2], h[1]
print(h)


h = [[5, 6], [1, 2], ['a', 'f']]
h = h + [7]
print(h)



h = [[5, 6], [1, 2], ['a', 'f']]
h = h*2
print(h)


n = list('stroka')
print(n)


n = list(range(10))
print(n)



n = list(range(10))
for i in n:
    print(n)


n = list(range(10))
for i in n:
    print(i)



n = list(range(10))
m = []

for i in n:
    if i == 8:
        continue     # bunda 8 raqamisiz chiqadi
    m += [i]

else:
    print(m)







a = input("Dastur yopilishi uchun Enterni bosing: \n")