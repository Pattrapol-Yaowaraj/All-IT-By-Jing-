# Generated by Django 4.2.5 on 2023-10-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userlink', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkForIT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('major', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
    ]
