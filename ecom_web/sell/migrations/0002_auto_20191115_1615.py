# Generated by Django 2.2.4 on 2019-11-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]