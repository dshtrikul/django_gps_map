# Generated by Django 2.2.3 on 2019-07-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='gps',
            field=models.CharField(default='gps', max_length=100),
        ),
    ]