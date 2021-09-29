lst = list()
lst = []
lst = [1, 2, 3, 4]
lst = ["a", 1, 2, 3.14, (1,2,3,)]
lst = list('abcd')
lst = list(range(100))
lst = list((1,2,3))
print(lst)
lst = ['a', 'b', 'c', 'd', 'e']
print(lst[0], lst[-1])
print(lst[1:3])
lst.append('f')
print(lst)

print(len(lst))

lst[0] = 'A'
lst[-1] = 'F'
print(lst)

del lst[0]
del lst[-1]
print(lst)

lst = ['a', 'b', 'c', 'd', 'e']
lst.insert(0, 'A')
lst.insert(2, 'B')
lst.insert(-1, 'E')
print(lst)

lst.pop()
last = lst.pop()
print(lst, last)
while lst:
    print(lst.pop())
print(lst)

lst = ['a', 'b', 'c', 'd', 'e']
temp = lst.pop(2)
print(temp, lst)

lst = ['a', 'b', 'c', 'd', 'e', 'c']
lst.remove('c')
lst.remove('c')
print(lst)
lst.clear()
print(lst)

# extend append
lst.append('a')
print(lst)
lst.extend(['b', 'c', 'd'])
print(lst)

lst.reverse()
print(lst)

lst = [3, 5, 1, 2, 4]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
# ASCII 0~9 , A~Z, a~z，每个字符对应一个数字。
# ord, chr 可以将字符与ASCII值相互转换。
lst = ['apple', 'banana', 'orange', 'blueberry']
lst.sort()
print(lst)

revenue = [('1月', 5610000), ('2月', 4850000), ('3月', 6220000)]
revenue.sort(reverse=True)
print(revenue)

# key参数，使用每个元素的第二个索引作为排序依据
revenue.sort(reverse=True, key=lambda x: x[1])
print(revenue)

# copy函数
lst1 = [1, 2, 3]
lst2 = lst1
lst1.append(4)
print(lst1, lst2)

lst3 = lst1.copy()
lst1.append(5)
print(lst1, lst3)

# 列表表达式
lst = list(range(20))
lst = [i for i in range(20) if i % 2 == 0]
print(lst)
lst = [i * 2 for i in range(10)]
print(lst)
lst = [i for i in range(0, 20, 2)]
print(lst)
lst = []
for i in range(0, 20, 2):
    lst.append(i)
print(lst)

# 打印出26个大写字母
a_z = [chr(i) for i in range(65, 65 + 26)]
print(a_z)