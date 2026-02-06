from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from .Locations import world_locations

if TYPE_CHECKING:
    from . import HogwartsLegacyWorld
else:
    HogwartsLegacyWorld = object


# loosely based on the Inscryption Rules
class HogwartsLegacyRules:
    player: int
    world: HogwartsLegacyWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]] = {}
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: HogwartsLegacyWorld) -> None:
        self.player = world.player
        self.world = world
        self.region_rules = {
            "Full Map": self.has_full_map_requirements
        }

        for location in world_locations:
            for req in location.requirements:
                if req == "Ancient Magic":
                    self.location_rules[location.name] = self.has_ancient_magic
                elif req == "Mallowsweet":
                    self.location_rules[location.name] = self.has_mallowsweet
                elif req == "Telescope":
                    self.location_rules[location.name] = self.has_telescope
                elif req == "Broom":
                    self.location_rules[location.name] = self.has_broom
                elif req == "Progressive Alohomora 1":
                    self.location_rules[location.name] = self.has_alohomora_one
                elif req == "Progressive Alohomora 2":
                    self.location_rules[location.name] = self.has_alohomora_two
                elif req == "Progressive Alohomora 3":
                    self.location_rules[location.name] = self.has_alohomora_three
                elif req == "Accio":
                    self.location_rules[location.name] = self.has_accio
                elif req == "Levioso":
                    self.location_rules[location.name] = self.has_levioso
                elif req == "Incendio":
                    self.location_rules[location.name] = self.has_incendio
                elif req == "Reparo":
                    self.location_rules[location.name] = self.has_reparo

    def has_full_map_requirements(self, state: CollectionState) -> bool:
        return state.has_all(["Levioso", "Accio", "Reparo", "Ancient Magic Throw", "Ancient Magic"], self.player)

    def has_ancient_magic(self, state: CollectionState) -> bool:
        return state.has("Ancient Magic", self.player)

    def has_mallowsweet(self, state: CollectionState) -> bool:
        return state.has("Mallowsweet", self.player) or state.has("Mallowsweet Seed", self.player)

    def has_telescope(self, state: CollectionState) -> bool:
        return state.has("Telescope", self.player)

    def has_broom(self, state: CollectionState) -> bool:
        return state.has("Broom", self.player)

    def has_alohomora_one(self, state: CollectionState) -> bool:
        return state.has("Progressive Alohomora", self.player, 1)

    def has_alohomora_two(self, state: CollectionState) -> bool:
        return state.has("Progressive Alohomora", self.player, 2)

    def has_alohomora_three(self, state: CollectionState) -> bool:
        return state.has("Progressive Alohomora", self.player, 3)

    def has_accio(self, state: CollectionState) -> bool:
        return state.has("Accio", self.player)

    def has_levioso(self, state: CollectionState) -> bool:
        return state.has("Levioso", self.player)

    def has_incendio(self, state: CollectionState) -> bool:
        return state.has("Incendio", self.player)

    def has_reparo(self, state: CollectionState) -> bool:
        return state.has("Reparo", self.player)

    def has_final_repository_requirements(self, state: CollectionState) -> bool:
        return state.has("Final Item", self.player, 1)
