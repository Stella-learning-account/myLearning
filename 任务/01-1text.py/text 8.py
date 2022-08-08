
a = [','.join(['a','q','w']).replace(',', '，')]
b = ['123']
d = ['r']
lis = []
c = '|'.join(a+b+d)
lis.append(c)
print(c)
print(lis)
print(len(c.split('，')))

f = ['']
print(b+f)
if f[0]=='':
    print('//////')


# d = {}
# d.setdefault('导演',[]).append('')
# print(d)

u = []
# if len(u) == 0:
#     u.append('空')
# print(u)

list = [u, a, b]
# print(list)
# for i in list:
#     if len(i)==0:
#         i.append('empty')
# print(list)
# print(u)

lit = ['e','t']
df = [1,2,3,'yu']
lit.extend(df)
print(lit)