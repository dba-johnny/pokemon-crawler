
class PokemonPipeline:

    def process_item(self, item, spider):
        pokemon_item = item['pokemon_item']
        ability_items = item['ability_items']

        pokemon = pokemon_item.update_or_create()
        for ability_item in ability_items:
            a = ability_item.update_or_create(pokemon)
        return item


class SpeciesPipeline:

    def process_item(self, item, spider):
        item.update_or_create()
        return item
