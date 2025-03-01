# Generated by Django 4.2.13 on 2024-07-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_builder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='city',
            new_name='domain',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='keyword',
            new_name='locality',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='state',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='company',
            name='employees',
        ),
        migrations.AddField(
            model_name='company',
            name='current_employees',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='linkedin_url',
            field=models.URLField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='size_range',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AddField(
            model_name='company',
            name='total_employees_estimate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
