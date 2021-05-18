# Generated by Django 3.1.6 on 2021-05-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0040_auto_20210517_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('Completed', '3'), ('Yet to Begin', '1'), ('Ongoing', '2')], max_length=30),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('3', 'Cancel'), ('1', 'Call back'), ('2', 'Admitted')], max_length=20),
        ),
    ]
