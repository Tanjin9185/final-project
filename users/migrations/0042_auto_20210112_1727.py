# Generated by Django 3.1.4 on 2021-01-12 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20210112_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='report',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.test'),
        ),
    ]
