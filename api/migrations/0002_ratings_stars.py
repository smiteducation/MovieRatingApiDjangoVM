# Generated by Django 3.2.5 on 2021-07-21 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='stars',
            field=models.IntegerField(default=1),
        ),
    ]
