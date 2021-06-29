# Generated by Django 3.2 on 2021-06-27 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_auto_20210624_2335'),
        ('projects', '0028_auto_20210627_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to='projects.project'),
        ),
    ]