from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from .Locations import locations

if TYPE_CHECKING:
    from . import HogwartsLegacyWorld
else:
    HogwartsLegacyWorld = object


# loosely based on the Inscryption Rules
class HogwartsLegacyRules:
    player: int
    world: HogwartsLegacyWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: HogwartsLegacyWorld) -> None:
        self.player = world.player
        self.world = world

        for location in locations:
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
                elif req == "Lumos":
                    self.location_rules[location.name] = self.has_lumos
                elif req == "Accio":
                    self.location_rules[location.name] = self.has_accio
                elif req == "Levioso":
                    self.location_rules[location.name] = self.has_levioso
                elif req == "Incendio":
                    self.location_rules[location.name] = self.has_incendio


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

    def has_lumos(self, state: CollectionState) -> bool:
        return state.has("Lumos", self.player)

    def has_accio(self, state: CollectionState) -> bool:
        return state.has("Accio", self.player)

    def has_levioso(self, state: CollectionState) -> bool:
        return state.has("Levioso", self.player)

    def has_incendio(self, state: CollectionState) -> bool:
        return state.has("Incendio", self.player)

    def has_final_repository_requirements(self, state: CollectionState) -> bool:
        return state.has("Pensieve Artifact", self.player, 6)

    def set_all_rules(self):
        multiworld = self.world.multiworld

        multiworld.completion_condition[self.player] = self.has_final_repository_requirements

        for location in locations:
            if location.name in self.location_rules:
                location.access_rule = self.location_rules[location.name]
