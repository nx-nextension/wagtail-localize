# Generated by Django 2.1.7 on 2019-03-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('languages', models.ManyToManyField(to='wagtail_i18n.Language')),
            ],
        ),
    ]
