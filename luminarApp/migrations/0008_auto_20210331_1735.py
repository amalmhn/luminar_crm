# Generated by Django 3.1.6 on 2021-03-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0007_auto_20210331_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('3', 'Cancel'), ('2', 'Admitted'), ('1', 'Call back')], max_length=20),
        ),
    ]
