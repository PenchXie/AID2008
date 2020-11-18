from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from bookstore.models import Book


# Create your views here.
def all_book(request):
    books = Book.objects.all()
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, bid):
    try:
        book = Book.objects.get(id=bid)
    except Exception as e:
        print('Error is', e)
        return HttpResponse('图书编号有误!')
    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())
    elif request.method == 'POST':
        market_price = request.POST.get('market_price')
        book.market_price = market_price
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')


def add_book(request):
    if request.method == 'GET':
        return render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        market_price = request.POST.get('market_price')
        press = request.POST.get('press')
        Book.objects.create(title=title, price=price,
                            market_price=market_price, press=press)
        # 重定向到列表视图
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request):
    bid = request.GET.get('bid')
    try:
        book = Book.objects.get(id=bid)
        book.delete()
    except Exception as e:
        print("Error is", e)
        return HttpResponse('图书编号有误!')

    return HttpResponseRedirect('/bookstore/all_book')
