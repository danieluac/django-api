# Generated by Django 3.2.4 on 2021-08-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
    ]
