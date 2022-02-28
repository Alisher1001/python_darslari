##def decor(f):
##        def wrapper():
##                print("Bezatuvchini kodi")
##                f()
##                print("Bezatuvchining keyingi kodi")
##        return wrapper
##
##
##@decor  # make = decor(make)
##def make():
##        enter = input("Enter something... ")
##        print(enter)
##
##print("bor")
##make()
##




def decor(f):
        def wrapper():
                try:
                        h = f()
                except Exception:
                        print("Yana urinib ko'ring...")
                        h = f()
                return h
        return wrapper


@decor  # make = decor(make)
def make():
        enter = float(input("Raqmni kiriting: "))
        return enter
@decor
def make2():
        enter = float(input("Yana raqmni kiriting: "))
        return enter
make2()
make()























