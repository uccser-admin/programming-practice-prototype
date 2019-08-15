# Generated by Django 2.1.5 on 2019-08-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('user_code', models.TextField()),
                ('passed_tests', models.BooleanField(default=False)),
            ],
        ),
    ]