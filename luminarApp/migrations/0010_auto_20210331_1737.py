# Generated by Django 3.1.6 on 2021-03-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0009_auto_20210331_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('1', 'Yet to Begin'), ('3', 'Completed'), ('2', 'Ongoing')], max_length=30),
        ),
    ]
