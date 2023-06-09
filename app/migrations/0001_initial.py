# Generated by Django 4.1.7 on 2023-04-03 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=60)),
                ('firstname', models.TextField()),
                ('lastname', models.TextField()),
                ('address', models.TextField()),
                ('sdt', models.CharField(max_length=11)),
                ('roles', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TraSua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loai', models.TextField()),
                ('kichthuoc', models.CharField(max_length=1)),
                ('gia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DonHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isdeliver', models.BooleanField()),
                ('idts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.trasua')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.account')),
            ],
        ),
    ]
