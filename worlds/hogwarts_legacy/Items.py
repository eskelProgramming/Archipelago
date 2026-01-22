from typing import TypedDict, List

from BaseClasses import Item, ItemClassification


class HogwartsLegacyItem(Item):
    name: str = "Hogwarts Legacy"

class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification

spells: List[ItemDict] = [
    {
        "name": "Arresto Momentum",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Glacius",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Levioso",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Transformation",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Accio",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Depulso",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Descendor",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Flipendo",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Confringo",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Diffindo",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Expelliarmus",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Bombarda",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Incendio",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Disillusionment",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Reparo",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Wingardium Leviosa",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Conjuring Spell",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Altering Spell",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Avada Kedavra",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Crucio",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Imperio",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Beast Petting Brush",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Beast Feed",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Nab-Sack",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Ancient Magic Throw",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Ancient Magic",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Alohomora - Progressive",
        "count": 3,
        "classification": ItemClassification.progression
    }
]

key_items = [
    {
        "name": "Pensieve Artifact",
        "count": 6,
        "classification": ItemClassification.progression_skip_balancing
    },
    {
        "name": "Telescope",
        "count": 1,
        "classification": ItemClassification.progression
    },
    {
        "name": "Broom",
        "count": 1,
        "classification": ItemClassification.progression
    }
]

non_required_quest_items = [
    {
        "name": "Demiguise Moon",
        "count": 30,
        "classification": ItemClassification.useful
    },
    {
        "name": "House Token",
        "count": 16,
        "classification": ItemClassification.useful
    }
]

potion_recipes_items = [
    {
        "name": "Wiggenweld Potion Recipe",
        "count": 1,
        "classification": ItemClassification.progression # Required for Potions Class
    },
    {
        "name": "Focus Potion Recipe",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Edurus Potion Recipe",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Invisibility Potion Recipe",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Maxima Potion Recipe",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Thunderbrew Potion Recipe",
        "count": 1,
        "classification": ItemClassification.useful
    }
]

seed_items = [
    {
        "name": "Knotgrass Seed",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Dittany Seed",
        "count": 1,
        "classification": ItemClassification.progression # required for Herbology Class
    },
    {
        "name": "Mallowsweet Seed",
        "count": 1,
        "classification": ItemClassification.progression # required for Merlin Trials
    },
    {
        "name": "Fluxweed Seed",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Shrivelfig Seed",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Chinese Chomping Cabbage Seed",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Mandrake Seed",
        "count": 1,
        "classification": ItemClassification.useful
    },
    {
        "name": "Venomous Tentacula Seed",
        "count": 1,
        "classification": ItemClassification.useful
    }
]

filler_items = [
    {
        "name": "Galleons",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Wiggenweld Potions",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Chinese Chomping Cabbage",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Focus Potion",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Edurus Potion",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Invisibility Potion",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Mandrake",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Maxima Potion",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Thunderbrew Potion",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name" : "Venomous Tentacula",
        "count": 1,
        "classification": ItemClassification.filler
    },
    {
        "name": "Mallowsweet",
        "count": 1,
        "classification": ItemClassification.filler
    }
]
