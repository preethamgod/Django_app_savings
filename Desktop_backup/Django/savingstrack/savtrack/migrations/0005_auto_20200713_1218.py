# Generated by Django 2.1 on 2020-07-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savtrack', '0004_auto_20200713_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_savings',
            name='sa_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='my_savings',
            name='transaction_amt',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
