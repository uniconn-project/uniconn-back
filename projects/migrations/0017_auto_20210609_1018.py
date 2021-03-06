# Generated by Django 3.2 on 2021-06-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_profile_linkedin'),
        ('projects', '0016_alter_project_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pending_invited_mentors',
            field=models.ManyToManyField(blank=True, related_name='pending_projects_invitations', to='profiles.Mentor'),
        ),
        migrations.AddField(
            model_name='project',
            name='pending_invited_students',
            field=models.ManyToManyField(blank=True, related_name='pending_projects_invitations', to='profiles.Student'),
        ),
    ]
