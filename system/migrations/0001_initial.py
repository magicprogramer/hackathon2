# Generated by Django 4.2.7 on 2023-11-16 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=5)),
                ('current_state', models.CharField(max_length=5)),
                ('last_maintanace', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Dragon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
                ('digest_period', models.IntegerField()),
                ('herbivore', models.BooleanField()),
                ('last_meal', models.DateTimeField()),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dragon', to='system.zone')),
            ],
        ),
    ]