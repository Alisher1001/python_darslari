

##h = [9,8,7,4,5,6,3,2,1,5,5]




##new = []
##for x in h:
##        new.append(x*2)
##print(new)
##
##
##
##new2 = [x*2 for x in h]
##print(new2)





##z = {x*2 for x in h}
##print(z)





##f = {x: x*2 for x in h}
##print(f)






##new = []
##for x in h:
##        if x % 2 == 0:
##                new.append(x*2)
##print(new)
##
##
##
##g = [x for x in h if x % 2 == 0]
##print(g)
##print(type(g))






##h = [9,8,7,4,5,6,3,2,1,5,5, -2]
##
##new = []
##for x in h:
##        if x % 2 == 0:
##                new.append(x*2)
##print(new)
##
##
##g = [x for x in h if x % 2 == 0 and x > 0]
##print(g)









##import os
##h = [9,8,7,4,5,6,3,2,1,5,5, -2]
##
##g = [os.path.join(z, i) for z, x, c in os.walk("C:\\") for i in c]
##
##print(len(g))






##import os
##h = [9,8,7,4,5,6,3,2,1,5,5, -2]
##
##g = [os.path.join(z, i)
##     for z, x, c in os.walk("C:\\")
##     for i in c if ".txt" in i]
##
##print(g)


##import os
##h = [9,8,7,4,5,6,3,2,1,5,5, -2]


price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}


new_price = {}
for i in price.keys():
        new_price[i] = round(price[i] * 0.85, 2)
print(new_price)

new_d = {i: round(price[i] * 0.85, 2) for i in price.keys()}
print(new_d)
















