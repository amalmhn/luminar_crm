# Generated by Django 3.1.6 on 2021-04-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0017_auto_20210401_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('1', 'Yet to Begin'), ('2', 'Ongoing'), ('3', 'Completed')], max_length=30),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('2', 'Admitted'), ('3', 'Cancel'), ('1', 'Call back')], max_length=20),
        ),
    ]
