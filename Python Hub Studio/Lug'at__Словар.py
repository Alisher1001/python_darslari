d1 = {"a":7}
d2 = dict(a=7)
d3 = dict.fromkeys([1,2,3,4,5], 'olma')

price = {"meat": 3, "bread": 1, "potato": 0.5, "water": 0.2}

users = {
    "Alex21": {"password": 4567345, "id": 1542},
    "Jimmy55": {"password": 9878965, "id": 8764},
    "Bob33": {"password": 1265398, "id": 4927}
}




price1 = {
     "meat": 3, "bread": 1, "potato": 0.5, "water": 0.2,
     "meat 2": 6, "bread 2": 2, "potato 2": 1, "water 2": 0.4,
     "meat 3": 9, "bread 3": 3, "potato 3": 1.5, "water 3": 0.6,
     "meat 4": 12, "bread 4": 4, "potato 4": 2, "water 4": 0.8,
     "meat 5": 15, "bread 5": 5, "potato 5": 2.5, "water 5": 1,
     "meat 6": 18, "bread 6": 6, "potato 6": 3, "water 6": 1.2,
     "meat 7": 21, "bread 7": 7, "potato 7": 3.5, "water 7": 1.4,
     "meat 8": 24, "bread 8": 8, "potato 8": 4, "water 8": 1.6,
     "meat 9": 27, "bread 9": 9, "potato 9": 4.5, "water 9": 1.8
 }




def buy():
    pay = 0
    while True:
        enter = input("Nima sotib olasiz???\n")
        if enter == "end":
            break
        pay += price[enter]
    return pay





d1 = {"a":7}
d2 = dict([[1,2], [3,4], [5,6]])
d3 = dict.fromkeys([1,2,3,4,5], 'olma')

d5 = d1.copy()
print(d5)
print(d1.items())
print(d1.keys())
print(d1.values())
d1.update(d2)
print(d1)
t = d1.pop("a")
print(t, d1)









price1 = {"1": 3, "2": 1, "3": 0.5, "4": 0.2}

def buy():
    pay = 0
    while True:
        enter = str(input("Nima sotib olasiz???\n"))
        if enter == "=":
            break
        pay += price1[enter]
    return pay










price1 = {"1": 3, "2": 1, "3": 0.5, "4": 0.2}
foo = 100
def buy():
    pay = 0
    while True:
        enter = input("Nima sotib olasiz???\n")
        if enter == "=":
            break
        pay += price1[enter]
        dar = price1[enter]
        bar = foo - dar
        print(bar)

    return pay



















a = input("Dastur yopilishi uchun Enterni bosing: \n")
