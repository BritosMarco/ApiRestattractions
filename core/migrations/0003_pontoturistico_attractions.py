# Generated by Django 4.1.5 on 2023-01-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
        ('core', '0002_alter_pontoturistico_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='attractions',
            field=models.ManyToManyField(to='attractions.attractions'),
        ),
    ]
