# Generated by Django 3.1.4 on 2021-02-22 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmartFarm', '0005_auto_20201216_0926'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='sensordata',
            table='SENSORVAL',
        ),
    ]
