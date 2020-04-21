# Generated by Django 3.0.5 on 2020-04-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=10000)),
                ('placeCity', models.CharField(max_length=20)),
                ('placeCountry', models.CharField(max_length=20)),
                ('dateStart', models.DateField()),
                ('dateEnd', models.DateField()),
            ],
        ),
    ]
