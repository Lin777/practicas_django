# Generated by Django 2.0.4 on 2018-04-17 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20180416_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmer',
            old_name='language',
            new_name='languages',
        ),
    ]