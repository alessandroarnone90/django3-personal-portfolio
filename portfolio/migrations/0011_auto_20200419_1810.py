# Generated by Django 3.0.5 on 2020-04-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20200419_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='typeProject',
            field=models.CharField(choices=[('Machine learning', 'Machine Learning'), ('Data analytics', 'Data analytics'), ('Deep Learning', 'Deep Learning')], max_length=200),
        ),
    ]
