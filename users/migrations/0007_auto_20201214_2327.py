# Generated by Django 3.1.4 on 2020-12-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20201214_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'admin'), (2, 'lawyers'), (3, 'clients')], default=3, null=True),
        ),
    ]
