# Generated by Django 5.0 on 2025-02-03 02:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session_management', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaser_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendees', to='session_management.session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_attendee', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'attendee',
            },
        ),
    ]
