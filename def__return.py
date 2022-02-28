

##a = abs(-7)
##b = max(4, abs(-90), 4, min(100, 200))
##print(a)
##print(b)



##def squr(x):
##        print(x**2)
##
##
##a = squr(6)
##print(a)




##def squr(x):
##        return x**2
##        
##
##a = squr(6)
##print(a)





##def squr(x):
##        return x**2
##        
##
##a = squr(squr(3))
##print(a)




##def exam():
##        print(1)
##        print(2)
##        return 'hello'
##        print(3)
##        print(4)
##
##exam()






##def exam():
##        print(1)
##        print(2)
##        return 'hello'
##        print(3)
##        print(4)
##
##print(exam())






##def exam():
##        return 1
##        return 2
##        return 3
##print(exam())





##def even (x):
##        if x%2==0:
##                return True
##        else:
##                return False
##          
##for i in range(1, 11):
##        print(i, even(i))






##def even (x):
##        if x%2==0:
##                return True
##        return False
##          
##for i in range(1, 11):
##        print(i, even(i))





##def even (x):
##        return x%2==0
##          
##for i in range(1, 11):
##        print(i, even(i))







##def factor(x):
##        pr = 1
##        for i in range(2, x + 1):
##                pr = pr * i
##        return pr
##
##for i in range (1, 8):
##        print(i, factor(i))
##
##
##
##
##def sochet(n, k):
##        return factor(n)/ (factor(k)*factor(n-k))
##        
##
##print(sochet(5, 3))




##def sq1(a, b):
##
##        return a*b,  2*(a+b)
##
##
##print(sq1(3, 6), type(sq1(3, 6)))






##def sq1(a, b):
##
##        return a*b,  2*(a+b)
##
##
##print(sq1(2, 5), type(sq1(3, 6)))






##def sq1(a, b):
##
##        return a*b,  2*(a+b)
##
##
##foo, bar = sq1(2, 5)
##print(foo, bar)








def sq1(a, b):
        mas = []
        mas.append(a*b)
        mas.append(2*(a+b))
        return mas



print(sq1(2, 6))






