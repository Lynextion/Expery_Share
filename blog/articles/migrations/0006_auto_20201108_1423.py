# Generated by Django 3.1.2 on 2020-11-08 11:23

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20201105_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=0, size=[600, 750], upload_to=''),
        ),
    ]
