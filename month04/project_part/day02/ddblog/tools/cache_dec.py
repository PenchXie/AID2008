from django.core.cache import cache

from tools.login_dec import get_user_by_request


def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request, *args, **kwargs):
            # tedu/topics?t_id=1&a=100&b=200
            # GET {'t_id': 1, 'a': 100, 'b': 200}
            # keys() ['t_id', 'a', 'b']
            if 't_id' in request.GET.keys():
                # 拿文章详情页直接调用
                return func(request, *args, **kwargs)
            # 文章列表页设置缓存
            # 是否是博主访问自己
            # 访问者
            visitor_name = get_user_by_request(request)
            # 谁的文章
            author_name = kwargs['author_id']
            print('访问者:%s,作者%s' % (visitor_name, author_name))

            if visitor_name == author_name:
                # 博主访问
                cache_key = 'topic_cache_self_%s' % request.get_full_path()
            else:
                # 非博主访问
                cache_key = 'topic_cache_%s' % request.get_full_path()
            print('---cache key is %s ---' % cache_key)
            # 缓存思想
            res = cache.get(cache_key)
            if res:
                print('------cache in------')
                return res
            res = func(request, *args, **kwargs)
            cache.set(cache_key, res, expire)
            return res
        return wrapper
    return _topic_cache