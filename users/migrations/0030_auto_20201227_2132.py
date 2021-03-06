# Generated by Django 3.1.4 on 2020-12-27 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20201227_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='schedule',
        ),
        migrations.AddField(
            model_name='schedule',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='test',
            name='reportimg',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=users.models.upload_directory),
        ),
        migrations.AlterField(
            model_name='test',
            name='reportpdf',
            field=models.FileField(blank=True, default='default.pdf', upload_to=users.models.upload_directory),
        ),
    ]
