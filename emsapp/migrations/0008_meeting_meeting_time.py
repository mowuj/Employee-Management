# Generated by Django 4.1.3 on 2022-12-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0007_district_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
