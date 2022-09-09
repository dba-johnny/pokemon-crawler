from django.contrib import admin
from .models import Pokemon, PokemonAbility


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'index', 'height', 'weight', 'species_name']
    list_display_links = ['name']


@admin.register(PokemonAbility)
class PokemonAbilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'index', 'is_hidden', 'slot']
    list_display_links = ['name']

    def get_pokemons(self, instance):
        if instance.pokemons.all():
            return list(instance.pokemons.all().values_list('name', flat=True))
        return 'NA'
