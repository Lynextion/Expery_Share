# Generated by Django 3.1.2 on 2020-11-03 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=200)),
                ('bio', models.CharField(default='no bio...', max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('avatar', models.ImageField(default='avatar.png', upload_to='media/')),
            ],
        ),
    ]
