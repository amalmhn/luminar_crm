# Generated by Django 3.1.6 on 2021-05-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0029_auto_20210513_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('2', 'Admitted'), ('3', 'Cancel'), ('1', 'Call back')], max_length=20),
        ),
    ]