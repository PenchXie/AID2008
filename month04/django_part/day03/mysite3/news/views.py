from django.shortcuts import render

# Create your views here.
def news_index(request):
    return render(request, 'news/index.html')