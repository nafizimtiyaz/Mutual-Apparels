# Generated by Django 3.1.4 on 2021-03-15 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0007_auto_20210315_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Sub',
            new_name='subjects',
        ),
    ]
