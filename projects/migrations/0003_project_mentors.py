# Generated by Django 3.2 on 2021-04-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210413_1454'),
        ('projects', '0002_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mentors',
            field=models.ManyToManyField(related_name='projects', to='profiles.Mentor'),
        ),
    ]