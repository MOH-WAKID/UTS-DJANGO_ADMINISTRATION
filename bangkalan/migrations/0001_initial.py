# Generated by Django 4.2.6 on 2023-11-12 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luas_wilayah', models.CharField(max_length=100)),
                ('penduduk', models.CharField(max_length=100)),
                ('pemerintahan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bangkalan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kota', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bangkalan.profile')),
            ],
        ),
    ]