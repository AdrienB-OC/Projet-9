# Generated by Django 4.0.2 on 2022-02-28 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='following',
            new_name='follow',
        ),
    ]
