
# 首先是两重嵌套的装饰器

    # step1 装饰器定义
    def log(func):
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper
    
  
     # step2 使用log装饰器
         @log
        def now():
            print '2013-12-25'
            
     # step3 调用Now()函数
        now()
        
     # step4 调用now函数，不仅仅会运行Now函数，还回在之前打印一条日志：call now()
        上面的now()等效于now = log(now)， 然后再Now()
        
        # 
 
 
 # 如果装饰器需要一个参数比如@log('execute'), 则必须定义三重装饰器
 
    # step1 三重装饰器定义
         def log(text):
            def decorator(func):
                def wrapper(*args, **kw):
                    print '%s %s():' % (text, func.__name__)
                    return func(*args, **kw)
                return wrapper
            return decorator
        
    # step2 使用装饰器
        @log('execute')
        def now():
            print '2013-12-25'
            
    # step3 调用Now()函数
         now()
    
    # step4 上面的now()等效
        now = log('execute')(now)， 等效为 now = decorator(now), decorator里面的text参数为execute 然后再now()
    

# 页面缓存的三重嵌套的装饰器
        
    _model_data_cahce_signals_methods = []

    def model_data_cache_method(model_class):   # model_class 是表名
        def decorator(method):
            def get_data_method():
                key = _build_model_cachekey(method, model_class)
                data = cache.get(key)
                if data is None:
                    data = method()
                    cache.set(key, data)
                return data

            def callback_for_method(sender, instance, **kwargs):
                key = _build_model_cachekey(method, model_class)
                cache.delete(key)

            _model_data_cahce_signals_methods.append(callback_for_method)

            signals.post_save.connect(callback_for_method, sender=model_class)
            signals.post_delete.connect(callback_for_method, sender=model_class)

            return get_data_method
        return decorator
        
    
 # 用法
     @model_data_cache_method(Profile)
    def user_info(user=None):
        profile = Profile.objects.all().filter(member=user).select_related('personal_info').prefetch_related('company','wuser')
        return profile
