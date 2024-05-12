# Generated by Django 5.0.4 on 2024-05-08 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestingApp', '0002_remove_comment_qa_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='qa_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='TestingApp.qa_models'),
        ),
    ]
