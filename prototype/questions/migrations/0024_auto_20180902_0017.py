# Generated by Django 2.0.4 on 2018-09-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0023_auto_20180902_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginday',
            name='day',
            field=models.DateField(auto_now_add=True),
        ),
    ]