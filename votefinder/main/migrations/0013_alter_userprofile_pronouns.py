# Generated by Django 4.2.2 on 2023-06-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_userprofile_pronouns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pronouns',
            field=models.TextField(blank=True, null=True),
        ),
    ]
