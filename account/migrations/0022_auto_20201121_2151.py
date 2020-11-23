# Generated by Django 3.1.2 on 2020-11-21 18:51

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_profile_profile_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='avatar.png', force_format=None, keep_meta=True, quality=75, size=[500, 300], upload_to=''),
        ),
    ]