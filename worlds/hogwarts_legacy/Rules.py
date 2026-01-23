from typing import TYPE_CHECKING, Callable, Dict

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import HogwartsLegacyWorld
else:
    HogwartsLegacyWorld = object


# Based on Inscryption's implementation
class HogwartsLegacyRules:
    player: int
    world: HogwartsLegacyWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: HogwartsLegacyWorld) -> None:
        self.player = world.player
        self.world = world
        self.location_rules = {
            "Ancient Magic": self.has_ancient_magic,

        }

    def has_ancient_magic(self, state: CollectionState) -> bool:
        return state.has("Ancient Magic", self.player)