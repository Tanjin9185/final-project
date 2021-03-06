# Generated by Django 3.1.4 on 2020-12-26 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20201226_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='Schedule title'),
        ),
        migrations.AlterField(
            model_name='user',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.schedule'),
        ),
    ]
