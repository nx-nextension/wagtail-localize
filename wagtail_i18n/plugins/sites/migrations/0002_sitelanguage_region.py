# Generated by Django 2.1.7 on 2019-03-25 16:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail_i18n.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_i18n', '0002_region'),
        ('wagtail_i18n_sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitelanguage',
            name='region',
            field=models.ForeignKey(default=wagtail_i18n.models.Region.default_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtail_i18n.Region', verbose_name='region'),
        ),
    ]
