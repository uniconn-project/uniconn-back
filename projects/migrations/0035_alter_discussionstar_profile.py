# Generated by Django 3.2 on 2021-07-06 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20210702_1503'),
        ('projects', '0034_auto_20210706_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionstar',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discussions_stars', to='profiles.profile'),
        ),
    ]
