# Generated by Django 4.0.5 on 2022-07-02 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curslar', '0003_alter_courses_options_alter_courses_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='idx',
            field=models.IntegerField(default=0),
        ),
    ]
