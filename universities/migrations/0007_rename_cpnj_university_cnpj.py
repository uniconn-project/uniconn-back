# Generated by Django 3.2 on 2021-04-15 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0006_alter_university_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='university',
            old_name='cpnj',
            new_name='cnpj',
        ),
    ]
