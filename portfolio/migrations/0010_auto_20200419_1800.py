# Generated by Django 3.0.5 on 2020-04-19 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_project_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='type',
            new_name='typeProject',
        ),
    ]
