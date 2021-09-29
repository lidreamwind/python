# num = 10000
#
# if num % 2 == 0:
#     print(num, "是一个偶数")
# else:
#     print(num, "是一个奇数")
#
# print("程序结束")


# score = 90
# # 60以下 不及格
# # 60~90  合格
# # 90以上  优秀
# if score < 60:
#     print("您的成绩不及格")
# elif score <= 90:
#     print("您的成绩合格")
# else:
#     print("您的成绩优秀")

# 60以下 不及格
# 60~70  合格
# 70~90  良好
# 90以上  优秀
# if score >= 60:
#     if score < 70:
#         print("您的成绩合格")
#     elif score < 90:
#         print("您的成绩良好")
#     else:
#         print("您的成绩优秀")
# else:
#     print("您的成绩不及格")

# age = 18
# # if age >= 18 and age < 60:
# if 18 <= age < 60:
#     print("你已经不是个孩子啦，赶紧去工作吧")
# else:
#     print("你还是个孩子")

# count = 1
# if 2 - 1:
#     print("条件成立")
# else:
#     print("条件不成立")

# 0, None, 空字符串转换为布尔值后为False
result = "123"
# if result == None:
if result:
    print("获取数据成功")
    pass
else:
    print("什么收获都没有")
