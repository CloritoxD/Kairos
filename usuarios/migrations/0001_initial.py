# Generated by Django 5.1.2 on 2024-10-18 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=150, unique=True)),
                ('contraseña', models.CharField(max_length=150)),
            ],
        ),
    ]
