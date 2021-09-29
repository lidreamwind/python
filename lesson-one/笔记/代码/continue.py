# 1+3+5+7+9=?
total = 0
max = 20
for i in range(max):
    if i % 2 == 0:
        continue
    # 能够执行到这里的都是奇数
    total += i
    # total = total + i
    print(i, end="")
    if i == max - 1:
        continue
    print(" + ", end="")
print(' =', total)