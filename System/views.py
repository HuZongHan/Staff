from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from System.models import Emp, User


def userList(request):
    # 获取数据
    emp = Emp.objects.all()
    # 页码
    page = int(request.GET.get("page", 1))
    # 每一页数据
    per_page = request.GET.get("per_page", 4)
    # 分页器
    paginator = Paginator(emp, per_page)
    # 单页数据
    page_single = paginator.page(page)
    # page_single.has_previous()
    # page_single.has_next()
    # page_single.previous_page_number()
    # page_single.next_page_number()

    return render(request,'userList.html',locals())


def userAdd(request):
    if request.method == 'GET':
        return render(request, 'userAdd.html')
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        emp = Emp()
        emp.name = name
        emp.age = age
        emp.gender = gender
        emp.save()
        return redirect(reverse('sta:userList'))


def userDelete(request, ):
    id = request.GET.get('id')
    emp = Emp.objects.get(pk=id)
    emp.delete()
    return redirect(reverse('sta:userList'))


def userUpdate(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        emp = Emp.objects.get(pk=id)
        context = {
            'emp': emp
        }
        return render(request, 'userUpdate.html', context=context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        id = request.POST.get('id')
        emp = Emp.objects.get(pk=id)
        emp.name = name
        emp.age = age
        emp.gender = gender
        emp.save()

        return redirect(reverse('sta:userList'))


# def fenye(request):
    # # 获取数据
    # emp = Emp.objects.all()
    # # 页码
    # page = int(request.GET.get("page", 1))
    # # 每一页数据
    # per_page = request.GET.get("per_page", 4)
    # # 分页器
    # paginator = Paginator(emp, per_page)
    # # 单页数据
    # page_single = paginator.page(page)
    # return redirect(reverse('sta:userList'),locals())

    # book_list = []
    # '''
    # 数据通常是从 models 中获取。这里为了方便，直接使用生成器来获取数据。
    # '''
    # for x in range(1, 26):  # 一共 25 本书
    #     book_list.append('Book ' + str(x))
    # # emp = Emp.objects.all()
    #
    # # 将数据按照规定每页显示 10 条, 进行分割
    # paginator = Paginator(book_list, 5)
    #
    # if request.method == "GET":
    #     # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
    #     page = request.GET.get('page')
    #     try:
    #         books = paginator.page(page)
    #     #
    #     except PageNotAnInteger:
    #         # 如果请求的页数不是整数, 返回第一页。
    #         books = paginator.page(1)
    #     except InvalidPage:
    #         # 如果请求的页数不存在, 重定向页面
    #         return HttpResponse('找不到页面的内容')
    #     except EmptyPage:
    #         # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
    #         books = paginator.page(paginator.num_pages)
    #
    # template_view = 'page.html'
    # return render(request, template_view, {'books': books})

    # if request.method == 'POST':
    #     emp = Emp.objects.all()
    #     paginagtor = Paginator(emp, 4)
    #     pager = paginagtor.page(page)
    #     pager.has_previous()
    #     pager.has_next()
    #     pager.previous_page_number()
    #     pager.next_page_number()
    #     return redirect(reverse('sta:page'))


def userRegist(request):
    if request.method == 'GET':
        return render(request, 'userRegist.html')
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     password = request.POST.get('password')
    #     request.session['name'] = name
    #
    #     password = make_password(password)
    #     User.objects.create(name=name, password=password)
    #     return redirect(reverse('sta:userLogin'))
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        password = make_password(password)
        user = User()
        user.name = name
        user.password = password
        user.save()
        return render(request, 'userLogin.html')


def userLogin(request):
    if request.method == 'GET':
        return render(request, 'userLogin.html')
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     password = request.POST.get('password')
    #
    #     if User.objects.filter(name=name).exists():
    #         return render(request, 'userLogin.html', {'password': '用户密码错误'})
    #
    #     if check_password(password, User.password):
    #
    #         return redirect(reverse('sta:userList'))
    #     else:
    #         return render(request, 'userList.html', context=locals() )
    if request.method == 'POST':
        name = request.POST.get('name')
        passwd = request.POST.get('password')
        user = User.objects.get(name=name)

        if check_password(passwd, user.password):
            # if passwd == user.password:
            return redirect(reverse('sta:userList'))
        else:
            return HttpResponse('密码不正确')
