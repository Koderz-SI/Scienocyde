# Generated by Django 3.1.7 on 2021-04-01 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210330_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='Image_of_Project',
            field=models.URLField(),
        ),
    ]
