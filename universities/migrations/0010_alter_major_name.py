# Generated by Django 3.2 on 2021-04-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0009_alter_university_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]