# Generated by Django 2.2.13 on 2020-06-08 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import votefinder.main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CookieStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cookie', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExecutionMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('thread_id', models.IntegerField(db_index=True, unique=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('max_pages', models.IntegerField()),
                ('current_page', models.IntegerField()),
                ('slug', models.SlugField()),
                ('locked_at', models.DateTimeField(blank=True, null=True)),
                ('state', models.CharField(max_length=32)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('timezone', models.CharField(default='US/Eastern', max_length=128)),
                ('post_lynches', models.BooleanField(default=False)),
                ('ecco_mode', models.BooleanField(default=False)),
                ('last_vc_post', models.DateTimeField(blank=True, null=True)),
                ('is_big', models.BooleanField(default=False)),
                ('current_day', models.IntegerField(default=0)),
                ('living_count', models.IntegerField(default=0)),
                ('players_count', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=models.SET(votefinder.main.models.get_root_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GameFaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faction_name', models.CharField(max_length=255)),
                ('faction_type', models.CharField(choices=[(votefinder.main.models.FactionType('Town'), 'Town'), (votefinder.main.models.FactionType('Scum'), 'Scum'), (votefinder.main.models.FactionType('Third Party'), 'Third Party'), (votefinder.main.models.FactionType('Cult'), 'Cult')], max_length=5)),
                ('winning', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factions', to='main.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('uid', models.IntegerField(db_index=True, unique=True)),
                ('slug', models.SlugField()),
                ('last_post', models.DateTimeField(blank=True, null=True)),
                ('total_posts', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField(db_index=True, unique=True)),
                ('timestamp', models.DateTimeField()),
                ('author_search', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('avatar', models.CharField(max_length=256)),
                ('page_number', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=models.SET(votefinder.main.models.get_default_player), related_name='posts', to='main.Player')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VotecountTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('shared', models.BooleanField(default=False)),
                ('system_default', models.BooleanField(default=False, editable=False)),
                ('overall', models.TextField()),
                ('single_line', models.CharField(max_length=256)),
                ('deadline_exists', models.CharField(max_length=256)),
                ('deadline_not_set', models.CharField(max_length=256)),
                ('before_vote', models.CharField(blank=True, max_length=256)),
                ('after_vote', models.CharField(blank=True, max_length=256)),
                ('before_unvote', models.CharField(blank=True, max_length=256)),
                ('after_unvote', models.CharField(blank=True, max_length=256)),
                ('before_unvoted_vote', models.CharField(blank=True, max_length=256)),
                ('after_unvoted_vote', models.CharField(blank=True, max_length=256)),
                ('detail_level', models.IntegerField(choices=[(1, 'Brief'), (2, 'Medium'), (3, 'Detailed')], default=3)),
                ('hide_zero_votes', models.BooleanField(default=False)),
                ('full_tick', models.CharField(default=f'https://{settings.VF_PRIMARY_DOMAIN}/t.png', max_length=256)),
                ('empty_tick', models.CharField(default=f'https://{settings.VF_PRIMARY_DOMAIN}/te.png', max_length=256)),
                ('creator', models.ForeignKey(editable=False, on_delete=models.SET(votefinder.main.models.get_default_player), to='main.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_string', models.CharField(max_length=256)),
                ('unvote', models.BooleanField(default=False)),
                ('ignored', models.BooleanField(default=False)),
                ('manual', models.BooleanField(default=False)),
                ('nolynch', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='main.Player')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='main.Game')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='main.Post')),
                ('target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target_of_votes', to='main.Player')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('pronouns', models.TextField()),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Player')),
                ('theme', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Theme')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=85)),
                ('icon', models.CharField(max_length=10)),
                ('sent', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=models.SET(votefinder.main.models.get_default_player), related_name='pms_sent', to='main.Player')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pms', to='main.Game')),
                ('target', models.ForeignKey(on_delete=models.SET(votefinder.main.models.get_default_player), related_name='pms_received', to='main.Player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spectator', models.BooleanField(default=False)),
                ('alive', models.BooleanField(default=False)),
                ('moderator', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='main.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='main.Player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerFaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.GameFaction')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factions', to='main.Player')),
            ],
        ),
        migrations.CreateModel(
            name='GameStatusUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=1024)),
                ('url', models.CharField(max_length=255)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Game')),
            ],
        ),
        migrations.CreateModel(
            name='GameDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_number', models.IntegerField(default=1)),
                ('notified', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='main.Game')),
                ('start_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Post')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='moderator',
            field=models.ForeignKey(on_delete=models.SET(votefinder.main.models.get_default_player), related_name='moderatingGames', to='main.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='template',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.VotecountTemplate'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=4096, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Game')),
                ('player', models.ForeignKey(on_delete=models.SET(votefinder.main.models.get_root_user), to='main.Player')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=255)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Player')),
            ],
            options={
                'verbose_name_plural': 'Aliases',
            },
        ),
    ]