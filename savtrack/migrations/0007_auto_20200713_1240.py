# Generated by Django 2.1 on 2020-07-13 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('savtrack', '0006_my_savings_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_savings',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='my_savings',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='my_savings',
            name='year',
        ),
    ]
