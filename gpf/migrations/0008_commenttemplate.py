# Generated by Django 2.0.5 on 2018-06-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0007_merge_20180601_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
