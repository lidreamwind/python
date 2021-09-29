# 11位
# 13 15 17 18 19
# 区号+电话号码  010， 0888 + 8位=11位或12位
# 400电话：400开头，10位
# 当用户输入exit的时候，程序退出

cellphone_number_start = "13 15 17 18 19"
telephone_number_start = "010 021 022 025 0888 0555"
# 13812345678

while True:
    num = input("请输入一个电话号码：\n")
    if num.strip() == 'exit':
        break
    if not num:
        print("电话号码不能为空")
        continue
    num = num.strip()
    if not num.isdigit():
        print("您输入的是一个无效电话号码")
        continue
    if num[:2] in cellphone_number_start and len(num) == 11:
        print("这是一个手机号码")
        continue
    if num.startswith('0'):
        # 01088888888
        # 088812345678
        if (len(num) == 12 and num[:4] in telephone_number_start) or \
                (len(num) == 11 and num[:3] in telephone_number_start):
            print("这是固定电话号码")
            continue
    if num.startswith('400') and len(num) == 10:
        print("这是一个广告电话")
        continue
    print("无法识别该号码")