# Generated by Django 3.1.2 on 2020-11-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20201121_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_update',
            field=models.DateTimeField(default=None),
        ),
    ]
