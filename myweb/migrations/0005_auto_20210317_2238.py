# Generated by Django 3.1.6 on 2021-03-17 14:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myweb', '0004_testtext'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topical_title', models.CharField(max_length=50)),
                ('topical_url', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='testtext',
            old_name='update_time',
            new_name='lesson_update_time',
        ),
        migrations.RemoveField(
            model_name='testtext',
            name='article',
        ),
        migrations.RemoveField(
            model_name='testtext',
            name='people',
        ),
        migrations.RemoveField(
            model_name='testtext',
            name='title',
        ),
        migrations.AddField(
            model_name='testtext',
            name='lesson_article',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='testtext',
            name='lesson_people',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='testtext',
            name='lesson_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testtext',
            name='lesson_url',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='testtext',
            name='lesson_topical',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myweb.topical'),
            preserve_default=False,
        ),
    ]