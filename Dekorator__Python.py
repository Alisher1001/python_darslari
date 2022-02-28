##def decator(func):
##
##        def inner():
##                print("start decarator...")
##                func()
##
##
##                print("finish decarotor...")
##        return inner
##
##def say():
##        print("hello world")
##
##
##d = decator(say)
##print(d)







##def decator(func):
##
##        def inner():
##                print("start decarator...")
##                func()
##
##
##                print("finish decarotor...")
##        return inner
##
##def say():
##        print("hello world")
##
##
##d = decator(say)
##d()






##def decator(func):
##
##        def inner():
##                print("start decarator...")
##                func()
##
##
##                print("finish decarotor...")
##        return inner
##
##def say():
##        print("hello world")
##
##
##d = decator(say)
##d()
##
##
##
##t = decator(say)
##t()




##def decator(func):
##
##        def inner():
##                print("start decarator...")
##                func()
##
##
##                print("finish decarotor...")
##        return inner
##
##def say():
##        print("hello world")
##
##
##say = decator(say)
##say()








##def decator(func):
##
##        def inner():
##                print("start decarator...")
##                func()
##
##
##                print("finish decarotor...")
##        return inner
##
##def say():
##        print("hello world")
##
##
##def buy():
##        print("buy world")
##
##
##say = decator(say)
##say()
##
##
##buy = decator(buy)
##buy()







##def decator(func):
##
##        def inner(n):
##                print("start decarator...")
##                
##                func(n)
##
##                print("finish decarotor...")
##        return inner
##
##def say(name):
##        print("hello", name)
##
##
##
##say = decator(say)
##say("Vasya")









##def decator(func):
##
##        def inner(n, m):
##                print("start decarator...")
##                
##                func(n, m)
##
##                print("finish decarotor...")
##        return inner
##
##def say(name, surname):
##        print("hello", name, surname)
##
##
##
##say = decator(say)
##say("Vasya", "Ivanov")











##def decator(func):
##
##        def inner(*args, **kwargs):
##                print("start decarator...")
##                
##                func(*args, **kwargs)
##
##                print("finish decarotor...")
##        return inner
##
##def say(name, surname):
##        print("hello", name, surname)
##
##
##
##say = decator(say)
##say("Vasya", "Ivanov")








##def decator(func):
##
##        def inner(*args, **kwargs):
##                print("start decarator...")
##                
##                func(*args, **kwargs)
##
##                print("finish decarotor...")
##        return inner
##
##def say(name, surname, age):
##        print("hello", name, surname, age)
##
##
##
##say = decator(say)
##say("Vasya", "Ivanov", 30)







##def header(func):
##
##        def inner(*args, **kwargs):
##                print("<h1>")
##                
##                func(*args, **kwargs)
##
##                print("</h1>")
##        return inner
##
##def say(name, surname, age):
##        print("hello", name, surname, age)
##
##
##
##say = header(say)
##say("Vasya", "Ivanov", 30)







##def header(func):
##
##        def inner(*args, **kwargs):
##                print("<h1>")
##                
##                func(*args, **kwargs)
##
##                print("</h1>")
##        return inner
##
##
##
##def table(func):
##
##        def inner(*args, **kwargs):
##                print("table")
##                
##                func(*args, **kwargs)
##
##                print("</table")
##        return inner
##
##
##
##def say(name, surname, age):
##        print("hello", name, surname, age)
##
##
##
##say = table(header(say))
##say("Vasya", "Ivanov", 30)






##def header(func):
##
##        def inner(*args, **kwargs):
##                print("<h1>")
##                
##                func(*args, **kwargs)
##
##                print("</h1>")
##        return inner
##
##
##
##def table(func):
##
##        def inner(*args, **kwargs):
##                print("table")
##                
##                func(*args, **kwargs)
##
##                print("</table")
##        return inner
##
##
##@header # say = header(say)
##def say(name, surname, age):
##        print("hello", name, surname, age)
##
##
##
####say = header(table(say))
##say("Vasya", "Ivanov", 30)






##def header(func):
##
##        def inner(*args, **kwargs):
##                print("<h1>")
##                
##                func(*args, **kwargs)
##
##                print("</h1>")
##        return inner
##
##
##
##def table(func):
##
##        def inner(*args, **kwargs):
##                print("table")
##                
##                func(*args, **kwargs)
##
##                print("</table")
##        return inner
##
##
##@table # say = header(say)
##def say(name, surname, age):
##        print("hello", name, surname, age)
##
##
##
####say = header(table(say))
##say("Vasya", "Ivanov", 30)





def header(func):

        def inner(*args, **kwargs):
                print("<h1>")
                
                func(*args, **kwargs)

                print("</h1>")
        return inner



def table(func):

        def inner(*args, **kwargs):
                print("table")
                
                func(*args, **kwargs)

                print("</table")
        return inner

@table
@header # say = header(table(say))
def say(name, surname, age):
        print("hello", name, surname, age)



##say = header(table(say))
say("Vasya", "Ivanov", 30)









