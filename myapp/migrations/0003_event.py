# Generated by Django 2.0 on 2019-08-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190813_1139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('url', models.URLField(unique=True)),
                ('created_date', models.DateField()),
                ('place_name', models.CharField(max_length=120)),
                ('place_address', models.CharField(max_length=120)),
                ('place_city', models.CharField(max_length=120)),
                ('place_zipcode', models.CharField(max_length=120)),
                ('place_country', models.CharField(max_length=120)),
            ],
        ),
    ]
