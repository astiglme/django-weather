# Generated by Django 5.0.3 on 2024-03-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0003_daytemp_date_daytemp_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytemp',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
