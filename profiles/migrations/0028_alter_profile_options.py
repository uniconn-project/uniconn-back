# Generated by Django 3.2 on 2021-08-02 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_remove_profile_linkedin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-id']},
        ),
    ]
