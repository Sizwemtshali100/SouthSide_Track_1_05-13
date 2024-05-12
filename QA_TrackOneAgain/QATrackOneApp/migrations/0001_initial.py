# Generated by Django 5.0.4 on 2024-05-10 18:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QA_Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Policy_Number', models.CharField(max_length=12)),
                ('Case_Number', models.CharField(max_length=7)),
                ('AVS_Check', models.CharField(choices=[('PASS', 'PASS'), ('FAIL', 'FAIL'), ('UNVERIFIED', 'UNVERIFIED')], max_length=12)),
                ('Caller_ID', models.CharField(max_length=50)),
                ('Call_duration', models.CharField(max_length=10)),
                ('Start_date', models.CharField(choices=[('1st January', '1st January'), ('1st February', '1st February'), ('1st March', '1st March'), ('1st April', '1st April'), ('1st May', '1st May'), ('1st June', '1st June'), ('1st July', '1st July'), ('1st August', '1st August'), ('1st September', '1st September'), ('1st October', '1st October'), ('1st November', '1st November'), ('1st December', '1st December')], max_length=20)),
                ('Premium', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Debit_date', models.CharField(max_length=10)),
                ('Cover_amount', models.CharField(max_length=10)),
                ('QA_Correct', models.CharField(choices=[('FALSE', 'FALSE'), ('TRUE', 'TRUE')], max_length=5)),
                ('KPA_1', models.CharField(choices=[('Product', 'Product'), ('Pass', 'Pass'), ('Compliance', 'Compliance'), ('Data Capturing', 'Data Capturing'), ('TCF', 'TCF')], max_length=15, null=True)),
                ('KPA_2', models.CharField(choices=[('Product', 'Product'), ('Pass', 'Pass'), ('Compliance', 'Compliance'), ('Data Capturing', 'Data Capturing'), ('TCF', 'TCF')], max_length=15, null=True)),
                ('KPA_3', models.CharField(choices=[('Product', 'Product'), ('Pass', 'Pass'), ('Compliance', 'Compliance'), ('Data Capturing', 'Data Capturing'), ('TCF', 'TCF')], max_length=15, null=True)),
                ('HIV_Required', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3)),
                ('Comment', models.TextField(max_length=200)),
                ('Agents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
