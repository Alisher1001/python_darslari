import os


while True:
    sayt = input("Veb-sayt manzilini kiriting\n")
    
    if sayt == "yopilsin":
        break
    
    if "https://" in sayt:
        os.system('start ' + sayt)
        print('if')

    elif "www. " in sayt:
        sayt = "https://" + sayt
        os.system('start ' + sayt)
        print("elif")

    else:
        sayt = "https://www." + sayt
        os.system("start " + sayt)
        print("else")



##a = input("Dasturni yopish uchun Enterni bosing: \n")
