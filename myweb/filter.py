import django_filters
from myweb import models
from django import forms

class TransferGoodsFilter(django_filters.FilterSet):

    return_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
        )

    sell_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
        )

    class Meta:
        model = models.TransferGoods
        fields = {
            'shop_a_name_from',
            'shop_b_name_to',
            'return_sheet_number',
            'sell_sheet_number',
            'done',
        }

class ZhongliSendFilter(django_filters.FilterSet):

    order_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    sell_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    class Meta:
        model = models.ZhongliSend
        fields = {
            'shop_a_name_from',
            'order_sheet_number',
            'sell_sheet_number',
            'done',
        }

class ZhongliCarFilter(django_filters.FilterSet):

    send_from_phone = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    send_to_phone = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    send_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    class Meta:
        model = models.ZhongliCar
        fields = {
            'send_from_phone',
            'send_to_phone',
            'send_sheet_number',
            'done',
        }

class OrderGoodsFilter(django_filters.FilterSet):

    order_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    sell_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    class Meta:
        model = models.OrderGoods
        fields = {
            'shop_a_name_from',
            'order_sheet_number',
            'sell_sheet_number',
            'done',
        }

class OrderGoodsRemarkFilter(django_filters.FilterSet):

    sell_sheet_number = django_filters.CharFilter(
        lookup_expr='icontains',
    )

    class Meta:
        model = models.OrderGoods
        fields = {
            'shop_a_name_from',
            'sell_sheet_number',
            'remark_done',
            'remark_bao_done',
        }