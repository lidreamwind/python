def hello(name):
    print("Hello", name)

hello('python')
hello('world')


def hello2(name='Anonym', sex='女'):
    if sex == '男':
        print("Hello, Mr", name)
    elif sex == '女':
        print("Hello, Mrs", name)

hello2('Zhang', '男')
hello2('Wang', '女')
hello2(sex="男", name="Li")
hello2(name='Zhong')
hello2()


def multiply(num1, num2):
    return num1 * num2
print(multiply(2, 4))


def permit(age):
    if age >= 18:
        print("准许进入")
        return True
    else:
        print("禁止进入")
        return False
    print("end")
permit(18)
permit(17)
permit(28)

def do_nothing():
    pass

print(do_nothing())
if not do_nothing():
    print('....')


def find_min_max(nums):
    nums.sort()
    return nums[0], nums[-1]

min, max = find_min_max([2, 3, 5, 6, 1, 4])
print(min, max)
