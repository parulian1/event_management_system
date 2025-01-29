# Generated by Django 5.0 on 2025-01-29 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField()),
                ('capacity', models.IntegerField()),
            ],
            options={
                'db_table': 'track',
            },
        ),
    ]
