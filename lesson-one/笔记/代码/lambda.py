square1 = lambda n: n * n

def square2(n):
    return n * n

print(square1(2))
print(square2(2))

revenue = [('1月', 5610000), ('2月', 4850000), ('3月', 6220000)]
key = lambda x: x[1]
for r in revenue:
    print(key(r))
print(key([1, 2]))
print(key('abcd'))

plus = lambda x, y, z: x + y + z
# print(plus(2, 6))
# print(plus('a', 'b'))
print(plus(1, 2, 3))
revenue = [('1季度', (5610000, 5710000, 5810000)),
           ('2季度', (4850000, 4850000, 4850000)),
           ('3季度', (6220000, 6320000, 6420000))]
revenue.sort(reverse=True, key=lambda x: sum(x[1]))
print(revenue)
