def name(*a):
    print(a)

name()


##print("============================")
##
##
##def name(*a):
##    print(a)
##
##name(7, 9, 8, 7)
##
##
##def name(h, *args):
##    print(h)
##    print(args)
##
##name(1, 2, 3)
##
##print("============================")
##
##
##def name(h, g, *args):
##    print(h)
##    print(g)
##    print(args)
##
##name(1, 2, 3)
##
##print("============================")
##
##
##
##def name(h=7, g=5, *args, key):
##    print(h)
##    print(g)
##    print(args)
##
##name(1, 2, 3, 4, 5, 6, key=10)
##
##
##print("============================")
##
##
##def name(h=7, g=5, *args, key):
##    print(h)
##    print(g)
##    print(args)
##    print(key)
##name(1, 2, 3, 4, 5, 6, key=10)
##
##
##print("============================")
##
##
##def exclusive_item(*args):
##    new_list = []
##    for i in args:
##        for y in i:
##            if y not in new_list:
##                new_list.append(y)
##    return new_list
##
##z = [9, 8, 6]
##x = [7, 6, 3, 0, 4, 7, 9]
##c = [3, 6, 8, 9, 2, 5, 4, 1, 3, 0]
##
##t = exclusive_item(z, x, c)   # list da bor bo'lgan raqamlarni ko'rsatadi 
##print(t)
##
##
##print("============================")
##
##
##def exclusive_item(*args):
##    new_list = []
##    for i in args:
##        for y in i:
##            if y not in new_list:
##                new_list.append(y)
##    return new_list
##
##z = [9, 8, 6]       
##x = [7, 6, 3, 0, 4, 7, 9]
##c = [3, 6, 8, 9, 2, 5, 4, 1, 3, 0]
##
##t = exclusive_item()      # o'zgaruvchilar yo'q bo'lgani uchun list bo'sh bo'lib ko'riniyabdi
##print(t)
##
##
##
##print("============================")
##
##
##
##def exclusive_item(*args, key=False):
##    new_list = []
##    for i in args:
##        for y in i:
##            if y not in new_list:
##                new_list.append(y)
##    if key == True:
##        new_list.sort()           
##    return new_list
##
##z = [9, 8, 6]
##x = [7, 6, 3, 0, 4, 7, 9]
##c = [3, 6, 8, 9, 2, 5, 4, 1, 3, 0]
##
##t = exclusive_item(z, x, c, key=True)
##print(t)
##
##
##
##
##





# def name(h=1,g=4,k=2,r=2,y=3, *args):
#     print(h)
#     print(g)
#     print(k)
#     print(r)
#     print(y)
#     print(args)
# name(1,2,3,4,5,6, )

def anor(*a):
    new_list = []
    for i in a:
        for y in i:
            if y not in new_list:
                new_list.append(y)
                new_list.sort()
    return new_list
    # if key == True:
    #     new_list.sort()
    # return new_list

z = [9, 1, 7, 6, 1]
x = [7, 6, 8, 7, 5, 4]
c = [1, 2, 3, 4, 5, 7, 6, 5, 9, 0]






















##a = input("Dastur yopilishi uchun Enterni bosing: \n")
