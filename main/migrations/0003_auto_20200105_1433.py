# Generated by Django 3.0.2 on 2020-01-05 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200105_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='strhistory',
            old_name='nmbr_cnt',
            new_name='number_count',
        ),
        migrations.RenameField(
            model_name='strhistory',
            old_name='istring',
            new_name='string',
        ),
        migrations.RenameField(
            model_name='strhistory',
            old_name='word_cnt',
            new_name='word_count',
        ),
    ]
