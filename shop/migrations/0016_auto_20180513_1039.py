# Generated by Django 2.0.4 on 2018-05-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20180513_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='shop.Category'),
        ),
    ]
