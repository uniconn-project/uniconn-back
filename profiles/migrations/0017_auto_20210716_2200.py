# Generated by Django 3.2 on 2021-07-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_auto_20210709_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='students', to='profiles.StudentSkill'),
        ),
    ]
