# Generated by Django 4.2.1 on 2023-08-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_create', '0006_profile_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Usuario', 'Usuario'), ('Funcionario', 'Funcionario'), ('Administrador', 'Administrador')], max_length=100, null=True, verbose_name='Tipo Usuario'),
        ),
    ]