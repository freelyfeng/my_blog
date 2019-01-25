# Generated by Django 2.1.4 on 2019-01-24 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=50, unique=True, verbose_name='文章标题')),
                ('a_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('a_image', models.ImageField(null=True, upload_to='upload')),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Colu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=20, unique=True, verbose_name='栏目的名字')),
                ('c_alias', models.CharField(max_length=20, unique=True, verbose_name='栏目的别名')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'colu',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=255, unique=True, verbose_name='用户密码')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='a_column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb1.Colu', verbose_name='文章栏目'),
        ),
    ]