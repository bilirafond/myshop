# Generated by Django 2.0.4 on 2018-05-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.ImageField(default='default', upload_to='color'),
            preserve_default=False,
        ),
    ]
