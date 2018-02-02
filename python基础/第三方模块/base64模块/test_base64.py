# -*- coding: utf-8 -*-

"""
base64是一个将二进制数据编码到可打印的ascii码字符，而且还可以将这些编码解码到原来的二进制数据
它为RFC 3548中指定的编码提供编码和解码功能，RFC 3548定义了Base16、Base32和Base64算法。

不是一种安全算法，只是一种编码算法

"""
import base64

encoded = base64.b64encode("123".encode('utf-8'))
# print(encoded)
# print(encoded.decode('utf-8'))
encoded = encoded.decode('utf-8')
data = base64.b64decode(encoded.encode('utf-8'))
print(data.decode('utf-8'))

print("\033[34;1m欢迎进入CLASS_SYSTEM系统\n"
      "1 讲师视图\n"
      "2 学生视图\n"
      "q 退出管理系统\n\033[0m")

# base64的意义在于哪里呢？
#由于某些系统中只能使用ASCII字符。Base64就是用来将非ASCII字符的数据转换成ASCII字符的一种方法

# 我们知道在计算机中任何数据都是按ascii码存储的，而ascii码的128～255
# 之间的值是不可见字符。而在网络上交换数据时，比如说从A地传到B地，
# 往往要经过多个路由设备，由于不同的设备对字符的处理方式有一些不同，
# 这样那些不可见字符就有可能被处理错误，这是不利于传输的。
# 所以就先把数据先做一个Base64编码，统统变成可见字符，这样出错的可能性就大降低了。
#
#
#
#
# 如一个xml当中包含另一个xml数据，此时如果将xml数据直接写入显然不合适，
# 将xml进行适当编码存入较为方便，事实上xml当中的字符一般都是可见字符（0 - 127
# 之间），但是由于中文的存在，可能存在不可见字符，
# 直接将字符打印在外层xml的数据中显然不合理，那么怎么办呢？
# 可以使用base64进行编码，然后存入xml，解码反之