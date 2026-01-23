from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import HogwartsLegacyWorld
else:
    HogwartsLegacyWorld = object


# Based on Inscryption's implementation
class HogwartsLegacyRules:
    player: int
    world: HogwartsLegacyWorld

    def __init__(self, world: HogwartsLegacyWorld) -> None:
        self.player = world.player
        self.world = world