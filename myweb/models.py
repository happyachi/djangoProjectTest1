from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class ShopNameA(models.Model):
    shop_name_a = models.CharField(max_length=10, null=False)
    order = models.IntegerField(default='99')

    def __str__(self):
        return self.shop_name_a

class ShopNameB(models.Model):
    shop_name_b = models.CharField(max_length=10, null=False)
    order = models.IntegerField(default='99')

    def __str__(self):
        return self.shop_name_b

class TransferGoods(models.Model):
    return_sheet_print_choices = (
        ('是', '是'),
        ('否', '否'),
    )
    done_choices = (
        ('已處理', '已處理'),
        ('未處理', '未處理'),
    )

    shop_a_name_from = models.ForeignKey('ShopNameA', on_delete=models.CASCADE)
    shop_b_name_to = models.ForeignKey('ShopNameB', on_delete=models.CASCADE)
    return_sheet_number = models.CharField(max_length=12, unique=True)
    return_sheet_print = models.CharField(max_length=3, choices=return_sheet_print_choices)
    return_sheet_print_staff = models.CharField(null=True, blank=True, max_length=12)
    shop_a_time = models.DateTimeField(default=timezone.now)
    shop_a_staff = models.CharField(max_length=12)
    sell_sheet_number = models.CharField(null=True, blank=True, max_length=12)
    service_time = models.DateTimeField(null=True, blank=True, )
    service_staff = models.CharField(null=True, blank=True, max_length=12)
    remark = models.TextField(null=True, blank=True)
    done = models.CharField(max_length=3, choices=done_choices, default='未處理')

    def __str__(self):
        return self.return_sheet_number

class ZhongliSend(models.Model):
    done_choices = (
        ('已處理', '已處理'),
        ('未處理', '未處理'),
    )
    shop_a_name_from = models.ForeignKey('ShopNameA', on_delete=models.CASCADE)
    order_sheet_number = models.CharField(max_length=12, unique=True)
    pos_sheet_number = models.CharField(max_length=17,)
    shop_a_time = models.DateTimeField(default=timezone.now)
    shop_a_staff = models.CharField(max_length=12)
    sell_sheet_number = models.CharField(null=True, blank=True, max_length=12)
    send_sheet_number = models.CharField(null=True, blank=True, max_length=16)
    service_time = models.DateTimeField(null=True, blank=True, )
    service_staff = models.CharField(null=True, blank=True, max_length=12)
    remark = models.TextField(null=True, blank=True)
    done = models.CharField(max_length=3, choices=done_choices, default='未處理')

    def __str__(self):
        return self.order_sheet_number

class ZhongliCar(models.Model):
    done_choices = (
        ('已處理', '已處理'),
        ('未處理', '未處理'),
    )
    id = models.AutoField(primary_key=True)
    shop_a_name_from = models.ForeignKey('ShopNameA', on_delete=models.CASCADE)
    shop_a_time = models.DateTimeField(default=timezone.now)
    shop_a_staff = models.CharField(max_length=12)
    send_from_people = models.CharField( max_length=30)
    send_from_phone = models.CharField( max_length=30)
    send_from_address = models.CharField( max_length=30)
    product = models.CharField(max_length=50)
    piece = models.PositiveIntegerField()
    send_to_people = models.CharField(max_length=30)
    send_to_phone = models.CharField(max_length=30)
    send_to_address = models.CharField(max_length=30)
    send_sheet_number = models.CharField(null=True, blank=True, max_length=16)
    sell_sheet_number = models.CharField(null=True, blank=True, max_length=12)
    service_time = models.DateTimeField(null=True, blank=True, )
    service_staff = models.CharField(null=True, blank=True, max_length=12)
    remark = models.TextField(null=True, blank=True)
    done = models.CharField(max_length=3, choices=done_choices, default='未處理')

    def __str__(self):
        return str(self.id)

class OrderGoods(models.Model):
    done_choices = (
        ('已處理', '已處理'),
        ('未處理', '未處理'),
    )
    shop_a_name_from = models.ForeignKey('ShopNameA', on_delete=models.CASCADE)
    order_sheet_number = models.CharField(max_length=12, unique=True)
    shop_a_time = models.DateTimeField(default=timezone.now)
    shop_a_staff = models.CharField(max_length=12)
    sell_sheet_number = models.CharField(null=True, blank=True, max_length=12)
    service_time = models.DateTimeField(null=True, blank=True,)
    service_staff = models.CharField(null=True, blank=True, max_length=12)
    remark = models.TextField(null=True, blank=True)
    remark_bao = models.TextField(null=True, blank=True)
    done = models.CharField(max_length=3, choices=done_choices, default='未處理')
    remark_done = models.CharField(max_length=3, choices=done_choices, default='未處理')
    remark_bao_done = models.CharField(max_length=3, choices=done_choices, default='未處理')


class Subject(models.Model):
    subject_title = models.CharField(max_length=50, null=False)
    subject_url = models.CharField(max_length=50, default='')
    order = models.IntegerField(default='99')
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.subject_title


class Topical(models.Model):
    subject_title = models.ForeignKey('Subject', on_delete=models.CASCADE)
    topical_title = models.CharField(max_length=50, null=False)
    topical_url = models.CharField(max_length=50, default='')
    order = models.IntegerField(default='99')
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.topical_title

class Classes(models.Model):
    lesson_topical = models.ForeignKey('Topical', on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=50, null=False)
    lesson_article = RichTextField(default='')
    lesson_update_time = models.DateTimeField(auto_now=True)
    lesson_people = models.CharField(max_length=20, default='')
    lesson_url = models.CharField(max_length=20, default='')
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson_title



class Staff(models.Model):
    staff_number = models.CharField(max_length=10, null=False)
    staff_name = models.CharField(max_length=10, null=False)
    staff_system_number = models.IntegerField()
    staff_email = models.EmailField()

    def __str__(self):
        return self.staff_name
