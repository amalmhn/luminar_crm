# Generated by Django 3.1.6 on 2021-05-17 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0042_auto_20210517_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batch_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarApp.batchstatus'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('2', 'Admitted'), ('1', 'Call back'), ('3', 'Cancel')], max_length=20),
        ),
    ]
