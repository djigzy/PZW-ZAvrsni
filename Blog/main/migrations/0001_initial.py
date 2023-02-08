# Generated by Django 4.1.4 on 2022-12-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, verbose_name='Ime')),
                ('user_name', models.CharField(max_length=64, null=True, verbose_name='Korisnicko ime')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('password', models.CharField(max_length=20, null=True, verbose_name='Lozinka')),
            ],
        ),
    ]
