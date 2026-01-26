from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import HogwartsLegacyWorld, ancient_magic_hotspots, merlin_trial_locations, astronomy_table_locations, \
    balloon_locations, broom_trial_locations
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
        for location in ancient_magic_hotspots:
            self.location_rules[location] = self.has_ancient_magic
        for location in merlin_trial_locations:
            self.location_rules[location] = self.has_mallowsweet
        for location in astronomy_table_locations:
            self.location_rules[location] = self.has_telescope
        for location in balloon_locations:
            self.location_rules[location] = self.has_broom
        for location in broom_trial_locations:
            self.location_rules[location] = self.has_broom

    def has_ancient_magic(self, state: CollectionState) -> bool:
        return state.has("Ancient Magic", self.player)

    def has_mallowsweet(self, state: CollectionState) -> bool:
        return state.has("Mallowsweet", self.player) or state.has("Mallowsweet Seed", self.player)

    def has_telescope(self, state: CollectionState) -> bool:
        return state.has("Telescope", self.player)

    def has_broom(self, state: CollectionState) -> bool:
        return state.has("Broom", self.player)
