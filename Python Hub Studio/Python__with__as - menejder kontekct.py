r = open('file.txt', 'a')
r.write('somthing' + '\n')
10/0
r.write('nima')
r.close()

print('Hammasi joyda')





r = open('file.txt', 'a')
try:
        r.write('somthing' + '\n')
        10/0
        r.write('nima')
finally:
        r.close()

print('Hammasi joyda')






with open('file.txt', 'a') as r:
        r.write('somthing' + '\n')
        10/0
        r.write('nima')
##r.close()

print('Hammasi joyda')
