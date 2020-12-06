import html
import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from tools.login_dec import login_check, get_user_by_request
from topic.models import Topic
from user.models import UserProfile


# Create your views here.
class TopicViews(View):

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
        return JsonResponse({'code': 200, 'username': author.username})

    def get(self, request, author_id):
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
