# Generated by Django 4.0.5 on 2022-07-01 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curslar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='duration',
            new_name='description',
        ),
    ]
