# Generated by Django 2.2.1 on 2019-06-26 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamName', models.CharField(default='', max_length=100)),
                ('League', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ('TeamName',),
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('Age', models.IntegerField(default='')),
                ('Club', models.TextField()),
                ('Position', models.TextField()),
                ('Birthdate', models.DateField(max_length=100)),
                ('Nationality', models.CharField(max_length=100)),
                ('InfoId', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Player_id', to='footballapp.Team')),
            ],
            options={
                'ordering': ('Name',),
            },
        ),
    ]
