##a = "Lets write a string 'as' s"
##
##print(a)
##a = 'Let\'s write a string as "s"'
##
##print(a)
##
##
##a = 'Lets \
##write a \
##string as s'
##print(a)
##
##
##a = 'Let\'s write a string as s'
##
##print(a)
##
##l = 'https:\www.youtube.com\new'
##
##print(l)
##
##
##
##d = 'https:\www.youtube.com\\new'
##
##print(d)
##
##
##d = r'https:\www.youtube.com\new'
##
##print(d)
##
##
##
####os.walk('D:\')
##
##
##
####os.walk('D:\\')
##
##
##
####os.walk(r'D:\')
##
##
##
##
##d = 'https:\\www.youtube.com\\new'
##
##print(d)
##
##
##
##
##d = 'https:/www.youtube.com/new'
##
##print(d)
##
##
##
##
##
##
##b = 'stroka text'
##
##print('str' in b)
##
##
##
##b = 'stroka text'
##
##print('sto' in b)
##
##
##
##b = 'sTROKA TEXT'
##
##print(b.capitalize())
##
##path = 'C:/Users/PyHS/Destop/s.py'
##path1 = path.replace('/', '\\')
##print(path1)
##
##
##
##
##path = 'C:/Users/PyHS/Destop/s.py'
##path1 = path.replace('/', '\\')
##r = path1.split('\\')
##print(r)
##
##
##r = path1.split('\\')
##print(r[-1])
##
##
##r = open('23.txt')
##u = r.read()
##list_znk = ['(',')','"','"']
##for i in list_znk:
##        u = u.replace(i, '')
##        
##print(u)
##
##
##print(path1)
##
##
##
##r = path1.split('\\')
##print(r)
##
##
##r = path1.split('\\')
##print(r[-1])
##
##
##r = open('23.txt')
##u = r.read()
##list_znk = ['(',')','"','"']
##for i in list_znk:
##        u = u.replace(i, '')
##        
##print(u)













r = open('23.txt')
u = r.read()
list_znk = ['(',')','"','"', '\n']
for i in list_znk:
        u = u.replace(i, '')
        
print(u)


u2 = u.split()
print(u2)


new_text = ' '.join(u2)
print(new_text)



new_text = '_*_'.join(u2)
print(new_text)






a = input("Dastur yopilishi uchun Enterni bosing: \n")



