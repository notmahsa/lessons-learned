# Generated by Django 3.2.6 on 2022-08-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_project_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='clark_id',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
