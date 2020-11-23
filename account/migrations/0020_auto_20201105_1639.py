# Generated by Django 3.1.2 on 2020-11-05 13:39

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20201105_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='avatar.png', force_format=None, keep_meta=True, quality=0, size=[500, 300], upload_to=''),
        ),
    ]