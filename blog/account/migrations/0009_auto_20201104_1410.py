# Generated by Django 3.1.2 on 2020-11-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(default='no e-mail...', max_length=200),
        ),
    ]
