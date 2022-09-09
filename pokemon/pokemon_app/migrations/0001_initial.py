# Generated by Django 3.2.15 on 2022-09-08 16:40

import dirtyfields.dirtyfields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('index', models.IntegerField(unique=True)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('num_abilities', models.IntegerField()),
                ('num_moves', models.IntegerField()),
                ('base_experience', models.IntegerField()),
                ('species_name', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'pokemon_app_pokemon',
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PokemonSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('index', models.IntegerField(unique=True)),
                ('base_happiness', models.IntegerField()),
                ('capture_rate', models.IntegerField()),
                ('color', models.CharField(max_length=64)),
                ('generation', models.CharField(max_length=64)),
                ('growth_rate', models.CharField(max_length=64)),
                ('habitat', models.CharField(max_length=64)),
                ('is_baby', models.BooleanField()),
                ('is_legendary', models.BooleanField()),
                ('is_mythical', models.BooleanField()),
                ('shape', models.CharField(max_length=64)),
                ('num_varieties', models.IntegerField()),
            ],
            options={
                'db_table': 'pokemon_app_pokemon_species',
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PokemonAbility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
                ('index', models.IntegerField(unique=True)),
                ('is_hidden', models.BooleanField()),
                ('slot', models.IntegerField()),
                ('pokemons', models.ManyToManyField(related_name='abilities', to='pokemon_app.Pokemon')),
            ],
            options={
                'db_table': 'pokemon_app_pokemon_ability',
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pokemon_app.pokemonspecies'),
        ),
    ]
