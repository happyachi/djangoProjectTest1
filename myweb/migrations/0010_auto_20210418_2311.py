# Generated by Django 3.1.6 on 2021-04-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0009_auto_20210330_2201'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ShopName',
            new_name='ShopNameA',
        ),
        migrations.RenameModel(
            old_name='ShopName2',
            new_name='ShopNameB',
        ),
        migrations.RenameField(
            model_name='shopnamea',
            old_name='shop_name',
            new_name='shop_name_a',
        ),
        migrations.RenameField(
            model_name='shopnameb',
            old_name='shop_name',
            new_name='shop_name_b',
        ),
    ]
