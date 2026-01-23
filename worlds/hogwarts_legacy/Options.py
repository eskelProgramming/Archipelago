from dataclasses import dataclass

from Options import Choice, OptionSet, DeathLinkMixin, PerGameCommonOptions, StartInventoryPool

class House(Choice):
    """Defines which house is selected to complete the game. USED FOR HOUSE FLOO FLAME

    - Gryffindor

    - Ravenclaw

    - Hufflepuff

    - Slytherin"""
    display_name = "House"
    option_gryffindor = 0
    option_ravenclaw = 1
    option_hufflepuff = 2
    option_slytherin = 3
    default = 0

@dataclass
class HogwartsLegacyOptions(DeathLinkMixin, PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    house: House