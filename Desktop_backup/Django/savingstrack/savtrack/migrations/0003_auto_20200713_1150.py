# Generated by Django 2.1 on 2020-07-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savtrack', '0002_auto_20200629_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_savings',
            name='transaction_amt',
            field=models.IntegerField(null=True),
        ),
    ]