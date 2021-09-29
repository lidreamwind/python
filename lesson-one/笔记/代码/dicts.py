top_sales = [('Tony', 284), ('Mike', 280), ('John', 253), ('Peter', 213), ('Henry', 205)]
# 两种定义字典的方式
sales = {
    'Tony': 284,
    'Mike': 280,
    'John': 253,
    'Peter': 213,
    'Henry': 205,
}
sales = dict(top_sales)
print(sales)
print(sales['Mike'])
# 添加数据
sales['mike'] = 0
print(sales['mike'])
# 修改数据
sales['mike'] = 300
print(sales)
# 删除
del sales['mike']
print(sales)

# 重点：使用for 循环迭代字典
for key, value in sales.items():
    print(key, value)

# print(sales['mike'])
print(sales.get('mike', 0))
# 相当于下面的写法
if 'mike' in sales:
    print(sales['mike'])
else:
    print('mike', 0)

print(sales.keys())
print(sum(sales.values()))