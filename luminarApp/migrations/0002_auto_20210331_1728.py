# Generated by Django 3.1.6 on 2021-03-31 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='date',
            field=models.DateField(default=datetime.date(2021, 3, 31)),
        ),
        migrations.AlterField(
            model_name='batch',
            name='batch_date',
            field=models.DateField(default=datetime.date(2021, 3, 31)),
        ),
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('2', 'Ongoing'), ('1', 'Yet to Begin'), ('3', 'Completed')], max_length=30),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='enquirydate',
            field=models.DateField(default=datetime.date(2021, 3, 31)),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('2', 'Admitted'), ('1', 'Call back'), ('3', 'Cancel')], max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(default=datetime.date(2021, 3, 31)),
        ),
    ]
