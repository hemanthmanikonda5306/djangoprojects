# Generated by Django 4.1.3 on 2022-11-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplejwt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simple',
            name='salary',
            field=models.FloatField(default=100000),
        ),
    ]