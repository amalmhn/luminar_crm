# Generated by Django 3.1.6 on 2021-05-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0057_delete_admissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('1', 'Call back'), ('3', 'Cancel'), ('2', 'Admitted')], max_length=20),
        ),
    ]