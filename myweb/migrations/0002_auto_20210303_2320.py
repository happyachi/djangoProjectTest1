# Generated by Django 3.1.6 on 2021-03-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changefrom',
            name='ps',
            field=models.TextField(blank=True, null=True),
        ),
    ]
