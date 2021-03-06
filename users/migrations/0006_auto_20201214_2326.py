# Generated by Django 3.1.4 on 2020-12-14 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201214_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bma',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='BMA Code'),
        ),
        migrations.AddField(
            model_name='user',
            name='designation',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Designation'),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=11, verbose_name='Mobile Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='nid',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='National ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='payment',
            field=models.CharField(blank=True, max_length=11, verbose_name='Payment Number'),
        ),
        migrations.AddField(
            model_name='user',
            name='specialist',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Specialist'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'admin'), (2, 'lawyer'), (3, 'clients')], default=3, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pm_district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pm_district', to='users.district', verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pm_division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pm_division', to='users.division', verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pm_thana',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pm_thana', to='users.thana', verbose_name='Thana'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ps_district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ps_district', to='users.district', verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ps_division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ps_division', to='users.division', verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ps_thana',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ps_thana', to='users.thana', verbose_name='Thana'),
        ),
    ]
