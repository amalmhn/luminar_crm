# Generated by Django 3.1.6 on 2021-05-17 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0039_auto_20210517_1506'),
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
            field=models.CharField(choices=[('1', 'Call back'), ('3', 'Cancel'), ('2', 'Admitted')], max_length=20),
        ),
    ]
