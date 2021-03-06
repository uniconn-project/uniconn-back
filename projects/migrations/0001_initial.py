# Generated by Django 3.2 on 2021-04-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universities', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('startup', 'startup'), ('junior_enterprise', 'junior enterprise'), ('academic', 'academic project')], max_length=50)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('fields', models.ManyToManyField(related_name='projects', to='universities.MajorField')),
                ('students', models.ManyToManyField(related_name='projects', to='profiles.Student')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
