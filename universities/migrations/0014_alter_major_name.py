# Generated by Django 3.2 on 2021-07-10 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0013_auto_20210709_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
