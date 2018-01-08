# step5 设置xadmin后台的中文，和当地时区

LANGUAGE_CODE ="zh-hans"  # 1.8之后该
TIME_ZONE = "Asia/Shanghai"
USE_I18N = True
USE_L10N = True
USE_TZ = False  # 这个一定要改成False, 否则数据库的时间就是国际时间，UTC时间