# Generated by Django 3.1.6 on 2021-03-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0006_auto_20210317_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='order',
            field=models.IntegerField(default='99'),
        ),
        migrations.AddField(
            model_name='subject',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
