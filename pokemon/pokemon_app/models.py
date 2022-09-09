from django.db import models
from dirtyfields import DirtyFieldsMixin

app_name = 'pokemon_app'


class APIResource(DirtyFieldsMixin, models.Model):
    name = models.CharField(max_length=256, unique=True)
    index = models.IntegerField(unique=True)

    def __str__(self):
        return "%s: %s" % (self.index, self.name)

    class Meta:
        abstract = True
        ordering = ('index', )


class PokemonSpecies(APIResource):
    base_happiness = models.IntegerField()
    capture_rate = models.IntegerField()
    color = models.CharField(max_length=64)
    generation  = models.CharField(max_length=64)
    growth_rate = models.CharField(max_length=64)
    habitat = models.CharField(max_length=64)
    has_gender_differences = models.BooleanField
    is_baby = models.BooleanField()
    is_legendary = models.BooleanField()
    is_mythical = models.BooleanField()
    shape = models.CharField(max_length=64)
    num_varieties = models.IntegerField()

    class Meta(APIResource.Meta):
        db_table = "%s_pokemon_species" % app_name


class Pokemon(APIResource):
    height = models.IntegerField()
    weight = models.IntegerField()
    num_abilities = models.IntegerField()
    num_moves = models.IntegerField()
    base_experience = models.IntegerField(null=True)
    species_name = models.CharField(max_length=64)
    species = models.ForeignKey(PokemonSpecies, on_delete=models.PROTECT, null=True)

    class Meta(APIResource.Meta):
        db_table = "%s_pokemon" % app_name
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'


class PokemonAbility(APIResource):
    pokemons = models.ManyToManyField(Pokemon, related_name='abilities')
    is_hidden = models.BooleanField()
    slot = models.IntegerField()

    class Meta(APIResource.Meta):
        db_table = "%s_pokemon_ability" % app_name
        verbose_name = 'Pokemon Ability'
        verbose_name_plural = 'Pokemon Abilities'
