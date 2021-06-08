from django.shortcuts import render, HttpResponseRedirect, redirect
from datetime import datetime
from .models import ShopNameA, ShopNameB, Staff,  Classes, Subject, Topical, TransferGoods, ZhongliSend, ZhongliCar, OrderGoods
from myweb import forms, models
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from .filter import TransferGoodsFilter, ZhongliSendFilter, ZhongliCarFilter, OrderGoodsFilter, OrderGoodsRemarkFilter
from django.core.paginator import Paginator

# Create your views here.


@login_required(login_url='/login/')
def index(request):
    staff = Staff.objects.all()
    now = datetime.now()
    if 'username' in request.session:
        username = request.session['username']
    
    return render(request, 'index.html', locals())


def transfer_goods(request):
    now = datetime.now()
    transfer_goods = TransferGoods.objects.all().order_by('-shop_a_time')

    transfer_goods_filter = TransferGoodsFilter(queryset=transfer_goods)

    if request.method == 'POST':
        transfer_goods_filter = TransferGoodsFilter(request.POST, queryset=transfer_goods)

    paginator = Paginator(transfer_goods_filter.qs, 20)
    num_p = request.GET.get('page', 1)  # 以page为键得到默认的页面1
    page = paginator.page(int(num_p))

    context = {
        'transfer_goods_filter': transfer_goods_filter
    }

    return render(request, 'transfer_goods.html', locals())

def transfer_goods_add(request):
    transfer_goods_add_form = forms.TransferGoodsAddForm()
    now = datetime.now()
    if request.method == 'POST':
        transfer_goods_add_form = forms.TransferGoodsAddForm(request.POST)
        if transfer_goods_add_form.is_valid():
            messages.add_message(request, messages.INFO, "新增成功")
            transfer_goods_add_form.save()
            return HttpResponseRedirect('/transfer_goods/')
        else:
            messages.add_message(request, messages.INFO, "資料有缺")
    else:
        transfer_goods_add_form = forms.TransferGoodsAddForm()

    return render(request, 'transfer_goods_add.html', locals())

def transfer_goods_edit(request, returnsheet):
    transfer_goods_add_form = forms.TransferGoodsEditForm()
    now = datetime.now()
    if request.method == 'POST':
        transfer_goods = TransferGoods.objects.filter(return_sheet_number=returnsheet)
        try:
            for i in range(len(transfer_goods)):
                transfer_goods[i].return_sheet_print = request.POST['return_sheet_print']
                transfer_goods[i].return_sheet_print_staff = request.POST['return_sheet_print_staff']
                transfer_goods[i].service_staff = request.POST['service_staff']
                transfer_goods[i].sell_sheet_number = request.POST['sell_sheet_number']
                transfer_goods[i].remark = request.POST['remark']
                transfer_goods[i].done = request.POST['done']
                if transfer_goods[i].done == '已處理':
                    transfer_goods[i].service_time = datetime.now()
                else:
                    pass
                transfer_goods[i].save()
            messages.add_message(request, messages.INFO, "try成功")
        except:
            messages.add_message(request, messages.INFO, "try失敗")
        messages.add_message(request, messages.INFO, "成功")
        return HttpResponseRedirect('/transfer_goods/')
    else:
        transfer_goods = TransferGoods.objects.filter(return_sheet_number=returnsheet)
        messages.add_message(request, messages.INFO, "失敗")
    return render(request, 'transfer_goods_edit.html', locals())

def transfer_goods_edit_delete(request, returnsheet):
    try:
        transfer_goods = TransferGoods.objects.filter(return_sheet_number=returnsheet)
        transfer_goods.delete()
        messages.add_message(request, messages.INFO, "刪除成功")
    except:
        pass

    return redirect('/transfer_goods/')

def zhongli_send(request):
    now = datetime.now()
    zhongli_send = ZhongliSend.objects.all().order_by('-shop_a_time')
    zhongli_send_filter = ZhongliSendFilter(queryset=zhongli_send)

    if request.method == 'POST':
        zhongli_send_filter = ZhongliSendFilter(request.POST, queryset=zhongli_send)

    paginator = Paginator(zhongli_send_filter.qs, 20)
    num_p = request.GET.get('page', 1)  # 以page为键得到默认的页面1
    page = paginator.page(int(num_p))

    context = {
        'zhongli_send_filter': zhongli_send_filter
    }

    return render(request, 'zhongli_send.html', locals())

def zhongli_send_add(request):
    zhongli_send_add_form = forms.ZhongliSendAddForm()
    now = datetime.now()
    if request.method == 'POST':
        zhongli_send_add_form = forms.ZhongliSendAddForm(request.POST)
        if zhongli_send_add_form.is_valid():
            messages.add_message(request, messages.INFO, "新增成功")
            zhongli_send_add_form.save()
            return HttpResponseRedirect('/zhongli_send/')
        else:
            messages.add_message(request, messages.INFO, "資料有缺")
    else:
        zhongli_send_add_form = forms.ZhongliSendAddForm()
    return render(request, 'zhongli_send_add.html', locals())

def zhongli_send_edit(request, ordersheet):
    now = datetime.now()
    if request.method == 'POST':
        zhongli_send = ZhongliSend.objects.filter(order_sheet_number=ordersheet)
        try:
            for i in range(len(zhongli_send)):
                zhongli_send[i].service_staff = request.POST['service_staff']
                zhongli_send[i].sell_sheet_number = request.POST['sell_sheet_number']
                zhongli_send[i].send_sheet_number = request.POST['send_sheet_number']
                zhongli_send[i].remark = request.POST['remark']
                zhongli_send[i].done = request.POST['done']
                if zhongli_send[i].done == '已處理':
                    zhongli_send[i].service_time = datetime.now()
                else:
                    pass
                zhongli_send[i].save()
            messages.add_message(request, messages.INFO, "try成功")
        except:
            messages.add_message(request, messages.INFO, "try失敗")
        messages.add_message(request, messages.INFO, "成功")
        return HttpResponseRedirect('/zhongli_send/')
    else:
        zhongli_send = ZhongliSend.objects.filter(order_sheet_number=ordersheet)
        messages.add_message(request, messages.INFO, "失敗")
    return render(request, 'zhongli_send_edit.html', locals())

def zhongli_send_edit_delete(request, ordersheet):
    try:
        zhongli_send = ZhongliSend.objects.filter(order_sheet_number=ordersheet)
        zhongli_send.delete()
        messages.add_message(request, messages.INFO, "刪除成功")
    except:
        pass
    return redirect('/zhongli_send/')


def zhongli_car(request):
    now = datetime.now()
    zhongli_car = ZhongliCar.objects.all().order_by('-shop_a_time')

    zhongli_car_filter = ZhongliCarFilter(queryset=zhongli_car)

    if request.method == 'POST':
        zhongli_car_filter = ZhongliCarFilter(request.POST, queryset=zhongli_car)

    paginator = Paginator(zhongli_car_filter.qs, 20)
    num_p = request.GET.get('page', 1)  # 以page为键得到默认的页面1
    page = paginator.page(int(num_p))

    context = {
        'zhongli_car_filter': zhongli_car_filter
    }
    return render(request, 'zhongli_car.html', locals())


def zhongli_car_add(request):
    now = datetime.now()
    zhongli_car_add_form = forms.ZhongliCarAddForm()
    now = datetime.now()
    if request.method == 'POST':
        zhongli_car_add_form = forms.ZhongliCarAddForm(request.POST)
        if zhongli_car_add_form.is_valid():
            messages.add_message(request, messages.INFO, "新增成功")
            zhongli_car_add_form.save()
            return HttpResponseRedirect('/zhongli_car/')
        else:
            messages.add_message(request, messages.INFO, "資料有缺")
    else:
        zhongli_car_add_form = forms.ZhongliCarAddForm()
    return render(request, 'zhongli_car_add.html', locals())


def zhongli_car_edit(request, id):
    now = datetime.now()
    if request.method == 'POST':
        zhongli_car = ZhongliCar.objects.filter(id=id)
        try:
            for i in range(len(zhongli_car)):
                zhongli_car[i].send_from_people = request.POST['send_from_people']
                zhongli_car[i].send_from_phone = request.POST['send_from_phone']
                zhongli_car[i].send_from_address = request.POST['send_from_address']
                zhongli_car[i].product = request.POST['product']
                zhongli_car[i].piece = request.POST['piece']
                zhongli_car[i].send_to_people = request.POST['send_to_people']
                zhongli_car[i].send_to_phone = request.POST['send_to_phone']
                zhongli_car[i].send_to_address = request.POST['send_to_address']
                zhongli_car[i].send_sheet_number = request.POST['send_sheet_number']
                zhongli_car[i].sell_sheet_number = request.POST['sell_sheet_number']
                zhongli_car[i].service_staff = request.POST['service_staff']
                zhongli_car[i].remark = request.POST['remark']
                zhongli_car[i].done = request.POST['done']
                if zhongli_car[i].done == '已處理':
                    zhongli_car[i].service_time = datetime.now()
                else:
                    pass
                zhongli_car[i].save()
            messages.add_message(request, messages.INFO, "try成功")
        except:
            messages.add_message(request, messages.INFO, "try失敗")
        messages.add_message(request, messages.INFO, "成功")
        return HttpResponseRedirect('/zhongli_car/')
    else:
        zhongli_car = ZhongliCar.objects.filter(id=id)
        messages.add_message(request, messages.INFO, "失敗")
    return render(request, 'zhongli_car_edit.html', locals())

def zhongli_car_edit_delete(request, id):
    try:
        zhongli_car = ZhongliCar.objects.filter(id=id)
        zhongli_car.delete()
        messages.add_message(request, messages.INFO, "刪除成功")
    except:
        pass

    return redirect('/zhongli_car/')


def order_goods(request):
    now = datetime.now()
    order_goods = OrderGoods.objects.all().order_by('-shop_a_time')

    order_goods_filter = OrderGoodsFilter(queryset=order_goods)

    if request.method == 'POST':
        order_goods_filter = OrderGoodsFilter(request.POST, queryset=order_goods)

    paginator = Paginator(order_goods_filter.qs, 20)
    num_p = request.GET.get('page', 1)  # 以page为键得到默认的页面1
    page = paginator.page(int(num_p))

    context = {
        'order_goods_filter': order_goods_filter
    }
    return render(request, 'order_goods.html', locals())

def order_goods_add(request):
    now = datetime.now()
    order_goods_add_form = forms.OrderGoodsAddForm
    if request.method == 'POST':
        order_goods_add_form = forms.OrderGoodsAddForm(request.POST)
        if order_goods_add_form.is_valid():
            messages.add_message(request, messages.INFO, "新增成功")
            order_goods_add_form.save()
            return HttpResponseRedirect('/order_goods/')
        else:
            messages.add_message(request, messages.INFO, "資料有缺")
    else:
        order_goods_add_form = forms.OrderGoodsAddForm()
    return render(request, 'order_goods_add.html', locals())

def order_goods_edit(request, ordersheet):
    now = datetime.now()
    if request.method == 'POST':
        order_goods = OrderGoods.objects.filter(order_sheet_number=ordersheet)
        try:
            for i in range(len(order_goods)):
                order_goods[i].service_staff = request.POST['service_staff']
                order_goods[i].sell_sheet_number = request.POST['sell_sheet_number']
                order_goods[i].remark = request.POST['remark']
                order_goods[i].remark_bao = request.POST['remark_bao']
                order_goods[i].done = request.POST['done']
                if order_goods[i].done == '已處理':
                    order_goods[i].service_time = datetime.now()
                else:
                    pass
                order_goods[i].save()
            messages.add_message(request, messages.INFO, "try成功")
        except:
            messages.add_message(request, messages.INFO, "try失敗")
        messages.add_message(request, messages.INFO, "成功")
        return HttpResponseRedirect('/order_goods/')
    else:
        order_goods = OrderGoods.objects.filter(order_sheet_number=ordersheet)
        messages.add_message(request, messages.INFO, "失敗")
    return render(request, 'order_goods_edit.html', locals())

def order_goods_edit_delete(request, ordersheet):
    try:
        order_goods = OrderGoods.objects.filter(order_sheet_number=ordersheet)
        order_goods.delete()
        messages.add_message(request, messages.INFO, "刪除成功")
    except:
        pass
    return redirect('/order_goods/')


def order_goods_remark(request ):
    now = datetime.now()
    order_goods = OrderGoods.objects.all().order_by('-shop_a_time')

    order_goods_filter = OrderGoodsRemarkFilter(queryset=order_goods)

    if request.method == 'POST':
        order_goods_filter = OrderGoodsRemarkFilter(request.POST, queryset=order_goods)

    paginator = Paginator(order_goods_filter.qs, 20)
    num_p = request.GET.get('page', 1)  # 以page为键得到默认的页面1
    page = paginator.page(int(num_p))

    context = {
        'order_goods_filter': order_goods_filter
    }

    if request.method == 'GET':
        try:
            order_sheet_number = request.GET['order_sheet_number']
            order_goods_get = OrderGoods.objects.filter(order_sheet_number=order_sheet_number)
            try:
                for i in range(len(order_goods_get)):
                    order_goods_get[i].remark_done = request.GET['remark_done']
                    order_goods_get[i].remark_bao_done = request.GET['remark_bao_done']
                    order_goods_get[i].save()
                messages.add_message(request, messages.INFO, "try成功")
            except:
                messages.add_message(request, messages.INFO, "try失敗")
        except:
            order_sheet_number = None
    else:
        pass

    return render(request, 'order_goods_remark.html', locals())


def learning(request):
    subject = Subject.objects.filter(show=True).order_by('order')
    topical = Topical.objects.filter(show=True).order_by('order')
    now = datetime.now()

    return render(request, 'learning.html', locals())

def learning_subject(request, subjects):
    subject = Subject.objects.filter(show=True).order_by('order')
    topical = Topical.objects.filter(show=True).order_by('order')
    now = datetime.now()
    try:
        topical_list = Topical.objects.filter(subject_title__subject_url=subjects)
    except:
        topical_list = None
    return render(request, 'learning_subjects.html', locals())

def learning_class(request, subjects, classes):
    subject = Subject.objects.filter(show=True).order_by('order')
    topical = Topical.objects.filter(show=True).order_by('order')
    now = datetime.now()

    try:
        test_post = Classes.objects.filter(lesson_url=classes, show=True)
    except:
        test_post = None

    return render(request, 'learning_class.html', locals())

def login(request):
    now = datetime.now()
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_email = request.POST['staff_email'].strip()
            users = authenticate(email=login_email,password='achi',username='achi')
            if users is not None:
                auth.login(request, users)
                messages.add_message(request, messages.WARNING, '成功登入')
                return redirect('/')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
            try:
                user = models.Staff.objects.get(staff_email = login_email)
                messages.add_message(request, messages.WARNING, '成功')
                request.session['username'] = user.staff_name
                request.session['useremail'] = user.staff_email
                return redirect('/')
            except:
                messages.add_message(request, messages.WARNING, '找不到使用者')
        else:
            messages.add_message(request, messages.WARNING, '請檢查輸入內容')
    else:
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())

def logout(request):
    now = datetime.now()
    auth.logout(request)
    messages.add_message(request, messages.WARNING, '登出囉～')
    return render(request, 'logout.html', locals())

def back(request):
    now = datetime.now()
    return render(request, 'back.html', locals())

def creat_user(request):
    now = datetime.now()
    staff = Staff.objects.all()
    creat_user_form = forms.CreatStaffForm()
    if request.method == 'POST':
        creat_user_form = forms.CreatStaffForm(request.POST)
        if creat_user_form.is_valid():
            messages.add_message(request, messages.INFO, "新增成功")
            creat_user_form.save()
            return HttpResponseRedirect('/creat_user/')
        else:
            messages.add_message(request, messages.INFO, "資料有缺")
    else:
        creat_user_form = forms.CreatStaffForm()
    return render(request, 'creat_user.html', locals())

def news(request):
    now = datetime.now()
    return render(request, 'news.html', locals())

def test123(request):
    ppp = 123
    return render(request, 'test.html', locals())





