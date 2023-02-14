# Generated by Django 4.1.5 on 2023-01-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=150)),
                ('address2', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(max_length=70)),
                ('state', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=70)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
