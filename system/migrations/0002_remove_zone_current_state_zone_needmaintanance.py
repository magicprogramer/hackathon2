# Generated by Django 4.2.7 on 2023-11-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='current_state',
        ),
        migrations.AddField(
            model_name='zone',
            name='needMaintanance',
            field=models.BooleanField(default=False),
        ),
    ]