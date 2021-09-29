# 123456
# 043107501464723123456877420404570415055430

password = '123'
while True:
    pwd = input("请设置您的密码：\n")
    if not pwd:
        break
    confirm_pwd = input("请再次输入您的密码:\n")
    if pwd == confirm_pwd:
        password = pwd
        break
    print("您两次输入的密码不致，请重新输入")
print("您的初始密码已设置为：", password)

print("进入开锁程序")
failed_time = 0
while True:
    input_pwd = input("请输入您的密码：\n")
    if password in input_pwd:
        print("开锁成功")
        break
    else:
        failed_time += 1
        if failed_time >= 3:
            print("输入错误超过3次，请联系主人")
            break
        print("您输入的密码有误，请重新输入")
