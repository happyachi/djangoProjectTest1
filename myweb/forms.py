#-*- encoding: utf-8 -*-
from django import forms
from myweb import models

class TransferGoodsAddForm(forms.ModelForm):
    class Meta:
        model = models.TransferGoods
        fields = [
            'shop_a_name_from',
            'shop_b_name_to',
            'return_sheet_number',
            'return_sheet_print',
            'return_sheet_print_staff',
            'shop_a_staff',
            'remark'
        ]

    def __init__(self, *args, **kwargs):
        super(TransferGoodsAddForm, self).__init__(*args, **kwargs)
        self.fields['shop_a_name_from'].label = '退貨店'
        self.fields['shop_b_name_to'].label = '調貨店'
        self.fields['return_sheet_number'].label = '銷退單'
        self.fields['return_sheet_print'].label = '銷退單是否列印'
        self.fields['return_sheet_print_staff'].label = '銷退單列印人'
        self.fields['shop_a_staff'].label = '填寫人員'
        self.fields['remark'].label = '備註'

class TransferGoodsEditForm(forms.Form):
    return_sheet_print_choice = [
        ['是','是'],
        ['否','否'],
    ]
    done_choices = [
        ['已處理','已處理'],
        ['未處理','未處理'],
    ]
    shop_a_staff = forms.CharField(label='分店處理人',max_length=12,initial='',required=False)
    return_sheet_print = forms.ChoiceField(label='是否列印',choices=return_sheet_print_choice)
    return_sheet_print_staff = forms.CharField(label='列印人',max_length=12,initial='',required=False)
    service_staff = forms.CharField(label='中壢處理人',max_length=12,initial='',required=False)
    service_time = forms.DateTimeField(label='處理日期',required=False,widget=forms.DateInput(attrs={'type':'datetime-local'}))
    sell_sheet_number = forms.CharField(label='銷售單號',max_length=12,initial='',required=False)
    remark = forms.CharField(label='備註',widget=forms.Textarea)
    done = forms.ChoiceField(label='處理狀態',choices=done_choices)

class ZhongliSendAddForm(forms.ModelForm):
    class Meta:
        model = models.ZhongliSend
        fields = [
            'shop_a_name_from',
            'order_sheet_number',
            'pos_sheet_number',
            'shop_a_staff',
            'remark'
        ]

    def __init__(self, *args, **kwargs):
        super(ZhongliSendAddForm, self).__init__(*args, **kwargs)
        self.fields['shop_a_name_from'].label = '分店'
        self.fields['order_sheet_number'].label = '訂單編號'
        self.fields['pos_sheet_number'].label = 'POS單號'
        self.fields['shop_a_staff'].label = '填寫人'
        self.fields['remark'].label = '備註'


class ZhongliCarAddForm(forms.ModelForm):
    class Meta:
        model = models.ZhongliCar
        fields = [
            'shop_a_name_from',
            'shop_a_staff',
            'send_from_people',
            'send_from_phone',
            'send_from_address',
            'product',
            'piece',
            'send_to_people',
            'send_to_phone',
            'send_to_address',
            'remark',
        ]

    def __init__(self, *args, **kwargs):
        super(ZhongliCarAddForm, self).__init__(*args, **kwargs)
        self.fields['shop_a_name_from'].label = '分店'
        self.fields['shop_a_staff'].label = '填寫人'
        self.fields['send_from_people'].label = '甲地寄件人'
        self.fields['send_from_phone'].label = '甲地寄件人電話'
        self.fields['send_from_address'].label = '甲地寄件人地址'
        self.fields['product'].label = '商品'
        self.fields['piece'].label = '件數'
        self.fields['send_to_people'].label = '乙地收件人'
        self.fields['send_to_phone'].label = '乙地收件人電話'
        self.fields['send_to_address'].label = '乙地收件人地址'
        self.fields['remark'].label = '備註'

class OrderGoodsAddForm(forms.ModelForm):
    class Meta:
        model = models.OrderGoods
        fields = [
            'shop_a_name_from',
            'order_sheet_number',
            'shop_a_staff',
            'remark',
            'remark_bao',
        ]

    def __init__(self, *args, **kwargs):
        super(OrderGoodsAddForm, self).__init__(*args, **kwargs)
        self.fields['shop_a_name_from'].label = '分店'
        self.fields['order_sheet_number'].label = '訂單編號'
        self.fields['shop_a_staff'].label = '填寫人'
        self.fields['remark'].label = '一般備註'
        self.fields['remark_bao'].label = '小寶備註'



class CreatStaffForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = [
            'staff_name',
            'staff_number',
            'staff_system_number',
            'staff_email',
        ]

    def __init__(self, *args, **kwargs):
        super(CreatStaffForm, self).__init__(*args, **kwargs)
        self.fields['staff_name'].label = '姓名'
        self.fields['staff_number'].label = '員工代號'
        self.fields['staff_system_number'].label = '系統帳號'
        self.fields['staff_email'].label = '電子信箱'

class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Staff
        fields = ['staff_email']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['staff_email'].label = '電子信箱'