# Generated by Django 3.1.6 on 2021-03-31 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0008_auto_20210331_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('2', 'Ongoing'), ('1', 'Yet to Begin'), ('3', 'Completed')], max_length=30),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('1', 'Call back'), ('3', 'Cancel'), ('2', 'Admitted')], max_length=20),
        ),
    ]
