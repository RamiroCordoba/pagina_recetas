# Generated by Django 4.2.5 on 2024-03-28 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetasApp', '0004_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nomUsuario', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'ordering': ['nomUsuario'],
            },
        ),
    ]