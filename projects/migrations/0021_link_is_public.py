# Generated by Django 3.2 on 2021-06-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_alter_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
