from scrapy import Spider, Request
from json import loads
from re import compile as rcompile
from ..items import PokemonItem, PokemonAbilityItem, PokemonSpeciesItem

URL_RE = rcompile('^.*\/(\d+)\/$')


class PokemonSpider(Spider):
    name = "pspider"
    start_urls = ['https://pokeapi.co/api/v2/pokemon/']

    @staticmethod
    def get_index_from_url(url_str):
        mh = URL_RE.match(url_str)
        return int(mh.groups()[0]) if mh else 0

    def parse(self, response, **kwargs):
        page = loads(response.body)
        next_page = page['next']

        for pokemon in page['results']:
            yield Request(url=pokemon['url'], callback=self.parse_pokemon)

            if next_page:
                yield Request(url=next_page)

    def parse_pokemon(self, response, **kwargs):
        pokemon = loads(response.body)
        pokemon_item = PokemonItem(name=pokemon['name'], index=pokemon['id'], height=pokemon['height'],
                                   weight=pokemon['weight'], num_abilities=len(pokemon['abilities']),
                                   num_moves=len(pokemon['moves']), base_experience=pokemon['base_experience'],
                                   species_name=pokemon['species']['name'])

        ability_items = []
        for ability in pokemon['abilities']:
            ability_index = self.get_index_from_url(ability['ability']['url'])
            ability_items.append(PokemonAbilityItem(name=ability['ability']['name'], index=ability_index,
                                                    is_hidden=ability['is_hidden'], slot=ability['slot']))

        yield {'pokemon_item': pokemon_item, 'ability_items': ability_items}

    #   TODO: implement Species parsing, pipline and storage
    #   yield Request(url=pokemon['species']['url'], callback=self.parse_species)

    def parse_species(self, response, **kwargs):
        pass
