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

    
