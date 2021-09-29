sales = (
    ("Peter", (78, 70, 65)),
    ("John", (88, 80, 85)),
    ("Tony", (90, 99, 95)),
    ("Henry", (80, 70, 55)),
    ("Mike", (95, 90, 95)),
)
champion = ''
max_amount = 0
for name, quarter_amount in sales:
    total_amount = sum(quarter_amount)
    if total_amount > max_amount:
        champion, max_amount = name, total_amount
print("第一季度的销售冠军是%s, TA的总销售额是%d万元" % (champion, max_amount))
