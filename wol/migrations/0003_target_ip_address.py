# Generated by Django 2.1.3 on 2018-11-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wol', '0002_auto_20181122_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='ip_address',
            field=models.GenericIPAddressField(default='255.255.255.255'),
        ),
    ]
