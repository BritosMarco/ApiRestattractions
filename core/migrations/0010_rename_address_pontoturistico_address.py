# Generated by Django 4.1.5 on 2023-02-13 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_pontoturistico_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pontoturistico',
            old_name='Address',
            new_name='address',
        ),
    ]
