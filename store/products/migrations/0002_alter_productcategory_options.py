# Generated by Django 4.2.1 on 2023-05-23 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'ProductCategories'},
        ),
    ]
