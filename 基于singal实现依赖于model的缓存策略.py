# 通过Signal实现依赖于Model的缓存策略

"""

    https://www.jianshu.com/p/9ea88e2d2394

    如果有一种方法能够在数据库中的数据变更时，
    及时的通知到我们，这样我们就可以在数据变动时手动调用cache.delete()方法来清除缓存，
    从而即能够保证页面的实时性，又能够获得最大的缓存利用率。

    django.db.models.signals.pre_save：当Model调用save()方法进行数据保存前发出的信号。
    django.db.models.signals.post_save：当Model调用save()方法进行数据保存后发出的信号。
    django.db.models.signals.pre_delete：当Model调用delete()方法删除数据前发出的信号。
    django.db.models.signals.post_delete：当Model调用delete()方法删除数据后发出的信号。
    django.db.models.signals.m2m_changed：当Model的ManyToManyField字段发生变更时发出的信号。

    通过这些信号，我们就可以获知数据变更的通知，
    进而调用cache.delete()方法及时的清理无效的缓存，从而达到即保证页面了的实时性，又能够获得最大的缓存利用率

"""

# step1 先简单介绍怎么使用signal
    # 先声明一个方法，用于接受信号后执行的操作
    def my_callback(sender, instance, **kwargs):
        """
        :param sender:保存的Model类。
        :param instance:保存的Model的实例。
        """
        print("%s保存完成！" % instance)

    # 导入信号
    from django.db.models.signals import post_save

    # 连接信号
    post_save.connect(my_callback, sender=Model)    # sender参数用于只接收指定的Model类的post_save信号

# step2 怎么使用cache
    # 导入缓存模块
    from django.core.cache import cache

    # 设置缓存数据 set(key, value, timeout)
    cache.set('my_key', 'hello, world!', 30)

    # 获取缓存数据get(key)
    cache.get('my_key')

    # 删除缓存delete()
    cache.delete('my_key')

# step3 实现一个简单的依赖于model的缓存方法

    # 假设我们有以下Model类
        class Info(models.Model):
            title = models.CharField(max_length=256, verbose_name=_('标题'))
        
    # 实现一个依赖于整个模型所有实例的缓存

        # 声明一个获取数据的原始方法
        def _get_info_top10_list():
            qs = Info.objects.all()[:10]
            return list(qs)

        # 声明一个缓存键值
        CACHE_KEY_INFO_TOP10_LIST = “info_top10_list”

        # 声明一个从缓存获取数据的方法
        def get_info_top10_list():
            data = cache.get(CACHE_KEY_INFO_TOP10_LIST)
            if data is None:
                data = _get_info_top10_list()
                cache.set(CACHE_KEY_INFO_TOP10_LIST, data)
            return data

        # 声明一个监听Model数据保存删除的回调，用以更新缓存
        def callback_for_info_top10_list(sender, instance, **kwargs)
            cache.delete(CACHE_KEY_INFO_TOP10_LIST)

        # 连接信号，以触发缓存更新
        post_save.connect(callback_for_info_top10_list, sender=Info)
        post_delete.connect(callback_for_info_top10_list, sender=Info


 # step4 再实现一个依赖于模型单个实例的缓存

    # 声明一个获取数据的原始方法
    def _get_info (info_id):
        try:
            info = Info.objects.get(pk=info_id)
        except Info.ObjectDoesNotExist:
            info = None
        return info

    # 声明一个构建缓存键的方法
    def build_cachekey_info(info_id):
        return ‘info_%s’ % info_id

    # 声明一个从缓存获取数据的方法
    def get_info(info_id):
        key = build_cachekey_info(info_id)
        data = cache.get(key)
        if data is None:
            data = _get_info(info_id)
            cache.set(key, data)
        return data

    # 声明一个监听Model数据保存删除的回调，用以更新缓存
    def callback_for_info(sender, instance, **kwargs)
        key = build_cachekey_info(instance.pk)
        cache.delete(key)

    # 连接信号，以触发缓存更新
    post_save.connect(callback_for_info, sender=Info)
    post_delete.connect(callback_for_info, sender=Info)

# step5 看清套路，重构代码（封装+装饰器）
    # coding=UTF-8
    from __future__ import unicode_literals

    from django.core.cache import cache
    from django.db.models import signals


    def _build_model_cachekey(method, model_class, mid=None):
        """
        构建一个基于Model类的的缓存键。
        :param method 原始方法名。
        :param model_class: Model的类。
        :param mid: Model类的实例的唯一标识，通常为pk，也可为任意唯一标识值。
        :return: 基于Model类的的缓存键。
        """
        opts = model_class._meta
        key = "__model_cache_%s_%s_%s" % (method.__name__, opts.app_label, opts.model_name)
        if not mid is None:
            key = "%s_%s" % (key, mid)
        return key

    def _get_mid(instance):
        """
        获取Model类的实例的唯一标识的默认方法。
        :param instance: Model类的实例。
        :return: Model类的实例的唯一标识。
        """
        return instance.pk


    # Model 数据缓存信号回调方法的集合，将信号回调方法存至全局变量，\
    # 避免该方法因无引用而被系统回收，从而导致信号回调不会执行的问题
    _model_data_cahce_signals_methods = []


    def model_data_cache_method(model_class):
        """
        生成一个用于将一个方法转换为一个依赖于Model的缓存的方法的装饰器。
        用法：
            @model_data_cache_method(Model)
            def get_data_method():
                return Model.objects.filter()
        :param model_class: 依赖的Model类。
        :return: 一个用于将一个方法转换为一个依赖于Model的缓存的方法的装饰器。
        """
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


    def model_instance_data_cache_method(model_class, get_mid_method=None):
        """
        生成一个用于将一个方法转换为一个依赖于Model的单个实例的缓存的方法的装饰器。
        用法：
            @model_data_cache_method(Model)
            def get_data_method(mid):
                return Model.objects.get(pk=mid)
        :param model_class: 依赖的Model类。
        :param get_mid_method: 获取Model实例唯一标识的方法，如果不指定，则默认为获取实例的pk值。
                                注意：此方法返回的Model实例唯一标识应与参数method的第一个参数相一致。
        :return: 一个用于将一个方法转换为一个依赖于Model的单个实例的缓存的方法的装饰器。
        """
        if get_mid_method is None:
            get_mid_method = _get_mid

        def decorator(method):
            def get_data_method(mid):
                key = _build_model_cachekey(method, model_class, mid=mid)
                data = cache.get(key)
                if data is None:
                    data = method(mid)  # 这里是关键，怎么讲method返回的数据存储进入redis
                    cache.set(key, data)
                return data

            def callback_for_method(sender, instance, **kwargs):
                key = _build_model_cachekey(method, model_class, mid=get_mid_method(instance))
                cache.delete(key)

            _model_data_cahce_signals_methods.append(callback_for_method)

            signals.post_save.connect(callback_for_method, sender=model_class)
            signals.post_delete.connect(callback_for_method, sender=model_class)

            return get_data_method
        return decorator



# step6 如何使用
    @model_data_cache_method(Info)
    def get_infos():
        return list(Info.objects.all())

    @model_instance_data_cache_method(Info)
    def get_info(mid):
        return Info.objects.get(pk=mid)

    infos = get_infos()
    info = get_info(1)

# step7 使用实例2
    from django.contrib.auth.models import Group

    @model_data_cache_method(Group)
    def get_groups():
        return list(Group.objects.all())

    @model_instance_data_cache_method(Group, get_mid_method=lambda instance : instance.name)
    def get_group(name):
        return Group.objects.get(name=name)

    groups = get_groups()
    group = get_group("group_name")


