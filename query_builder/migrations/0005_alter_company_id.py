# Generated by Django 4.2.13 on 2024-07-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_builder', '0004_alter_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
