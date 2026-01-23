from typing import Mapping, Any

from BaseClasses import Tutorial, Item, Region
from worlds.AutoWorld import WebWorld, World
from worlds.hogwarts_legacy import Rules
from worlds.hogwarts_legacy.Items import spells, goal_items, key_items, non_required_quest_items, potion_recipes_items, \
    seed_items, filler_items, base_id, HogwartsLegacyItem
from worlds.hogwarts_legacy.Locations import floo_flame_locations, ancient_magic_hotspots, bandit_camp_locations, \
    battle_arena_locations, merlin_trial_locations, vendor_locations, astronomy_table_locations, balloon_locations, \
    broom_trial_locations, collection_chest_locations, demiguise_statue_locations, revelio_page_locations, \
    moth_frame_locations, flying_page_locations, orb_statue_page_locations, dragon_brazier_page_locations, \
    landing_platform_locations, quest_locations, house_token_locations
from worlds.hogwarts_legacy.Options import HogwartsLegacyOptions
from worlds.hogwarts_legacy.Regions import hogwarts_regions_all
from worlds.inscryption import regions_to_locations


class HogwartsWeb(WebWorld):
    theme = "party"

    guide_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Hogwarts Legacy Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["eskelProgramming"]
    )

    tutorials = [guide_en]

class HogwartsLegacyWorld(World):
    """
    Hogwarts Legacy is an immersive, open-world action RPG set in the world first introduced in the Harry Potter books.
    For the first time, experience Hogwarts in the 1800s. Your character is a student who holds the key to an ancient
    secret that threatens to tear the wizarding world apart. Now you can take control of the action and be at the
    center of your own adventure in the wizarding world. Your legacy is what you make of it.
    """
    game = "Hogwarts Legacy"
    web = HogwartsWeb()
    options_dataclass = HogwartsLegacyOptions
    options: HogwartsLegacyOptions
    all_items = (spells + goal_items + key_items + non_required_quest_items
                 + potion_recipes_items + seed_items + filler_items)
    item_name_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}
    all_locations = (floo_flame_locations + ancient_magic_hotspots + bandit_camp_locations + battle_arena_locations +
                     merlin_trial_locations + vendor_locations + astronomy_table_locations + balloon_locations +
                     broom_trial_locations + collection_chest_locations + demiguise_statue_locations +
                     revelio_page_locations + revelio_page_locations + moth_frame_locations + flying_page_locations +
                     orb_statue_page_locations + dragon_brazier_page_locations + landing_platform_locations +
                     quest_locations + house_token_locations)

    location_name_to_id = {location: i + base_id for i, location in enumerate(all_locations)}

    def generate_early(self) -> None:
        self.all_items = [item.copy() for item in self.all_items]

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)["name"]

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = self.all_items[item_id - base_id]
        return HogwartsLegacyItem(name , item_data["classification"], item_id, self.player)

    def create_items(self) -> None:
        nb_items_added = 0
        useful_items = self.all_items.copy()

        useful_items = [item for item in useful_items
                        if not any(filler_item["name"] == item["name"] for filler_item in filler_items)]

        for item in useful_items:
            for _ in range(item["count"]):
                new_item = self.create_item(item["name"])
                self.multiworld.itempool.append(new_item)
                nb_items_added += 1

        filler_count = len(self.all_items) - nb_items_added

        for i in range(filler_count):
            index = i % len(filler_items)
            filler_item = filler_items[index]
            new_item = self.create_item(filler_item["name"])
            self.multiworld.itempool.append(new_item)

    def create_regions(self) -> None:
        used_regions = hogwarts_regions_all

        for region_name in used_regions.keys():
            self.multiworld.regions.append(Region(region_name, self.player, self.multiworld))

        for region_name, region_connections in used_regions.items():
            region = self.get_region(region_name)
            region.add_exits(region_connections)
            region.add_locations({
                location: self.location_name_to_id[location] for location in regions_to_locations[region_name]
            })

    def setup(self) -> None:
        Rules.HogwartsLegacyRules(self).set_all_rules()

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "house"
        )
