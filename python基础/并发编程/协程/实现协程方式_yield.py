import time


def A():
    print("第一次由B调到A")
    while True:
        print('------A-----')
        time.sleep(0.1)
        yield
        print("由B返回A")


def B(a):
    for i in range(3):
        print("此时B i = %d" % i)
        time.sleep(0.1)
        next(a) # 生成器一遇到next就会执行a函数的代码，A函数在yield处保存，从A函数并返回到此次
        # 从A函数返回B,接着往下执行
        # 在B函数循环里面再次遇到next(a),又从B调到A上次保存的地方，接着执行
        print('由A返回B')


a = A()
B(a)
# 结果应该是：
# ------B-----
#
# yield的缺点：不能监听到什么时候出现IO操作
# greenlet，可以检测到io操作（sleep),执行.switch会切换线程（需要手工切换）