# Generated by Django 3.0.4 on 2020-03-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200315_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
