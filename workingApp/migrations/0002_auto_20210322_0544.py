# Generated by Django 2.2.12 on 2021-03-22 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(),
        ),
    ]