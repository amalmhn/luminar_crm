# Generated by Django 3.1.6 on 2021-03-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0011_auto_20210331_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('3', 'Completed'), ('1', 'Yet to Begin'), ('2', 'Ongoing')], max_length=30),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('3', 'Cancel'), ('1', 'Call back'), ('2', 'Admitted')], max_length=20),
        ),
    ]
