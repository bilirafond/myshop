# Generated by Django 2.0.4 on 2018-05-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_image_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
