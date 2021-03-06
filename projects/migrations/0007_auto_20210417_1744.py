# Generated by Django 3.2 on 2021-04-17 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_remove_profile_email'),
        ('projects', '0006_alter_market_mentors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='mentors',
            field=models.ManyToManyField(blank=True, related_name='projects', to='profiles.Mentor'),
        ),
        migrations.AlterField(
            model_name='project',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='projects', to='profiles.Student'),
        ),
    ]
