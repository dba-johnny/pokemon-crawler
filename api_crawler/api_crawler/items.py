import logging
from scrapy_djangoitem import DjangoItem
from pokemon_app.models import Pokemon, PokemonSpecies, PokemonAbility


class PokemonItem(DjangoItem):
    django_model = Pokemon

    def update_or_create(self):
        # we assume name and index can't change as these are primary key fields
        try:  # outer try/except: to catch any unexpected exceptions whilst exception handling
            try:
                p = Pokemon.objects.get(index=self['index'])
                p.height = self['height']
                p.weight = self['weight']
                p.num_abilities = self['num_abilities']
                p.num_moves = self['num_moves']
                p.base_experience = self['base_experience']
                p.species_name = self['species_name']
                if p.is_dirty():
                    p.save()
                return p
            except self.django_model.DoesNotExist:
                self.save()
                return self.instance
        except Exception as err:
            logging.error('api_crawler.items.PokemonItem.update_or_create: Unexpected Error: %s' % str(err))


class PokemonAbilityItem(DjangoItem):
    django_model = PokemonAbility

    def update_or_create(self, pokemon_instance):
        ap = PokemonAbility.objects.prefetch_related('pokemons').filter(index=self['index'])
        try:  # outer try/except: to catch any unexpected exceptions whilst exception handling
            try:
                a = ap.get()
                a.is_hidden = self['is_hidden']
                a.slot = self['slot']
                if a.is_dirty():
                    a.save()
                # if 'a' already links to 'pokemon_instance' via m2m, the following add() call with do nothing
                a.pokemons.add(pokemon_instance)
                return a
            except self.django_model.DoesNotExist:
                self.save()
                # the following add() call will save entry in m2m table automatically
                self.instance.pokemons.add(pokemon_instance)
                return self.instance
        except Exception as err:
            logging.error('api_crawler.items.PokemonAbilityItem.update_or_create: Unexpected Error: %s' % str(err))


class PokemonSpeciesItem(DjangoItem):
    django_model = PokemonSpecies
