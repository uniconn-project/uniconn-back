# Generated by Django 3.2 on 2021-07-30 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_auto_20210729_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='linkedIn',
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('href', models.CharField(blank=True, max_length=300)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links', to='profiles.profile')),
            ],
        ),
    ]