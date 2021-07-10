# Generated by Django 3.2 on 2021-07-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0038_alter_discussionreply_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='body',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='title',
            field=models.CharField(default='', max_length=125),
        ),
        migrations.AlterField(
            model_name='discussionreply',
            name='content',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='link',
            name='href',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='project',
            name='slogan',
            field=models.CharField(default='', help_text='Very quick description', max_length=125),
        ),
        migrations.AlterField(
            model_name='projectenteringrequest',
            name='message',
            field=models.CharField(default='', max_length=500),
        ),
    ]
