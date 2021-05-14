# Generated by Django 3.1.6 on 2021-05-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0030_auto_20210513_1510'),
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
            field=models.CharField(choices=[('2', 'Admitted'), ('1', 'Call back'), ('3', 'Cancel')], max_length=20),
        ),
    ]