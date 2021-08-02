# Generated by Django 3.2 on 2021-08-02 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0027_remove_profile_linkedin'),
        ('projects', '0050_alter_project_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEntryRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=500)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects_entry_requests', to='profiles.profile')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_requests', to='projects.project')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProjectInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=500)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='projects.project')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_projects_invitations', to='profiles.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_projects_invitations', to='profiles.profile')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.DeleteModel(
            name='ProjectRequest',
        ),
    ]