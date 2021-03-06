# Generated by Django 3.1.6 on 2021-05-18 14:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0062_auto_20210518_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentNewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_date', models.DateField(default=datetime.date(2021, 5, 18))),
                ('admission_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarApp.admissionnewmodel')),
                ('enquiryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarApp.enquirythree')),
            ],
        ),
    ]
