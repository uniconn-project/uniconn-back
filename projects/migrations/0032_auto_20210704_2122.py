# Generated by Django 3.2 on 2021-07-05 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_alter_discussion_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default_project.jpg', upload_to='project_images'),
        ),
    ]
