# Generated by Django 4.2.2 on 2023-06-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_privmsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='discord_username',
            field=models.TextField(blank=True, max_length=32, null=True),
        ),
    ]
