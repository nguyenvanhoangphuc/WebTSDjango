# Generated by Django 4.1.7 on 2023-04-07 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trasua",
            old_name="gia",
            new_name="price",
        ),
        migrations.RenameField(
            model_name="trasua",
            old_name="kichthuoc",
            new_name="size",
        ),
        migrations.RenameField(
            model_name="trasua",
            old_name="loai",
            new_name="title",
        ),
    ]