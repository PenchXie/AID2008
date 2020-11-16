from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

html = """
<form method='post' action="/test_get_post">
    姓名:<input type="text" name="username">
    <input type='submit' value='登录'>
</form>
"""


def test_get_post(request):
    if request.method == "GET":
        # print(request.GET['a']) # 没有a会报错
        # print(request.GET.get('a', 100)) # 没有a返回默认值
        print(request.GET.getlist('a'))
        return HttpResponse(html)
    elif request.method == "POST":
        # username = request.POST['username']
        username = request.POST.get('username')
        age = request.POST.get('age', 18)
        return HttpResponse('欢迎<h1>%s岁<a style="color:red">菜逼</a>%s</h1>' % (age, username))


def birthday(request):
    if request.method == "GET":
        year = request.GET.get('year')
        month = request.GET.get('month')
        day = request.GET.get('day')
        return HttpResponse('生日为%s年%s月%s日' % (year, month, day))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        return "我是%s, 今年%s岁了" % (self.name, self.age)

def caibi():
    return "吕泽.菜逼.玛利亚"

def test_html(request):
    # 方式一
    # # 1. 加载模板
    # t = loader.get_template('test_html.html')
    # # 2. 将模板文件(包含字典数据)转换为字符串
    # html = t.render()
    # # 3. 将字符串作为响应对象参数
    # return HttpResponse(html)

    # 方式二
    # person = Person('qtx', 18)
    # dict01 = {}
    # dict01['name'] = "吕泽玛莉亚"
    # dict01['age'] = 18
    # dict01['hobby'] = ['吃饭', '睡觉', '打豆豆']
    # dict01['score'] = {'语文': 99, '数学': 100, '英语': 100}
    # dict01['person'] = person
    # dict01['func1'] = caibi
    # return render(request, 'test_html.html', dict01)

    # 方式三
    name = "lzmaria"
    age = 22
    hobby = ['吃饭', '睡觉', '打豆豆']
    score = {'语文': 99, '数学': 100, '英语': 100}
    person = Person('qtx', 18)
    func1 = caibi
    script = "<script>alert('菜逼')</script>"

    list01 = ['关羽', '张飞', '赵云', '马超', '黄忠']
    # list01 = []
    return render(request, 'test_html.html', locals())


def calculator(request):
    if request.method == "GET":
        return render(request, 'calculator.html')
    elif request.method == "POST":
        x = request.POST.get('x')
        y = request.POST.get('y')
        try:
            x = int(x)
            y = int(y)
        # 非空及非整数判断
        except ValueError as e:
            print("Error:", e)
            result = "<script>alert('请输入整数!')</script>"
            return render(request, 'calculator.html', locals())
        op = request.POST.get('op')
        if op == "add":
            result = x + y
        elif op == "sub":
            result = x - y
        elif op == "mul":
            result = x * y
        elif op == "div":
            try:
                result = x / y
            except ZeroDivisionError:
                result = "<script>alert('除数不能为0!')</script>"
        return render(request, 'calculator.html', locals())