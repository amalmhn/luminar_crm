# Generated by Django 3.1.6 on 2021-05-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0054_auto_20210517_1844'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admission',
            new_name='Admissions',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('2', 'Admitted'), ('1', 'Call back'), ('3', 'Cancel')], max_length=20),
        ),
    ]
