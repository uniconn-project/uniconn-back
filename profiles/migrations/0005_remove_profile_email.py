# Generated by Django 3.2 on 2021-04-17 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_mentor_expertise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]