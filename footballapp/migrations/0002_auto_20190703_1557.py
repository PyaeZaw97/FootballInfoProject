# Generated by Django 2.2.1 on 2019-07-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Position',
            field=models.CharField(max_length=100),
        ),
    ]
