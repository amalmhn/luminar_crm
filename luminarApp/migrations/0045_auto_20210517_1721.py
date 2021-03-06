# Generated by Django 3.1.6 on 2021-05-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0044_auto_20210517_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='admission_no',
            new_name='admission_nos',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('2', 'Admitted'), ('3', 'Cancel'), ('1', 'Call back')], max_length=20),
        ),
    ]
