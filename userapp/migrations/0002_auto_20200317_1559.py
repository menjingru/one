# Generated by Django 3.0.4 on 2020-03-17 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='ade',
            new_name='age',
        ),
    ]