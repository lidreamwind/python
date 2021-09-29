# 元组的定义
t = tuple('python')
t = ('p', 'y', 't', 'h', 'o', 'n')
t = ('My', 'age', 'is', 18)
t = 'My', 'age', 'is', 18
t = 'Solo',
print(t)
# print(t[0], t[2], t[-1])
# print(t[:2])
# 元组是不可变序列
t = ('My', 'age', 'is', '18')
print("+".join(t))

t = ('a', 'b', 'b', 'a')
print(t.count('a'))
print(t.index('b'))
# print(t.index('notexists'))

t = tuple(range(10000))
print(len(t), t[0], t[-1])

print(8888 in t)
print(10000 in t)

t = ('a', 'b', 'c', 'd', 'e')
# for i in t:
#     print(i)

i = 0
while i < len(t):
    print(t[i])
    i += 1