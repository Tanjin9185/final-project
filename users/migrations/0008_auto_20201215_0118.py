# Generated by Django 3.1.4 on 2020-12-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201214_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='payment',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Payment Number'),
        ),
    ]
