##while True: 
##        try:
##                enter = float(input("Raqamni kiriting: \n"))
##                break
##        except ValueError:
##                print("Bu raqam emas!!!")
##
##print("Hammsi joyda")



##while True: 
##        try:
##                enter = float(input("Raqamni kiriting: \n"))
##                print(100/enter)
##                break
##        except ValueError:
##                print("Bu raqam emas!!!")
##
##        except ZeroDivisionError:
##                print("Nolni kiritmang")
##
##print("Hammsi joyda")




##while True: 
##        try:
##                enter = float(input("Raqamni kiriting: \n"))
##                print(100/enter)
##                
##        except ValueError:
##                print("Bu raqam emas!!!")
##
##        except ZeroDivisionError:
##                print("Nolni kiritmang")
##        else:
##                print("Hammasi joyda yana bir bor urunib ko'r")
##        finally:
##                print("bu finally")
##print("Hammsi joyda")





##while True: 
##        try:
##                enter = float(input("Raqamni kiriting: \n"))
##                print(100/enter)
##                
##        except ValueError:
##                print("Bu raqam emas!!!")
##        
##
##        else:
##                print("Hammasi joyda yana bir bor urunib ko'r")
##        finally:
##                print("mana finally")
##print("Hammsi joyda")








##import sys
##
##ww_list = ["1.txt", "2.txt", "25.txt", "3.txt"]
##
##list_difect = []
##list_info = []
##
##for h in ww_list:
##        r = open(h)
##        print(r.read())






##import sys
##
##ww_list = ["1.txt", "2.txt", "25.txt", "3.txt"]
##
##list_difect = []
##list_info = []
##
##for h in ww_list:
##        try:
##                r = open(h)
##                list_info.append(r.read())
##                print("bor")
##        except Exception:
##                list_difect.append(h)
##                print("yo'q")
##                continue









##import sys
##
##ww_list = ["1.txt", "2.txt", "25.txt", "3.txt"]
##
##list_difect = []
##list_info = []
##
##try:
##        for h in ww_list:
##                try:
##                        r = open(h)
##                        list_info.append(r.read())
##                        print("bor")
##                except Exception:
##                        list_difect.append(h)
##                        print("yo'q")
##                        sys.exit()
##                        continue
##
##finally:
##        r = open("save.txt", "a")
##        for i in list_info:
##                r.write(i)
##        r.write(str(list_difect))
##        r.close()
##        print("men aynan qaysini zabis qilay")










import sys

ww_list = ["1.txt", "2.txt", "25.txt", "3.txt"]

list_difect = []
list_info = []

try:
        for h in ww_list:
                try:
                        r = open(h)
                        list_info.append(r.read())
                        print("bor")
                except Exception:
                        list_difect.append(h)
                        print("yo'q")
                        continue

finally:
        r = open("save.txt", "a")
        for i in list_info:
                r.write(i)
        r.write(str(list_difect))
        r.close()
        print("men aynan qaysini zabis qilay")








