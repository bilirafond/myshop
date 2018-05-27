# Generated by Django 2.0.4 on 2018-05-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_product_color_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color_test',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='products', to='shop.Color'),
        ),
    ]
