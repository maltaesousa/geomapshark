# Generated by Django 2.0.5 on 2018-05-31 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gpf', '0004_auto_20180531_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='actor_ptr',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projectowner',
            name='actor_ptr',
        ),
        migrations.AddField(
            model_name='actor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='ProjectOwner',
        ),
    ]
