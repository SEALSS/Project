# Generated by Django 2.2 on 2019-07-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industrydetailsapp', '0003_company_details_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='built_area',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='overall_area',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='shop_area',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(),
        ),
    ]
