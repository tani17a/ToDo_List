# Generated by Django 4.1.7 on 2023-03-30 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Task',
            new_name='Tittle',
        ),
    ]
