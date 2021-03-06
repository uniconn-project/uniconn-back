# Generated by Django 3.2 on 2021-05-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('startup', 'startup'), ('junior_enterprise', 'empresa júnior'), ('academic', 'projeto acadêmico'), ('social_project', 'projeto social')], max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
