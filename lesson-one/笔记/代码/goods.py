class Goods:
    id_count = 0

    # 类方法
    # 装饰器写法，classmethod用来定义类方法
    @classmethod
    def generate_id(cls):
        cls.id_count += 1
        return cls.id_count

    def __init__(self):
        # 商品唯一序号, 00001, 02738
        self.id = str(self.generate_id()).zfill(5)
        self.name = ''
        self.price = 0
        self.discount = 1


g1 = Goods()
print(g1.id)
g2 = Goods()
print(g2.id)
g3 = Goods()
print(g3.id)

for _ in range(10):
    g = Goods()
    print(g.id)

print(Goods.id_count)