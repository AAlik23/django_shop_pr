# Generated by Django 2.2.24 on 2021-11-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211113_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='we will add description soon', max_length=5000, null=True),
        ),
    ]
