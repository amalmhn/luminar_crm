# Generated by Django 3.1.6 on 2021-05-14 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0037_auto_20210514_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='enquiryid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarApp.enquirythree'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.CharField(choices=[('1', 'Yet to Begin'), ('2', 'Ongoing'), ('3', 'Completed')], max_length=30),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('3', 'Cancel'), ('2', 'Admitted'), ('1', 'Call back')], max_length=20),
        ),
    ]
