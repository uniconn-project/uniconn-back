# Generated by Django 3.2 on 2021-07-17 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_alter_studentskill_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentskill',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
