# Generated by Django 5.0.4 on 2024-04-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SouthSideApp', '0004_alter_collectionmodel_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionmodel',
            name='JE_Code',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='collectionmodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]