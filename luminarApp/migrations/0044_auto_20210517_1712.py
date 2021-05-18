# Generated by Django 3.1.6 on 2021-05-17 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('luminarApp', '0043_auto_20210517_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='admission_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='luminarApp.payment'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='status',
            field=models.CharField(choices=[('3', 'Cancel'), ('2', 'Admitted'), ('1', 'Call back')], max_length=20),
        ),
    ]
