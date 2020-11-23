import csv
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from test_upload.models import Content


def test_csv(request):
    # 1. 指定响应内容的类型
    response = HttpResponse(content_type='text/csv')
    # 2. 指定以附件的形式另存为
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    # 3. 创建一个csv写入器, 将内容写到response
    writer = csv.writer(response)
    writer.writerow(['编号', '名称'])
    books = [
        {'id': 1, 'name': 'python'},
        {'id': 2, 'name': 'c++'},
        {'id': 3, 'name': 'java'},
    ]
    for b in books:
        writer.writerow([b['id'], b['name']])
    return response

@csrf_exempt
def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        title = request.POST['title']
        afile = request.FILES['myfile']
        # 方式一: python的方式
        # # 生成一个服务器端的文件存储路径
        # filename = os.path.join(settings.MEDIA_ROOT, afile.name)
        # with open(filename, 'wb') as f:
        #     data = afile.file.read()
        #     f.write(data)
        # 方式二: orm方式
        Content.objects.create(title=title, myfile=afile)
        return HttpResponse('上传文件成功!文件名称:%s, 文件标题%s' % (afile.name, title))
