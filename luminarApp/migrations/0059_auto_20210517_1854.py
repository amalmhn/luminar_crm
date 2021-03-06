# Generated by Django 3.1.6 on 2021-05-17 18:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0058_auto_20210517_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('2', 'Admitted'), ('3', 'Cancel'), ('1', 'Call back')], max_length=20),
        ),
        migrations.CreateModel(
            name='Admissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(max_length=50, unique=True)),
                ('coursefees', models.IntegerField()),
                ('date', models.DateField(default=datetime.date(2021, 5, 17))),
                ('batchcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarApp.batch')),
                ('enquiryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarApp.enquirythree')),
            ],
        ),
    ]
