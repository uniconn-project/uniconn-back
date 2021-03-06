# Generated by Django 3.2 on 2021-04-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0004_auto_20210415_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='cpnj',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
