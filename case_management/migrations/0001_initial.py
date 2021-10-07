# Generated by Django 3.2.4 on 2021-06-23 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referrer', models.CharField(max_length=40)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case_management.person')),
            ],
            options={
                'db_table': 'referral',
            },
        ),
    ]