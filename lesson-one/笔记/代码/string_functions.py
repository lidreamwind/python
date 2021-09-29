# print("   A\tB\tC\nD\tE\tF    ")
# strip函数：去除首尾的特殊空白字符
password = '123'
input_password = ' 123 '
print(password == input_password.strip())
print('\nabc\t'.rstrip())

# 大小写操作
print('china'.upper())      # 大写
print("CHINA".lower())      # 小写
print("china".capitalize()) # 首字大写
print('i have a dream'.title()) # 每个单词的首字母大写

# 字符串判断
print("China".islower())
print("CHINA".isupper())
print("123456a".isdigit())
print("china".startswith('c'))
print("-2423333".startswith('-'))

# 查找字符串
password = '123'
input_password = '456123789'
print(input_password.find(password))
print(input_password.index(password))

# count ，数字符串的个数
b = 'banana'
print(b.count('a'))
print(b.count('n'))

# 替换 replace
print("abba".replace('a', 'b'))
print("apple orange".replace('apple', 'orange'))

# 字符串长度
print(len('china'))
print(len(''))
print(len('a'))


