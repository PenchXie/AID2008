import html
import json

from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page

from tools.cache_dec import topic_cache
from tools.login_dec import login_check, get_user_by_request
from topic.models import Topic
from user.models import UserProfile


# Create your views here.
class TopicViews(View):
    def make_topic_res(self, author, author_topic, is_self):
        # 上一篇和下一篇
        if is_self:
            next_topic = Topic.objects.filter(id__gt=author_topic.id,
                                              user_profile_id=author.username, ).first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id,
                                              user_profile_id=author.username, ).last()
        else:
            next_topic = Topic.objects.filter(id__gt=author_topic.id, limit='public',
                                              user_profile_id=author.username, ).first()
            last_topic = Topic.objects.filter(id__lt=author_topic.id, limit='public',
                                              user_profile_id=author.username, ).last()
        # if next_topic:
        #     next_id = next_topic.id
        #     next_title = next_topic.title
        # else:
        #     next_id = None
        #     next_title = None
        (next_id, next_title) = (next_topic.id, next_topic.title) if next_topic else (None, None)
        (last_id, last_title) = (last_topic.id, last_topic.title) if last_topic else (None, None)
        # 生成详情页的返回值
        result = {'code': 200, 'data': {}}
        result['data']['nickname'] = author.nickname
        result['data']['title'] = author_topic.title
        result['data']['category'] = author_topic.category
        result['data']['content'] = author_topic.content
        result['data']['introduce'] = author_topic.introduce
        result['data']['author'] = author.nickname
        result['data']['created_time'] = author_topic.created_time.strftime('%Y-%m%d %H:%M:%S')
        # 上一篇/下一篇
        result['data']['last_id'] = last_id
        result['data']['last_title'] = last_title
        result['data']['next_id'] = next_id
        result['data']['next_title'] = next_title
        # 评论相关
        result['data']['messages'] = []
        result['data']['messages_count'] = 0
        # 返回
        return result

    def make_topics_res(self, author, author_topics):
        # 返回指定用户的文章列表
        topics_res = []
        for topic in author_topics:
            d = {}
            d['id'] = topic.id
            d['title'] = topic.title
            d['category'] = topic.category
            d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
            d['introduce'] = topic.introduce
            d['author'] = author.nickname
            topics_res.append(d)
        res = {
            'code': 200,
            'data': {}
        }
        res['data']['topics'] = topics_res
        res['data']['nickname'] = author.nickname
        return res

    def clear_topic_cashes(self, request):
        # v1/topics/tedu
        # v1/topics/tedu?category=tec
        # v1/topics/tedu?category=no-tec
        # post请求的url:"http://127.0.0.1:8000/v1/topics/" + username
        # all_path = request.get_full_path()
        all_path = request.path_info
        all_key_p = ['topic_cache_self_', 'topic_cache_']
        all_key = []
        for key_p in all_key_p:
            for key_h in ['', '?category=tec', '?category=no-tec']:
                all_key.append(key_p + all_path + key_h)
        print('------all keys------')
        print(all_key)
        cache.delete_many(all_key)


    @method_decorator(login_check)
    def post(self, request, author_id):
        json_str = request.body
        json_obj = json.loads(json_str)
        content = json_obj['content']
        content_text = json_obj['content_text']
        introduce = content_text[:20]
        title = json_obj['title']
        # 避免xss攻击, 对用户输入做转义
        title = html.escape(title)
        limit = json_obj['limit']
        if limit not in ['public', 'private']:
            result = {'code': 10300, 'error': 'the limit is wrong'}
            return JsonResponse(result)
        category = json_obj['category']
        if category not in ['tec', 'no-tec']:
            result = {'code': 10301, 'error': 'the category is wrong'}
            return JsonResponse(result)

        author = request.myuser
        # 数据入库
        Topic.objects.create(title=title, content=content, limit=limit, category=category,
                             introduce=introduce, user_profile=author)
        # 清除缓存
        self.clear_topic_cashes(request)
        return JsonResponse({'code': 200, 'username': author.username})

    @method_decorator(topic_cache(180))
    def get(self, request, author_id):
        print('------get view in------')
        try:
            author = UserProfile.objects.get(username=author_id)
        except Exception as e:
            print('Error is', e)
            result = {'code': 10302, 'error': 'the author id is wrong'}
            return JsonResponse(result)
        # 返回文章列表前, 确定访问者的身份
        # 如果是博主本人访问, 返回所有文章
        # 如果不是博主本人访问, 只返回公开的文章
        # 从token中获取用户信息
        visitor_username = get_user_by_request(request)

        # 获取t_id
        t_id = request.GET.get('t_id')
        is_self = False  # 是否是博主访问自己
        if t_id:
            # 获取的是文章详情页
            if visitor_username == author_id:
                # 博主访问, 可以看到所有文章
                is_self = True
                try:
                    author_topic = Topic.objects.get(id=t_id,
                                                     user_profile_id=author_id)
                except Exception as e:
                    result = {'code': 10303, 'error': 'the topic id is error'}
                    return JsonResponse(result)

            else:
                # 非博主访问, 只能看public的文章
                try:
                    author_topic = Topic.objects.get(id=t_id, limit='public',
                                                     user_profile_id=author_id)
                except Exception as e:
                    result = {'code': 10303, 'error': 'the topic id is error'}
                    return JsonResponse(result)
            # 按照前段需要的JsonResponse格式返回
            res = self.make_topic_res(author, author_topic, is_self)
            return JsonResponse(res)
        else:
            # 获取的是文章列表页
            # 分类
            # 1. 从查询字符串中获取分类的值
            category = request.GET.get('category')
            # 2. 判断在['tec', 'no-tec']中
            category_sign = False
            if category in ['tec', 'no-tec']:
                category_sign = True
            # 3. 是否有分类[定义一个变量, 有分类赋值为True: 否则False]
            # 博主本人访问自己的博客, 返回个人+公开的文章
            if author_id == visitor_username:
                # 4. 是否需要增加分类条件
                if not category_sign:
                    author_topics = Topic.objects.filter(user_profile_id=author_id)
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, category=category)
            else:
                # 只返回该用户公开的文章
                # 4. 是否需要增加分类条件
                if not category_sign:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public')
                else:
                    author_topics = Topic.objects.filter(user_profile_id=author_id, limit='public', category=category)
            # 按照一定的格式返回
            res = self.make_topics_res(author, author_topics)
            return JsonResponse(res)
