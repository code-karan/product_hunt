# Generated by Django 2.2.5 on 2019-10-20 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='body',
            new_name='summary',
        ),
    ]
