# Generated by Django 3.2 on 2021-07-05 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0032_auto_20210704_2122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectenteringrequest',
            options={'ordering': ['-id']},
        ),
    ]
