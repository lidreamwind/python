sales = (
    ("Peter", (78, 70, 65)),
    ("John", (88, 80, 85)),
    ("Tony", (90, 99, 95)),
    ("Henry", (80, 70, 55)),
    ("Mike", (95, 90, 95)),
)
# for循环写法
top_sales = []
for name, quarter_amount in sales:
    total_amount = sum(quarter_amount)
    top_sales.append((name, total_amount))
# 列表表达示写法，不要求大家能够直接写出来
top_sales = [(name, sum(quarter_amount)) for name, quarter_amount in sales]
top_sales.sort(reverse=True, key=lambda x: x[1])
print(top_sales)
