# Generated by Django 4.1.4 on 2022-12-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emsapp', '0016_rename_attend_date_attendance_datetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(max_length=150)),
            ],
        ),
    ]
