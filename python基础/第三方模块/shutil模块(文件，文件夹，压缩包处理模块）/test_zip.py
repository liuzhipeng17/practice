# -*- coding: utf-8 -*-

# shutil.make_archive(base_name, format,...)
#
# 创建压缩包并返回文件路径，例如：zip、tar

# •base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
# 如：www                        =>保存至当前路径
# 如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
# •format： 压缩包种类，“zip”, “tar”, “bztar”，“gztar”
# •root_dir： 要压缩的文件夹路径（默认当前目录）
# •owner： 用户，默认当前用户
# •group： 组，默认当前组
# •logger： 用于记录日志，通常是logging.Logger对象


# 将 /Users/wupeiqi/Downloads/tests 下的文件打包放置当前程序目录
import shutil
ret = shutil.make_archive("22", 'gztar', root_dir='/Users/wupeiqi/Downloads/tests')



# 将 /Users/wupeiqi/Downloads/tests 下的文件打包放置当前目录
import shutil
ret = shutil.make_archive("/Users/wupeiqi/wwwwwwwwww", 'gztar', root_dir='/Users/wupeiqi/Downloads/tests')

