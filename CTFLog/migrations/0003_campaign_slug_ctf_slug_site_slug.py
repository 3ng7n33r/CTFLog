# Generated by Django 4.1.3 on 2022-11-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTFLog', '0002_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='ctf',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]