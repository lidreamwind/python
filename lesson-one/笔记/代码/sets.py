nums = {1, 2, 3, 4, 5}
print(nums)

lst = [1, 2, 3, 1, 3, 4]
nums = set(lst)
print(nums)
t = ('a', 'b', 'a', 'c')
print(set(t))
print(list(nums))
print(tuple(nums))

for n in nums:
    print(n)

print('nums的长度：', len(nums))
print(5 in nums)
nums.add(5)
print(5 in nums)
nums.add(5)
print(nums)

nums.remove(5)
print(nums)
# nums.remove(5)
nums.discard(5)

# while len(nums) > 0:
while nums:
    num = nums.pop()
    print(num)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5}
# 求交集
print(s1.intersection(s2))
# 求并集
s3 = s1.union(s2)
# 判断是否是子集
print(s1.issubset(s3))
# 判断是否是父集
print(s3.issuperset(s2))