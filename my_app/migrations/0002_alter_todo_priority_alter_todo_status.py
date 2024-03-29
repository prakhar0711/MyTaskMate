# Generated by Django 4.2.9 on 2024-01-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=15),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], max_length=15),
        ),
    ]
