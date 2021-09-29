seq = "hello"
for i in seq:
    print(i)

for i in range(5):
    print(i)

for lap in range(10):
    print("我跑完了第" + str(lap + 1) + "圈")
print("跑步结束")

width, height = 10, 5
# **********
# **********
# **********
# **********
# **********
for _ in range(height):
    for i in range(width):
        print("*", end="")
    print()
# *
# **
# ***
# ****
# *****
for i in range(9):
    for _ in range(i+1):
        print("*", end="")
    print()

# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j) + "*" + str(i) + "=" + str(i * j), end=" ")
    print()
