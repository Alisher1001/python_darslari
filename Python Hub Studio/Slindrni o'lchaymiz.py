import math

PI = math.pi

def radius():
    n = float(input("Diametr silindir: \n"))
    n /= 2
    return n

def heihgt():
    m = float(input("Chuqurlik silindir: \n"))
    return m


def volume():
    r = radius()
    h = heihgt()
    s = PI*r**2
    v = s*h
    
    return v


print("Hajmi silindir", volume(), "sm3")


def massa(g):
        n = float(input("Ummumiy og'irlik g/sm3: \n"))
        return g*n/1000
print("Silingrning og'irlikgi kg: ", massa(volume()))









a = input("Dastur yopilishi uchun Enterni bosing: \n")