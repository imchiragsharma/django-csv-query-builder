# Generated by Django 4.2.13 on 2024-07-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_builder', '0006_alter_company_current_employees_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='linkedin_url',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
