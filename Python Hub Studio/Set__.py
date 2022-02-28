#t = {'a', 'b', 1,1,1,1,1,1,2,3,4,5, (2,3)}
#print(t)



##x = (1,2,3,4,5,6,7)
##y = [1,2,3,4,5,6,7]
##u = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7}
##l = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
##h = {1,2,3,4,5,6,7}
##
##
##print(x.__sizeof__())
##print(y.__sizeof__())
##print(u.__sizeof__())
##print(l.__sizeof__())
##print(h.__sizeof__())





##import time
##
##def foo(*args):
##        list_new = []
##        for i in args:
##                for y in i:
##                        if y not in list_new:
##                                list_new.append(y)
##        return list_new
##
##
##z = list(range(10000))
##x = list(range(5000, 15000))
##c = list(range(10000, 20000))
##
##start = time.time()
##
##foo(z,x,c)
##stop = time.time() - start
##print(stop)
##
##
##start2 = time.time()
##r = set(z)
##t = r.union(set(x), set(c))
##
##stop2 = time.time() - start2
##print(stop2)







r = open("Hurmo.txt")
r1 = set(r.read().split())

r.close()



r = open("Hurmo2.txt")
r2 = set(r.read().split())

r.close()


new = r1.difference(r2)
print(new)
##
##print("=====================================")
##
##new2 = r2.difference(r1)
##print(new2)






a = input("Dastur yopilishi uchun Enterni bosing: \n")



