
class Goods:
    def func(self):
        pass
    # 定义属性
    @property
    def price(self):
        return 10
# ############### 调用 ###############
obj = Goods()

obj.func()
print(obj.price)  #调用属性
