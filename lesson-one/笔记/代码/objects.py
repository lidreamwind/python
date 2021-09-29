# object
# 品种、颜色、体型大小
# 吃东西、奔跑、吠叫

# 类
class Dog:
    # 构造函数，初始化函数
    def __init__(self, breed, color, size='大'):
        self.breed = breed
        self.color = color
        self.size = size
    def eat(self):
        print("I like bones")
    def run(self):
        print("I'll catch you.")
    def bark(self):
        """一只狗的自我介绍"""
        print('Wang! Wang!')
        print("一只%s型%s色的%s" % (self.size, self.color, self.breed))


# 类是创建对象的模板，对象是类的实例
dog = Dog("哈士奇", '黑白', '中')
dog.size = '小'
dog.eat()
dog.run()
dog.bark()
# dog.breed = '哈士奇'
# dog.color = '黑白'
# dog.size = '大'

dog2 = Dog('金毛犬', '金')
dog2.bark()

#
# dog1, dog2 = Dog(), Dog()
# #type函数可以查看任何对象的类型
# print(type(dog))
#
# print(type(1) == int)
# print(type('abc') == str)
# print(type(dog) == Dog)
#
# # isinstance
# print(isinstance(dog, Dog))
# print(isinstance(1, int))
# print(isinstance([], list))