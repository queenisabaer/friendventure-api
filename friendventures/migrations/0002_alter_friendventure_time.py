# Generated by Django 4.2.7 on 2024-08-15 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendventures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendventure',
            name='time',
            field=models.TimeField(),
        ),
    ]
