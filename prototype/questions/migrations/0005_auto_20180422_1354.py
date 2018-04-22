# Generated by Django 2.0.4 on 2018-04-22 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20180422_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='sphere_token',
            new_name='token',
        ),
        migrations.RemoveField(
            model_name='token',
            name='id',
        ),
        migrations.AddField(
            model_name='token',
            name='name',
            field=models.CharField(default='sphere', max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
