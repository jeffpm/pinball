# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player_name', models.CharField(max_length=100)),
                ('ifpa_number', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.BigIntegerField()),
                ('game', models.ForeignKey(to='league.Game')),
                ('player', models.ForeignKey(to='league.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('season_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_date', models.DateField(verbose_name=b'session date')),
                ('session_number', models.IntegerField()),
                ('location', models.ForeignKey(to='league.Location')),
                ('season', models.ForeignKey(to='league.Season')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='score',
            name='session',
            field=models.ForeignKey(to='league.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='player',
            field=models.ForeignKey(to='league.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='session',
            field=models.ForeignKey(to='league.Session'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='location',
            field=models.ForeignKey(to='league.Location'),
            preserve_default=True,
        ),
    ]
