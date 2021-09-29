# 商品：名称、价格、折扣率
# 购物车：商品，商品的数量

class Goods:
    """商品类"""

    id_count = 0

    # 类方法
    # 装饰器写法，classmethod用来定义类方法
    @classmethod
    def generate_id(cls):
        cls.id_count += 1
        return cls.id_count

    def __init__(self, name, price, discount=1):
        # 商品唯一序号, 00001, 02738
        self.id = str(self.generate_id()).zfill(5)
        self.name = name
        self.price = price
        self.discount = discount

    def calc_price(self):
        """计算商品打折后的实际价格"""
        return self.price * self.discount


class Cart:
    """购物车"""
    def __init__(self):
        self.cart = {}
        self.goods_list = []

    def add(self, goods, num=1):
        """向购物车内添加商品"""
        if goods in self.goods_list:
            self.cart[goods.id] += num
        else:
            self.goods_list.append(goods)
            self.cart[goods.id] = num

    def remove(self, goods, num):
        """从购物车中减少或者删除商品"""
        if goods not in self.goods_list:
            return
        self.cart[goods.id] -= num
        if self.cart[goods.id] <= 0:
            del self.cart[goods.id]
            self.goods_list.remove(goods)

    def get_goods_by_id(self, id):
        """根据商品ID找到商品"""
        for goods in self.goods_list:
            if id == goods.id:
                return goods

    def get_total_amount(self):
        """获取当前购物车中的总价"""
        amount = 0
        for id, num in self.cart.items():
            goods = self.get_goods_by_id(id)
            amount += goods.price * num
        return amount

    def get_pay_amount(self):
        """获取实际需要支付的总价"""
        amount = 0
        for id, num in self.cart.items():
            goods = self.get_goods_by_id(id)
            amount += goods.calc_price() * num
        return amount

    def show(self):
        title = ('商品', '单价', '数量', '价格（元）')
        def show_row(row):
            """内部函数，显示购物车中的每一行"""
            for col in row:
                print(str(col).ljust(12), end="\t")
            print()
        show_row(title)
        for id, num in self.cart.items():
            goods = self.get_goods_by_id(id)
            price = '%.2f' % goods.price
            if goods.discount < 1:
                price = '%.2f(%d折)' % (goods.price, goods.discount * 10)
            show_row((goods.name, price, num, '%.2f' % (goods.calc_price() * num)))
        total_amount = self.get_total_amount()
        pay_amount = self.get_pay_amount()
        discount_amount = total_amount - pay_amount
        show_row(('', '', '', "总金额：%.2f" % total_amount))
        if discount_amount > 0:
            show_row(('', '', '', '优惠了：%.2f' % discount_amount))
        show_row(('', '', '', "实付金额：%.2f" % pay_amount))


g1 = Goods('iPhone11', 6000, 0.9)
g2 = Goods('U盘32', 100, 0.8)
g3 = Goods('华为P40', 5000)

# print(g1.name, g2.name, g3.name)
# print(g1.price, g1.calc_price())
cart = Cart()
cart.add(g1)
cart.add(g2, 3)
cart.add(g3, 2)
cart.show()

cart.remove(g2, 1)
cart.show()

g1.price = 5000
cart.show()