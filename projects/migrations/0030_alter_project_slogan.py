# Generated by Django 3.2 on 2021-07-02 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0029_auto_20210627_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='slogan',
            field=models.CharField(blank=True, help_text='Very quick description', max_length=125, null=True),
        ),
    ]