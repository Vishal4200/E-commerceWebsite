# Generated by Django 3.0.2 on 2020-02-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200205_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]
