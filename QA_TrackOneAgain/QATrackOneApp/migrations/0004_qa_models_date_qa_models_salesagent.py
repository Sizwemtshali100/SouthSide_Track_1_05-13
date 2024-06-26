# Generated by Django 5.0.4 on 2024-05-12 13:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QATrackOneApp', '0003_alter_qa_models_agents'),
    ]

    operations = [
        migrations.AddField(
            model_name='qa_models',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qa_models',
            name='SalesAgent',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
