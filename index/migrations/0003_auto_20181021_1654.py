# Generated by Django 2.1.2 on 2018-10-21 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emergency_contact',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
