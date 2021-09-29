s = "CHINA"
s[0]    # 第一个字符
s[-1]   # 最后一个字符
s[-2]

s[0:3]  # CHI
s[:3]   # CHI

# 取出整个字符串
s[0:5]
s[0:]
s[:]
# 从第三个到末尾
s[2:]
# 从头到尾每隔两个字符取一个
print(s[::2])
print("abcdefghijklmn"[8:16:2])
print(s[::-2])


