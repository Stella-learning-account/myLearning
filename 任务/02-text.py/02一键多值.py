#encoding=utf-8

print ('中国')

#字典的一键多值

print('方案一 list作为dict的值 值允许重复'  )

d1={}
key=1
value=2
d1.setdefault(key,[]).append(value)
value=2
d1.setdefault(key,[]).append(value)

print( d1)

#获取值
print ('方案一 获取值')
print (list(d1[key]))

print ('方案一 删除值，会留下一个空列表')
d1[key].remove(value)
d1[key].remove(value)
print( d1 )

print ('方案一 检查是否还有一个值')
print (d1.get(key,[]))

print ('方案二 使用子字典作为dict的值 值不允许重复')

d1={}
key=1
keyin=2
value=11
d1.setdefault(key,{})[keyin]=value
keyin=2
value=22
d1.setdefault(key,{})[keyin]=value
keyin=3
value=33
d1.setdefault(key,{})[keyin]=value

print (d1)

print( '方案二 获取值')
print( list(d1[key]))

print( '方案二 删除值，会留下一个空列表')
del d1[key][keyin]
keyin=2
del d1[key][keyin]
print( d1)

print( '方案二 检查是否还有一个值')
print (d1.get(key,()))

print ('方案三 使用set作为dict的值 值不允许重复')
d1={}
key=1
value=2
d1.setdefault(key,set()).add(value)
value=2
d1.setdefault(key,set()).add(value)
value=3
d1.setdefault(key,set()).add(value)

print( d1)

print( '方案三 获取值')
print( list(d1[key]))

print( '方案三 删除值，会留下一个空列表')
d1[key].remove(value)
value=2
d1[key].remove(value)
print( d1 )

print( '方案三 检查是否还有一个值')
print( d1.get(key,()))
