# Generated by Django 4.2.1 on 2023-08-08 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_create', '0004_remove_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name='Idade'),
        ),
    ]
