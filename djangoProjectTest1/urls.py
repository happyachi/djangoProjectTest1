"""djangoProjectTest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myweb import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

handler400 = "myweb.error_views.view_400"
handler403 = "myweb.error_views.view_403"
handler404 = "myweb.error_views.view_404"
handler500 = "myweb.error_views.view_500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home-url'),
    url(r'^filer/', include('filer.urls')),

    path('transfer_goods/', views.transfer_goods, name='transfer-url'),
    path('transfer_goods/add/',views.transfer_goods_add, name='transfer-add-url'),
    path('transfer_goods/edit/<str:returnsheet>/', views.transfer_goods_edit, name='transfer-edit-url'),
    path('transfer_goods/edit/<str:returnsheet>/delete', views.transfer_goods_edit_delete, name='transfer-edit-delete-url'),

    path('zhongli_send/', views.zhongli_send, name='zhongli-send-url'),
    path('zhongli_send/add/', views.zhongli_send_add, name='zhongli-send-add-url'),
    path('zhongli_send/edit/<str:ordersheet>/', views.zhongli_send_edit, name='zhongli-send-edit-url'),
    path('zhongli_send/edit/<str:ordersheet>/delete', views.zhongli_send_edit_delete, name='zhongli-send-edit-delete-url'),

    path('zhongli_car/', views.zhongli_car, name='zhongli-car-url'),
    path('zhongli_car/add/',views.zhongli_car_add, name='zhongli-car-add-url'),
    path('zhongli_car/edit/<str:id>/', views.zhongli_car_edit, name='zhongli-car-edit-url'),
    path('zhongli_car/edit/<str:id>/delete', views.zhongli_car_edit_delete, name='zhongli-car-edit-delete-url'),

    path('order_goods/', views.order_goods, name='order-goods-url'),
    path('order_goods/add/', views.order_goods_add, name='order-goods-add-url'),
    path('order_goods/edit/<str:ordersheet>/', views.order_goods_edit, name='order-goods-edit-url'),
    path('order_goods/edit/<str:ordersheet>/delete', views.order_goods_edit_delete, name='order-goods-edit-delete-url'),
    path('order_goods/remark/', views.order_goods_remark, name='order-goods-remark-url'),

    path('learning/', views.learning, name='learning-url'),
    path('learning/<str:subjects>/', views.learning_subject, name='learning-subject-url'),
    path('learning/<str:subjects>/<str:classes>/', views.learning_class, name='learning-class-url'),

    path('login/', views.login, name='login-url'),
    path('logout/', views.logout, name='logout-url'),
    path('back/', views.back, name='back-url'),
    path('creat_user/', views.creat_user, name='creat-user-url'),
    path('news/', views.news, name='news-url'),
    path('accounts/', include('allauth.urls')),
    path('zhongli_car/', views.zhongli_car, name='zhongli-car-url'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)