# Generated by Django 2.1 on 2020-07-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savtrack', '0005_auto_20200713_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_savings',
            name='Name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
