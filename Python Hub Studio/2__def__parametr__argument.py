j = [9, 8, 7, 6]

count = 0
for i in j:
    count += 1
print(count)




print("============================")



j = [9, 8, 7, 6]

def count_list():
    count = 0
    for i in j:
        count += 1
    return count

print(count_list())




print("============================")




def count_list(par):   # parametr
    count = 0
    for i in par:
        count += 1
    return count

j = [9, 8, 7, 6]

print(count_list(j))   # argument




print("============================")




h = ['a', 'a', 'h']
print(count_list(h))


k = [9, 8, 7, 5, 6, 7]
print(count_list(k))


print(count_list("sttrooka"))



print("============================")




def count_list(par, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    
    for i in par:
        count += 1
    return count

j = [9, 8, 7, 6]

print(count_list(j))



print("============================")



def count_list(par, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    
    for i in par:
        count += 1
    return count

j = [9, 8, 7, 6]

print(count_list(j, 0))



print("============================")



def count_list(par, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    
    for i in par:
        count += 1
    return count

j = [9, 8, 7, 6]

print(count_list(j, -1))   # < j > o'zgaruvchida 4 ta raqm bor bo'sa uni bittasini ayrib ko'ratayabdi



print("============================")



def count_list(par, par2 = False, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    if par2 == True:        # bu yerda if sharti ishlamayapdi
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count

j = [9, 8, 7, 6]

print(count_list(j))



print("============================")



def count_list(par, par2 = False, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    if par2 == True:        # bu yerda if sharti ishlamayapdi
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count

j = [9, 8, 7, 6]

print(count_list(j, count=-1))
# bu yerda < count = 0 > par/ga < count=-1 > argument bo'liyabdi





print("============================")




def count_list(par, par2 = False, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count

j = [9, 8, 7, 6]

print(count_list(j, True)) # True if sharti ishlashi uchun qaysi turga mansub malumotligini bilish uchun

# bu yerda esa < par2 = False > par/ga < True > argument bo'liyabdi


print("============================")



def count_list(par, par2 = False, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count

j = [9, 8, 7, 6]

print(count_list(j, True, -1))




print("============================")


def count_list(par, par2 = False, count = 0):   # parametrga count = 0 funksiyasini qo'shib yozsak bo'ladi
    if par2 == True:
        typ = type(par[0])
        for i in par:
            count += 1
        return count, typ
    else:
        for i in par:
            count += 1
        return count

j = [9, 8, 7, 6]

h, p = count_list(j, True)
print(h)
print(p)






a = input("Dastur yopilishi uchun Enterni bosing: \n")