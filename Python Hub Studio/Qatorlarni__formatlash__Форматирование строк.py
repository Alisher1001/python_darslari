enter = input('Your name: ')

a = 'Hello %a' % enter

print(a)



enter = input('Your name: ')

a = 'Hello %a, I am %a' % (enter, 'Python')

print(a)



enter = input('Your name: ')

a1 = 'Hello {}, I am {}'.format(enter, 'Python')

print(a1)




enter = input('Your name: ')

a1 = 'Hello {1}, I am {0}'.format(enter, 'Python')

print(a1)




enter = input('Your name: ')

a2 = f'Hello {enter}, I can do it in f-string {2+2}'

print(a2)


var = 'stroka'

enter = input('Your name: ')

a2 = f'Hello {enter}, I can do it in f-string {len(var)}'

print(a2)







a = input("Dastur topilishi uchun Enterni bosing: \n")
