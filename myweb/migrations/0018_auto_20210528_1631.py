# Generated by Django 3.1.6 on 2021-05-28 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0017_zhonglicar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhonglicar',
            name='piece',
            field=models.PositiveIntegerField(),
        ),
    ]
