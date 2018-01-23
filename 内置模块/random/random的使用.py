# random.choice

a = [ str(random.choice(range(0,10)) for i in range(num) ]  # 生成列表，列表元素个数为num, 列表元素值为0-9的随机数

verify_code = ''.join(a)  # 将列表转换成字符串，前提是列表的元素是字符？

def generate_code(num,mobile):
        veri_code = ''.join([ str(random.choice(range(0,10))) for i in range(num) ])
        cache.set(mobile,veri_code,timeout=3600)
        return veri_code
		
		
# random.sample

random.sample("0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 8) # 从字符串中随机选择8个字符，生成列表

username =  lambda : ''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/",8))

username =  lambda num: ''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-><:}{?/", num))


# random.randrange([start], stop, [step])
random.randrange(100,200,1) # 输出100-200的随机数， 
random.randrange(100,200,2) # 输出100-200的随机一个偶数