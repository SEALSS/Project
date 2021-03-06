# Generated by Django 2.2 on 2019-07-12 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('company_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=70)),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('business_entity', models.CharField(max_length=20)),
                ('company_address', models.CharField(max_length=200)),
                ('pincode', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=500)),
                ('keycontact', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('founded_date', models.CharField(max_length=100)),
                ('number_of_employees', models.CharField(max_length=100)),
                ('transport_type', models.CharField(max_length=100)),
                ('clients', models.CharField(max_length=100)),
                ('office_time_from', models.CharField(max_length=100)),
                ('office_time_to', models.CharField(max_length=100)),
                ('factory_time_from', models.CharField(max_length=100)),
                ('factory_time_to', models.CharField(max_length=100)),
                ('core_operation', models.CharField(max_length=100)),
                ('certifications', models.CharField(max_length=100)),
                ('awards', models.CharField(max_length=100)),
                ('overall_area', models.FloatField(max_length=100)),
                ('built_area', models.FloatField(max_length=100)),
                ('shop_area', models.FloatField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=70, primary_key=True, serialize=False)),
                ('number', models.IntegerField(max_length=200)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]
