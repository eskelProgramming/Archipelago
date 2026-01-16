from typing import Dict, List

from BaseClasses import Location


class HogwartsLegacyLocation(Location):
    game: str = "Hogwarts Legacy"


floo_flame_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Astronomy Tower Floo Flame",
        "Charms Classroom Floo Flame",
        "Defence Against the Dark Arts Tower Floo Flame",
        "Defense Against the Dark Arts Classroom Floo Flame",
        "Professor Fig’s Classroom Floo Flame",
        "Transfiguration Classroom Floo Flame",
        "Transfiguration Courtyard Floo Flame",
        "Bell Tower Courtyard Floo Flame",
        "Flying Class Lawn Floo Flame",
        "Beasts Classroom Floo Flame",
        "Hogwarts North Exit Floo Flame",
        "West Tower Floo Flame",
        "Grand Staircase Floo Flame",
        "Grand Staircase Tower Floo Flame",
        "Lower Grand Staircase Floo Flame",
        "Quad Courtyard Floo Flame",
        "Ravenclaw Tower Floo Flame",
        "Trophy Room Floo Flame",
        "Boathouse Floo Flame",
        "Great Hall Floo Flame",
        "Viaduct Courtyard Floo Flame",
        "Central Hall Floo Flame",
        "Divination Classroom Floo Flame",
        "Greenhouses Floo Flame",
        "Library Floo Flame",
        "Potions Classroom Floo Flame",
        "The Map Chamber Floo Flame",
        "Room of Requirement Floo Flame",
        "Clock Tower Courtyard Floo Flame",
        "Faculty Tower Floo Flame",
        "Gryffindor Common Room Floo Flame",
        "Hospital Wing Floo Flame",  # TODO: Double check if accessible
        "Hogwarts South Exit Floo Flame"
    ],
    "hogsmeade": [
        "South Hogsmeade Floo Flame",
        "West Hogsmeade Floo Flame",
        "North Hogsmeade Floo Flame"
    ],
    "south_hogwarts": [
        "Mooncalf Den Floo Flame",
        "Aranshire Floo Flame",
        "Lower Hogsfield Floo Flame"
    ],
    "north_hogwarts": [
        "The Collector’s Cave Floo Flame",
        "East North Hogwarts Region Floo Flame",
        "Forbidden Forest Floo Flame",
        "Korrow Ruins Floo Flame"
    ],
    "hogsmeade_valley": [
        "Upper Hogsfield Floo Flame",
        "East Hogsmeade Valley Floo Flame",
        "Falbarton Castle Floo Flame"
    ],
    "forbidden_forrest": [
        "West Forbidden Forest Floo Flame",
        "Jackdaw’s Tomb Floo Flame"
    ],
    "north_ford_bog": [
        "Pitt-Upon-Ford Floo Flame",
        "North Ford Bog Floo Flame",
        "San Bakar’s Tower Floo Flame",
        "East North Ford Bog Floo Flame"
    ],
    "hogwarts_valley": [
        "Central Hogwarts Valley Floo Flame",
        "Brocburrow Floo Flame",
        "Keenbridge Floo Flame",
        "The Mine’s Eye Floo Flame"
    ],
    "feldcroft": [
        "West Hogwarts Valley Floo Flame",
        "North Feldcroft Floo Flame",
        "Rookwood Castle Floo Flame",
        "Feldcroft Floo Flame",
        "South Feldcroft Floo Flame",
        "Feldcroft Catacomb Floo Flame",
        "Irondale Floo Flame"
    ],
    "south_sea_bog": [
        "Northern South Sea Bog Floo Flame"
    ],
    "coastal_cavern": [
        "East South Sea Bog Floo Flame",
        "North Poidsear Coast Floo Flame"
    ],
    "poidsear_coast": [
        "Tomb of Treachery Floo Flame",
        "Poidsear Castle Floo Flame",
        "Phoenix Mountain Cave Floo Flame",
        "South Poidsear Coast Floo Flame",
        "Marunweem Bridge Floo Flame"
    ],
    "marunweem_lake": [
        "Coastal Mine Floo Flame",
        "Tower Tunnel Floo Flame",
        "Marunweem Lake Floo Flame",
        "Marunweem Floo Flame",
        "Marunweem Ruins Floo Flame"
    ],
    "cragcrosftshire": [
        "Cragcroft Shore Floo Flame",
        "Cragcroft Floo Flame"
    ],
    "manor_cape": [
        "Bainburgh Floo Flame",
        "West Manor Cape Floo Flame"
    ],
    "clagmar_coast": [
        "Clagmar Castle Floo Flame",
        "South Clagmar Coast Floo Flame"
    ]
}

ancient_magic_hotspots: Dict[str, List[str]] = {
    "north_hogwarts": [
        "North Hogwarts Region Ancient Magic Hotspot"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Ancient Magic Hotspot"
    ],
    "forbidden_forrest": [
        "Forbidden Forest Ancient Magic Hotspot #1",
        "Forbidden Forest Ancient Magic Hotspot #2"
    ],
    "hogwarts_valley": [
        "Hogwarts Valley Ancient Magic Hotspot #1",
        "Hogwarts Valley Ancient Magic Hotspot #2",
        "Hogwarts Valley Ancient Magic Hotspot #3",
        "Hogwarts Valley Ancient Magic Hotspot #4",
        "Hogwarts Valley Ancient Magic Hotspot #5",
        "Hogwarts Valley Ancient Magic Hotspot #6"
    ],
    "feldcroft": [
        "Feldcroft Region Ancient Magic Hotspot #1",
        "Feldcroft Region Ancient Magic Hotspot #2",
        "Feldcroft Region Ancient Magic Hotspot #3",
        "Feldcroft Region Ancient Magic Hotspot #4"
    ],
    "poidsear_coast": [
        "Poidsear Coast Ancient Magic Hotspot #1",
        "Poidsear Coast Ancient Magic Hotspot #2"
    ],
    "marunweem_lake": [
        "Marunweem Lake Ancient Magic Hotspot #1",
        "Marunweem Lake Ancient Magic Hotspot #2"
    ],
    "cragcrosftshire": [
        "CragcrosftShire Ancient Magic Hotspot"
    ],
    "manor_cape": [
        "Manor Cape Ancient Magic Hotspot"
    ]
}

bandit_camp_locations: Dict[str, List[str]] = {
    "north_ford_bog": [
        "North Ford Bandit Camp #1",
        "North Ford Bandit Camp #2",
        "North Ford Bandit Camp #3"
    ],
    "forbidden_forrest": [
        "Forbidden Forrest Bandit Camp #1",
        "Forbidden Forrest Bandit Camp #2",
        "Forbidden Forrest Bandit Camp #3",
        "Forbidden Forrest Bandit Camp #4",
        "Forbidden Forrest Bandit Camp #5"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Bandit Camp #1",
        "Hogsmeade Valley Bandit Camp #2"
    ],
    "north_hogwarts": [
        "North Hogwarts Bandit Camp #1",
        "North Hogwarts Bandit Camp #2",
        "North Hogwarts Bandit Camp #3",
        "North Hogwarts Bandit Camp #4"
    ],
    "hogwarts_valley": [
        "Hogwarts Valley Bandit Camp #1",
        "Hogwarts Valley Bandit Camp #2",
        "Hogwarts Valley Bandit Camp #3"
    ],
    "feldcroft": [
        "Feldcroft Region Bandit Camp #1",
        "Feldcroft Region Bandit Camp #2",
        "Feldcroft Region Bandit Camp #3",
        "Feldcroft Region Bandit Camp #4",
        "Feldcroft Region Bandit Camp #5",
        "Feldcroft Region Bandit Camp #6",
        "Feldcroft Region Bandit Camp #7",
        "Feldcroft Region Bandit Camp #8",
        "Feldcroft Region Bandit Camp #9"
    ],
    "south_sea_bog": [
        "South Sea Bandit Camp"
    ],
    "poidsear_coast": [
        "Poidsear Coast Bandit Camp #1",
        "Poidsear Coast Bandit Camp #2",
        "Poidsear Coast Bandit Camp #3",
        "Poidsear Coast Bandit Camp #4",
        "Poidsear Coast Bandit Camp #5",
        "Poidsear Coast Bandit Camp #6"
    ],
    "marunweem_lake": [
        "Marunweem Lake Bandit Camp #1",
        "Marunweem Lake Bandit Camp #2",
        "Marunweem Lake Bandit Camp #3",
        "Marunweem Lake Bandit Camp #4",
        "Marunweem Lake Bandit Camp #5"
    ],
    "manor_cape": [
        "Manor Cape Bandit Camp #1",
        "Manor Cape Bandit Camp #2"
    ],
    "cragcroftshire": [
        "Cragcroft Shire Bandit Camp"
    ],
    "clagmar_coast": [
        "Clagmar Coast Bandit Camp #1",
        "Clagmar Coast Bandit Camp #2",
        "Clagmar Coast Bandit Camp #3",
        "Clagmar Coast Bandit Camp #4"
    ]
}

battle_arena_locations: Dict[str, List[str]] = {
    "north_ford_bog": [
        "North Fod Bog Battle Arena"
    ],
    "feldcroft": [
        "Feldcroft Battle Arena"
    ]
}

merlin_trial_locations: Dict[str, List[str]] = {
    "north_ford_bog": [
        "North Ford Bog Merlin Trial # 1",
        "North Ford Bog Merlin Trial # 2",
        "North Ford Bog Merlin Trial # 3",
        "North Ford Bog Merlin Trial # 4"
    ],
    "forbidden_forest": [
        "Forbidden Forest Merlin Trial #1",
        "Forbidden Forest Merlin Trial #2",
        "Forbidden Forest Merlin Trial #3"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Merlin Trial #1",
        "Hogsmeade Valley Merlin Trial #2",
        "Hogsmeade Valley Merlin Trial #3",
        "Hogsmeade Valley Merlin Trial #4",
        "Hogsmeade Valley Merlin Trial #5"
    ],
    "north_hogwarts": [
        "North Hogwarts Merlin Trial #1",
        "North Hogwarts Merlin Trial #2",
        "North Hogwarts Merlin Trial #3",
        "North Hogwarts Merlin Trial #4",
        "North Hogwarts Merlin Trial #5"
    ],
    "south-hogwarts": [
        "South Hogwarts Merlin Trial #1",
        "South Hogwarts Merlin Trial #2",
        "South Hogwarts Merlin Trial #3",
        "South Hogwarts Merlin Trial #4",
        "South Hogwarts Merlin Trial #5",
        "South Hogwarts Merlin Trial #6",
        "South Hogwarts Merlin Trial #7",
        "South Hogwarts Merlin Trial #8",
        "South Hogwarts Merlin Trial #9",
        "South Hogwarts Merlin Trial #10",
        "South Hogwarts Merlin Trial #11",
        "South Hogwarts Merlin Trial #12",
        "South Hogwarts Merlin Trial #13",
        "South Hogwarts Merlin Trial #14",
        "South Hogwarts Merlin Trial #15"
    ],
    "hogwarts": [
        "Hogwarts Merlin Trial #1",
        "Hogwarts Merlin Trial #2",
        "Hogwarts Merlin Trial #3",
        "Hogwarts Merlin Trial #4",
        "Hogwarts Merlin Trial #5",
        "Hogwarts Merlin Trial #6",
        "Hogwarts Merlin Trial #7",
        "Hogwarts Merlin Trial #8",
        "Hogwarts Merlin Trial #9",
        "Hogwarts Merlin Trial #10",
        "Hogwarts Merlin Trial #11",
        "Hogwarts Merlin Trial #12",
        "Hogwarts Merlin Trial #13",
        "Hogwarts Merlin Trial #14",
        "Hogwarts Merlin Trial #15",
        "Hogwarts Merlin Trial #16"
    ],
    "feldcroft": [
        "Feldcroft Merlin Trial #1",
        "Feldcroft Merlin Trial #2",
        "Feldcroft Merlin Trial #3",
        "Feldcroft Merlin Trial #4",
        "Feldcroft Merlin Trial #5",
        "Feldcroft Merlin Trial #6",
        "Feldcroft Merlin Trial #7",
        "Feldcroft Merlin Trial #8",
        "Feldcroft Merlin Trial #9",
        "Feldcroft Merlin Trial #10",
        "Feldcroft Merlin Trial #11",
        "Feldcroft Merlin Trial #12",
        "Feldcroft Merlin Trial #13",
        "Feldcroft Merlin Trial #14",
        "Feldcroft Merlin Trial #15",
        "Feldcroft Merlin Trial #16"
    ],
    "south_sea": [
        "South Sea Merlin Trial #1",
        "South Sea Merlin Trial #2"
    ],
    "poidsear": [
        "Poidsear Merlin Trial #1",
        "Poidsear Merlin Trial #2",
        "Poidsear Merlin Trial #3",
        "Poidsear Merlin Trial #4",
        "Poidsear Merlin Trial #5",
        "Poidsear Merlin Trial #6",
        "Poidsear Merlin Trial #7",
        "Poidsear Merlin Trial #8",
        "Poidsear Merlin Trial #9",
        "Poidsear Merlin Trial #10"
    ],
    "marunweem_lake": [
        "Marunweem Lakes Merlin Trial #1",
        "Marunweem Lakes Merlin Trial #2",
        "Marunweem Lakes Merlin Trial #3",
        "Marunweem Lakes Merlin Trial #4"
    ],
    "manor_cape": [
        "Manor Capes Merlin Trial #1",
        "Manor Capes Merlin Trial #2",
        "Manor Capes Merlin Trial #3",
        "Manor Capes Merlin Trial #4",
        "Manor Capes Merlin Trial #5"
    ],
    "cragcroftshire": [
        "Cragcroftshires Merlin Trial #1",
        "Cragcroftshires Merlin Trial #2",
        "Cragcroftshires Merlin Trial #3",
        "Cragcroftshires Merlin Trial #4",
        "Cragcroftshires Merlin Trial #5"
    ],
    "clagmar_coast": [
        "Clagmar Coast Merlin Trial #1",
        "Clagmar Coast Merlin Trial #2",
        "Clagmar Coast Merlin Trial #3",
        "Clagmar Coast Merlin Trial #4",
        "Clagmar Coast Merlin Trial #5"
    ]
}

vendor_locations: Dict[str, List[str]] = {
    "tomes_and_scrolls": [
        "Tomes and Scrolls - Beast Feeder Spellcraft",
        "Tomes and Scrolls - Beast Toybox Spellcraft",
        "Tomes and Scrolls - Chopping Station Spellcraft",
        "Tomes and Scrolls - Dung Composter Spellcraft",
        "Tomes and Scrolls - Hopping Pot Spellcraft",
        "Tomes and Scrolls - Material Refiner Spellcraft",
        "Tomes and Scrolls - Potting Table with One Large Pot Spellcraft",
        "Tomes and Scrolls - Potting Table with Two Large Pots Spellcraft",
        "Tomes and Scrolls - Potting Table with One Medium Pot Spellcraft",
        "Tomes and Scrolls - Potting Table with Two Medium Pots Spellcraft",
        "Tomes and Scrolls - Potting Table with 3 Medium Pots Spellcraft",
        "Tomes and Scrolls - Potting Table with Three Small Pots Spellcraft",
        "Tomes and Scrolls - Potting Table with Five Small Pots Spellcraft",
        "Tomes and Scrolls - Medium Potions Station Spellcraft",
        "Tomes and Scrolls - T-Shaped Potions Station Spellcraft"
    ],
    "spintwitches_sporting_needs": [
        "Spintwitches - Ember Dash Broom",
        "Spintwitches - Hogwarts House Broom",
        "Spintwitches - Moon Trimmer Broom",
        "Spintwitches - Wind Wisp Broom",
        "Spintwitches - Yew Weaver Broom",
    ],
    "j_pippins_potions": [
        "J. Pippin's Potions - Focus Potion Recipe",
        "J. Pippin's Potions - Thunderbrew Potion Recipe",
        "J. Pippin's Potions - Invisibility Potion Recipe",
        "J. Pippin's Potions - Maxima Potion Recipe",
    ],
    "the_magic_neep": [
        "The Magic Neep - Fluxweed Seed",
        "The Magic Neep - Knotgrass Seed",
        "The Magic Neep - Mallowsweet Seed",
        "The Magic Neep - Shrivelfig Seed",
    ],
    "dogweed_and_deathcap": [
        "Dogweed and Deathcap - Chinese Chomping Cabbage Seed",
        "Dogweed and Deathcap - Mandrake Seed",
        "Dogweed and Deathcap - Venomous Tentacula Seed",
    ],
    "gladrags_wizardwear": [
        "Gladrags Wizardwear - Unidentified Head Item",
        "Gladrags Wizardwear - Sanguine Mask",
        "Gladrags Wizardwear - Dark Sun Hat",
        "Gladrags Wizardwear - Sienna Bloom Scarf",
        "Gladrags Wizardwear - Illustrious Emerald Silk Robe",
        "Gladrags Wizardwear - Rugged Fedora",
        "Gladrags Wizardwear - Tettersall Casual School Uniform",
        "Gladrags Wizardwear - Capricious Vest School Uniform",
        "Gladrags Wizardwear - Elegant Vest Uniform",
        "Gladrags Wizardwear - Steel Blue Robe",
        "Gladrags Wizardwear - Aristocratic Ensemble",
        "Gladrags Wizardwear - Spring Ivy Scarf",
        "Gladrags Wizardwear - Mormaer Robes",
        "Gladrags Wizardwear - Secret Solver's Tailor Hat",
        "Gladrags Wizardwear - Black Rivet Gloves",
        "Gladrags Wizardwear - Distinguished School Robe"
    ],
    "edgar_adley": [
        "Edgar Adley - Tartan Vest School Uniform",
        "Edgar Adley - Lace Sorcerer Hat",
        "Edgar Adley - Rapscallion Garb"
    ],
    "arn": [
        "Arn - Silver Arrow Broom"
    ],
    "priya_treadwell": [
        "Priya Treadwell - Family Antique Broom"
    ],
    "agnes_coffey": [
        "Agnes Coffey - Item #1",
        "Agnes Coffey - Item #2",
        "Agnes Coffey - Item #3",
        "Agnes Coffey - Item #4",
        "Agnes Coffey - Item #5",
        "Agnes Coffey - Item #6",
        "Agnes Coffey - Item #7",
        "Agnes Coffey - Item #8"
    ]
}

astronomy_table_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle Astronomy Table - Phoenix"
    ],
    "south_hogwarts": [
        "South Hogwarts Astronomy Table - Lyra"
    ],
    "forbidden_forest": [
        "Forbidden Forest Astronomy Table - Draco"
    ],
    "north_ford_bog": [
        "North Ford Bog Astronomy Table - Centaurus"
    ],
    "hogwarts_valley": [
        "Hogwarts Valley Astronomy Table - Capricornus",
        "Hogwarts Valley Astronomy Table - Corvus"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Astronomy Table - Leo"
    ],
    "feldcroft_region": [
        "Feldcroft Region Astronomy Table - Horologium",
        "Feldcroft Region Astronomy Table - Lacerta"
    ],
    "poidsear_coast": [
        "Poidsear Coast Astronomy Table - Hydra"
    ],
    "marunweem_lake": [
        "Marunweem Lake Astronomy Table - Canis Major"
    ],
    "manor_cape": [
        "Manor Cape Astronomy Table - Sagittarius"
    ],
    "cragcroftshire": [
        "Cragcroftshire Astronomy Table - Cetus"
    ],
    "clagmar_coast": [
        "Clagmar Coast Astronomy Table - Lupus"
    ]
}

balloon_locations: Dict[str, List[str]] = {
    "south_hogwarts": [
        "South Hogwarts Balloon Cluster #1",
        "South Hogwarts Balloon Cluster #2",
        "South Hogwarts Balloon Cluster #3",
        "South Hogwarts Balloon Cluster #4",
        "South Hogwarts Balloon Cluster #5"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Balloon Cluster"
    ],
    "north_hogwarts": [
        "North Hogwarts Balloon Cluster"
    ],
    "north_ford_bog": [
        "North Ford Bog Balloon Cluster #1",
        "North Ford Bog Balloon Cluster #2"
    ],
    "hogwarts_valley": [
        "Hogwarts Valley Balloon Cluster #1",
        "Hogwarts Valley Balloon Cluster #2",
        "Hogwarts Valley Balloon Cluster #3",
        "Hogwarts Valley Balloon Cluster #4",
        "Hogwarts Valley Balloon Cluster #5",
        "Hogwarts Valley Balloon Cluster #6",
        "Hogwarts Valley Balloon Cluster #7"
    ],
    "feldcroft_region": [
        "Feldcroft Region Balloon Cluster #1",
        "Feldcroft Region Balloon Cluster #2",
        "Feldcroft Region Balloon Cluster #3",
        "Feldcroft Region Balloon Cluster #4",
        "Feldcroft Region Balloon Cluster #5",
        "Feldcroft Region Balloon Cluster #6"
    ],
    "coastal_cavern": [
        "Coastal Cavern Balloon Cluster #1"
    ],
    'poidsear_coast': [
        "Poidsear Coast Balloon Cluster #1",
        "Poidsear Coast Balloon Cluster #2",
        "Poidsear Coast Balloon Cluster #3"
    ],
    "marunweem_lake": [
        "Marunweem Lake Balloon Cluster"
    ],
    "manor_cape": [
        "Manor Cape Balloon Cluster #1",
        "Manor Cape Balloon Cluster #2"
    ],
    "cragcroftshire": [
        "CragcroftShire Balloon Cluster #1",
        "CragcroftShire Balloon Cluster #2"
    ],
    "clagmar_coast": [
        "Clagmar Coast Balloon Cluster"
    ]
}

broom_trial_locations: Dict[str, List[str]] = {
    "broom_trials": [
        "Quidditch Pitch Broom Flight Trial",
        "Irondale Broom Flight Trial",
        "South Coast Broom Flight Trial"
    ]
}

collection_chest_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle - Astronomy Wing Chest #1",
        "Hogwarts Castle - Astronomy Wing Chest #2",
        "Hogwarts Castle - Astronomy Wing Chest #3",
        "Hogwarts Castle - Astronomy Wing Chest #4",
        "Hogwarts Castle - Astronomy Wing Chest #5",
        "Hogwarts Castle - Bell Tower Chest #1",
        "Hogwarts Castle - Bell Tower Chest #2",
        "Hogwarts Castle - Bell Tower Chest #3",
        "Hogwarts Castle - Bell Tower Chest #4",
        "Hogwarts Castle - Bell Tower Chest #5",
        "Hogwarts Castle - Bell Tower Chest #6",
        "Hogwarts Castle - Grand Staircase Chest #1",
        "Hogwarts Castle - Grand Staircase Chest #2",
        "Hogwarts Castle - Grand Staircase Chest #3",
        "Hogwarts Castle - Grand Staircase Chest #4",
        "Hogwarts Castle - Grand Staircase Chest #5",
        "Hogwarts Castle - Grand Staircase Chest #6",
        "Hogwarts Castle - Grand Staircase Chest #7",
        "Hogwarts Castle - Great Hall Chest #1",
        "Hogwarts Castle - Great Hall Chest #2",
        "Hogwarts Castle - Great Hall Chest #3",
        "Hogwarts Castle - Library Annex Chest #1",
        "Hogwarts Castle - Library Annex Chest #2",
        "Hogwarts Castle - Library Annex Chest #3",
        "Hogwarts Castle - Library Annex Chest #4",
        "Hogwarts Castle - Library Annex Chest #5",
        "Hogwarts Castle - Library Annex Chest #6",
        "Hogwarts Castle - Library Annex Chest #7",
        "Hogwarts Castle - Library Annex Chest #8",
        "Hogwarts Castle - Library Annex Chest #9",
        "Hogwarts Castle - South Wing Chest #1",
        "Hogwarts Castle - South Wing Chest #2",
        "Hogwarts Castle - South Wing Chest #3",
        "Hogwarts Castle - South Wing Chest #4",
        "Hogwarts Castle - South Wing Chest #5"
    ],
    "hogsmeade_village": [
        "Hogsmeade Village Chest #1",
        "Hogsmeade Village Chest #2",
        "Hogsmeade Village Chest #3",
        "Hogsmeade Village Chest #4",
        "Hogsmeade Village Chest #5"
    ],
    "south_hogwarts": [
        "South Hogwarts Chest #1",
        "South Hogwarts Chest #2",
        "South Hogwarts Chest #3",
        "South Hogwarts Chest #4",
        "South Hogwarts Chest #5",
        "South Hogwarts Chest #6",
        "South Hogwarts Chest #7",
        "South Hogwarts Chest #8",
        "South Hogwarts Chest #9"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Chest #1",
        "Hogsmeade Valley Chest #2",
        "Hogsmeade Valley Chest #3",
        "Hogsmeade Valley Chest #4",
        "Hogsmeade Valley Chest #5",
        "Hogsmeade Valley Chest #6",
        "Hogsmeade Valley Chest #7",
        "Hogsmeade Valley Chest #8"
    ],
    "north_hogwarts": [
        "North Hogwarts Chest #1",
        "North Hogwarts Chest #2",
        "North Hogwarts Chest #3",
        "North Hogwarts Chest #4",
        "North Hogwarts Chest #5",
        "North Hogwarts Chest #6",
        "North Hogwarts Chest #7"
    ],
    "north_ford_bog": [
        "North Ford Bog Chest #1",
        "North Ford Bog Chest #2",
        "North Ford Bog Chest #3",
        "North Ford Bog Chest #4",
        "North Ford Bog Chest #5",
        "North Ford Bog Chest #6",
        "North Ford Bog Chest #7"
    ],
    "hogwarts_valley": [
        "Hogwarts Valley Chest #1",
        "Hogwarts Valley Chest #2",
        "Hogwarts Valley Chest #3",
        "Hogwarts Valley Chest #4",
        "Hogwarts Valley Chest #5",
        "Hogwarts Valley Chest #6",
        "Hogwarts Valley Chest #7",
        "Hogwarts Valley Chest #8",
        "Hogwarts Valley Chest #9",
        "Hogwarts Valley Chest #10",
        "Hogwarts Valley Chest #11",
        "Hogwarts Valley Chest #12",
        "Hogwarts Valley Chest #13",
        "Hogwarts Valley Chest #14",
        "Hogwarts Valley Chest #15"
    ],
    "feldcroft": [
        "Feldcroft Chest #1",
        "Feldcroft Chest #2",
        "Feldcroft Chest #3",
        "Feldcroft Chest #4",
        "Feldcroft Chest #5",
        "Feldcroft Chest #6",
        "Feldcroft Chest #7",
        "Feldcroft Chest #8",
        "Feldcroft Chest #9",
        "Feldcroft Chest #10",
        "Feldcroft Chest #11",
        "Feldcroft Chest #12",
        "Feldcroft Chest #13",
        "Feldcroft Chest #14",
        "Feldcroft Chest #15",
        "Feldcroft Chest #16",
        "Feldcroft Chest #17",
        "Feldcroft Chest #18",
        "Feldcroft Chest #19",
        "Feldcroft Chest #20",
        "Feldcroft Chest #21",
        "Feldcroft Chest #22"
    ],
    "forbidden_forrest": [
        "Forbidden Forrest Chest #1",
        "Forbidden Forrest Chest #2",
        "Forbidden Forrest Chest #3",
        "Forbidden Forrest Chest #4",
        "Forbidden Forrest Chest #5",
        "Forbidden Forrest Chest #6"
    ],
    "south_sea_bog": [
        "South Sea Bog Chest"
    ],
    "coastal_cavern": [
        "Coastal Cavern Chest"
    ],
    "poidsear_coast": [
        "Poidsear Coast Chest #1",
        "Poidsear Coast Chest #2",
        "Poidsear Coast Chest #3",
        "Poidsear Coast Chest #4",
        "Poidsear Coast Chest #5",
        "Poidsear Coast Chest #6",
        "Poidsear Coast Chest #7",
        "Poidsear Coast Chest #8"
    ],
    "marunweem_lake":[
        "Marunweem Lake Chest #1",
        "Marunweem Lake Chest #2",
        "Marunweem Lake Chest #3",
        "Marunweem Lake Chest #4",
        "Marunweem Lake Chest #5",
        "Marunweem Lake Chest #6",
        "Marunweem Lake Chest #7",
        "Marunweem Lake Chest #8",
        "Marunweem Lake Chest #9",
        "Marunweem Lake Chest #10",
        "Marunweem Lake Chest #11",
        "Marunweem Lake Chest #12",
        "Marunweem Lake Chest #13",
        "Marunweem Lake Chest #14",
        "Marunweem Lake Chest #15"
    ],
    "cragcroftshire": [
        "Cragcroftshire Chest #1",
        "Cragcroftshire Chest #2",
        "Cragcroftshire Chest #3",
        "Cragcroftshire Chest #4",
        "Cragcroftshire Chest #5"
    ],
    "clagmar_coast": [
        "Clagmar Coast Chest #1",
        "Clagmar Coast Chest #2",
        "Clagmar Coast Chest #3",
        "Clagmar Coast Chest #4",
        "Clagmar Coast Chest #5"
    ]
}

demiguise_statue_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle Demiguise Statue - Grand Staircase",
        "Hogwarts Castle Demiguise Statue - Hospital Wing",
        "Hogwarts Castle Demiguise Statue - Prefect's Bathroom",
        "Hogwarts Castle Demiguise Statue - Professor Fig's Office",
        "Hogwarts Castle Demiguise Statue - Divination Classroom",
        "Hogwarts Castle Demiguise Statue - Restricted Section Library",
        "Hogwarts Castle Demiguise Statue - Great Hall Room",
        "Hogwarts Castle Demiguise Statue - South Wing Bathroom",
        "Hogwarts Castle Demiguise Statue - North Hall Dungeons",
        "Hogwarts Castle Demiguise Statue - Bell Tower Ramparts",
        "Hogwarts Castle Demiguise Statue - Long Gallery",
        "Hogwarts Castle Demiguise Statue - Defense Against the Dark Arts Tower",
        "Hogwarts Castle Demiguise Statue - Beasts Classroom",
    ],
    "hogsmeade_village": [
        "Hogsmeade Demiguise Statue - Tomes and Scrolls",
        "Hogsmeade Demiguise Statue - Hog's Head Inn",
        "Hogsmeade Demiguise Statue - Dervish and Bangs",
        "Hogsmeade Demiguise Statue - Three Broomsticks",
        "Hogsmeade Demiguise Statue - Spire Street House",
        "Hogsmeade Demiguise Statue - Northern River's Edge Home",
        "Hogsmeade Demiguise Statue - Easternmost House",
        "Hogsmeade Demiguise Statue - Lower High Street",
        "Hogsmeade Demiguise Statue - Western River's Edge Home",
    ],
    "south_hogwarts": [
        "Demiguise Statue - South Hogsfield",
        "Demiguise Statue - Aranshire"
    ],
    "hogsmeade_valley": [
        "Demiguise Statue - Upper Hogsfield"
    ],
    "north_ford_bog": [
        "Demiguise Statue - Pitt-Upon-Ford"
    ],
    "hogwarts_valley": [
        "Demiguise Statue - Brocburrow",
        "Demiguise Statue - Keenbridge"
    ],
    "feldcroft": [
        "Demiguise Statue - Irondale",
        "Demiguise Statue - Feldcroft Village"
    ],
    "marunweem_lake": [
        "Demiguise Statue - Mariweem Hamlet"
    ],
    "manor_cape": [
        "Demiguise Statue - Bainburgh"
    ],
    "cragcrostshire": [
        "Demiguise Statue - Cragcroft"
    ]
}

revelio_page_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle Revelio Page - Astronomy Wing - Tapestry of Barnabas the Barmy",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Astronomy Telescope",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Partial Transfiguration",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Portrait of Baruffio",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Augurey Skeleton",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Boggart Closet",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Dark Tower Cell",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Herbridean Black Skeleton",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Painting of Illyius",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Serpentine Beast Window",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Alchemy Class",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Wyvern Fountain",
        "Hogwarts Castle Revelio Page - Astronomy Wing - Pungent Passage",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Broken Broom",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Flattened Armour",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Goblin Artefact",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Three Sisters Bells",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Scorch Marks",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Grimbald Weft",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Frog Choir",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Waving Knight",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - History of Magic Windows",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Wooden Cat",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Urn of Ashes",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Bloody Meat",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Caged Bathtub",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Glumbumbles",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Castle Ramparts",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Hogwarts Owls",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Quidditch Pitch",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - The Old Librarian",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Important Muggle Artefact",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Sleeping Dragon Statue",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Sphinx Statue",
        "Hogwarts Castle Revelio Page - Bell Tower Wing - Werewolf Saga Tapestries",
        "Hogwarts Castle Revelio Page - Grand Staircase - Salazar Slytherin's Scriptorium",
        "Hogwarts Castle Revelio Page - Grand Staircase - Honeydukes Passageway",
        "Hogwarts Castle Revelio Page - Grand Staircase - Quill of Acceptance and Book of Admittance",
        "Hogwarts Castle Revelio Page - Grand Staircase - Centaur Armour",
        "Hogwarts Castle Revelio Page - Grand Staircase - Moving Staircase",
        "Hogwarts Castle Revelio Page - Grand Staircase - Headmaster's Office Gargoyle",
        "Hogwarts Castle Revelio Page - Grand Staircase - Goblet of Fire Casket",
        "Hogwarts Castle Revelio Page - Grand Staircase - House-Elf Armour",
        "Hogwarts Castle Revelio Page - Grand Staircase - Sleeping Portraits",
        "Hogwarts Castle Revelio Page - Grand Staircase - The Sorting Hat",
        "Hogwarts Castle Revelio Page - Grand Staircase - Troll Armour",
        "Hogwarts Castle Revelio Page - Grand Staircase - Trophy Room",
        "Hogwarts Castle Revelio Page - Grand Staircase - The Hogwarts Architect",
        "Hogwarts Castle Revelio Page - Grand Staircase - Hufflepuff Barrels",
        "Hogwarts Castle Revelio Page - Grand Staircase - House-Elf Recipe Book",
        "Hogwarts Castle Revelio Page - Grand Staircase - Ravenclaw Bust",
        "Hogwarts Castle Revelio Page - Grand Staircase - Ravenclaw Doorknocker",
        "Hogwarts Castle Revelio Page - Grand Staircase - Kelpie Statue",
        "Hogwarts Castle Revelio Page - Great Hall - Black Lake",
        "Hogwarts Castle Revelio Page - Great Hall - Underground Harbour",
        "Hogwarts Castle Revelio Page - Great Hall - The Great Hall Ceiling",
        "Hogwarts Castle Revelio Page - Great Hall - The Yawning Gargoyle",
        "Hogwarts Castle Revelio Page - Great Hall - The Hogwarts Crest",
        "Hogwarts Castle Revelio Page - Great Hall - House Point Hourglasses",
        "Hogwarts Castle Revelio Page - Great Hall - Owl Lectern",
        "Hogwarts Castle Revelio Page - Great Hall - Kitchen Tables",
        "Hogwarts Castle Revelio Page - Great Hall - Pear Portrait",
        "Hogwarts Castle Revelio Page - Great Hall - House-Elf Living Quarters",
        "Hogwarts Castle Revelio Page - Great Hall - Deathday Party Room",
        "Hogwarts Castle Revelio Page - Great Hall - Slytherin's Sink",
        "Hogwarts Castle Revelio Page - Great Hall - Detention Chamber",
        "Hogwarts Castle Revelio Page - Great Hall - Headless Hunt Tapestry",
        "Hogwarts Castle Revelio Page - Library Annex - Arithmancy Classroom",
        "Hogwarts Castle Revelio Page - Library Annex - Central Hall Fountain",
        "Hogwarts Castle Revelio Page - Library Annex - Professor Sharp's Auror Badge",
        "Hogwarts Castle Revelio Page - Library Annex - Gorgon Portrait",
        "Hogwarts Castle Revelio Page - Library Annex - Greenhouse Tree",
        "Hogwarts Castle Revelio Page - Library Annex - Dirigible Plums",
        "Hogwarts Castle Revelio Page - Library Annex - Statue of Gregory the Smarmy",
        "Hogwarts Castle Revelio Page - Library Annex - Enchanted Books",
        "Hogwarts Castle Revelio Page - Library Annex - Palmistry Model",
        "Hogwarts Castle Revelio Page - Library Annex - Book on Intermediate Transfiguration",
        "Hogwarts Castle Revelio Page - Library Annex - Portrait of Sir Cadogan",
        "Hogwarts Castle Revelio Page - South Wing - Clock Mechanics",
        "Hogwarts Castle Revelio Page - South Wing - The Well of Four Beasts",
        "Hogwarts Castle Revelio Page - South Wing - Haunted Toilets",
        "Hogwarts Castle Revelio Page - South Wing - Map of Argyllshire",
        "Hogwarts Castle Revelio Page - South Wing - Boris the Bewildered",
        "Hogwarts Castle Revelio Page - South Wing - Lachlan the Lanky",
        "Hogwarts Castle Revelio Page - South Wing - Adventure Novel Set",
        "Hogwarts Castle Revelio Page - South Wing - Prefect's Bathroom",
        "Hogwarts Castle Revelio Page - South Wing - Jewel-Encrusted Tortoise Shell",
        "Hogwarts Castle Revelio Page - South Wing - Unicorn Fountain",
        "Hogwarts Castle Revelio Page - South Wing - Fat Lady Portrait",
        "Hogwarts Castle Revelio Page - South Hogwarts- Groundskeeper's Tools"
    ],
    "hogsmeade_village": [
        "Hogsmeade Village Revelio Page - Three Broomsticks",
        "Hogsmeade Village Revelio Page - Three Broomsticks Private Room",
        "Hogsmeade Village Revelio Page - Butterbeer Barrels",
        "Hogsmeade Village Revelio Page - Ceridwen's Precarious Caldrons",
        "Hogsmeade Village Revelio Page - Sneakoscope",
        "Hogsmeade Village Revelio Page - The Dogweed and Deathcap Tree",
        "Hogsmeade Village Revelio Page - Hogsmeade Community Garden",
        "Hogsmeade Village Revelio Page - Gladrags Mannequin",
        "Hogsmeade Village Revelio Page - Gladrags Wizardwear",
        "Hogsmeade Village Revelio Page - Hog's Head Docks",
        "Hogsmeade Village Revelio Page - Mounted Hog's Head",
        "Hogsmeade Village Revelio Page - Exploding Bonbons",
        "Hogsmeade Village Revelio Page - Honeydukes",
        "Hogsmeade Village Revelio Page - Fizzing Whizzbees",
        "Hogsmeade Village Revelio Page - The Magic Neep Cart",
        "Hogsmeade Village Revelio Page - Abandoned Shop",
        "Hogsmeade Village Revelio Page - Ollivanders Wand Shop",
        "Hogsmeade Village Revelio Page - J. Pippin's Potions",
        "Hogsmeade Village Revelio Page - Hengist of Woodcroft",
        "Hogsmeade Village Revelio Page - Magical Mail",
        "Hogsmeade Village Revelio Page - Scivenshaft Cats",
        "Hogsmeade Village Revelio Page - Spintwitches Sporting Needs",
        "Hogsmeade Village Revelio Page - Tea Shop Decor",
        "Hogsmeade Village Revelio Page - Enchanted Staircase",
        "Hogsmeade Village Revelio Page - Brood and Peck",
        "Hogsmeade Village Revelio Page - Hogsmeade",
        "Hogsmeade Village Revelio Page - Water Well",
        "Hogsmeade Village Revelio Page - Dungbomb",
        "Hogsmeade Village Revelio Page - Frog Spawn Soap",
        "Hogsmeade Village Revelio Page - Zonko's Joke Shop"
    ],
    "south_hogwarts": [
        "South Hogwarts Revelio Page - Spider Parts",
        "South Hogwarts Revelio Page - Hogsmeade Station Ticket office"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Revelio Page - Beehives",
        "Hogsmeade Valley Revelio Page - Chocolate Frogs",
        "Hogsmeade Valley Revelio Page - Pumpkin Fizz",
        "Hogsmeade Valley Revelio Page - Squib Cottage"
    ],
    "north_hogwarts": [
        "North Hogwarts Revelio Page- Alihotsy Fudge",
    ],
    "north_ford_bog": [
        "North Ford Bog Revelio Page - Antique Horn",
        "North Ford Bog Revelio Page - Spider Sign"
    ],
    "hogwarts_valley" : [
        "Hogwarts Valley Revelio Page - Lace Doily",
        "Hogwarts Valley Revelio Page - Doxy Egg",
        "Hogwarts Valley Revelio Page - Ginger Root",
        "Hogwarts Valley Revelio Page - Hebridean Black Scale",
        "Hogwarts Valley Revelio Page - Murtlap Tentacles",
        "Hogwarts Valley Revelio Page - Runespoor Egg",
        "Hogwarts Valley Revelio Page - Enchanted Scarecrow",
        "Hogwarts Valley Revelio Page - The Tilted House"
    ],
    "feldcroft": [
        "Feldcroft Revelio Page - Broken Binoculars",
        "Feldcroft Revelio Page - Cinnamon Bark",
        "Feldcroft Revelio Page - Practice Dummies",
        "Feldcroft Revelio Page - Jewelled Brooch",
        "Feldcroft Revelio Page - Lovage Bouquet",
        "Feldcroft Revelio Page - Peruvian Instant Darkness Powder",
        "Feldcroft Revelio Page - The Feldcroft Well"
    ],
    "south_sea_bog": [
        "South Sea Bog Revelio Page - Abandoned Bothy"
    ],
    "coastal_cavern": [
        "Coastal Cavern Revelio Page- Antique Compass"
    ],
    "cragcroftshire": [
        "Cragcroftshire Revelio Page - Giant Shade Tree",
        "Cragcroftshire Revelio Page - Dragon Skeleton"
    ],
    "clagmar_coast": [
        "Clagmar Coast Revelio Page - Pungous Onion Bulb",
        "Clagmar Coast Revelio Page - Acromantula Venom"
    ]
}

moth_frame_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle - Astronomy Wing - Astronomy Tower Moth Frame",
        "Hogwarts Castle - Astronomy Wing - Defense Against the Dark Arts Tower Moth Frame",
        "Hogwarts Castle - Astronomy Wing - Tranfiguration Classroom Moth Frame",
        "Hogwarts Castle - Astronomy Wing - Transfiguration Courtyard Moth Frame",
        "Hogwarts Castle - Bell Tower Wing - Hogwarts North Exit Moth Frame",
        "Hogwarts Castle - Grand Staircase - Lower Grand Staircase/Slytherin Dungeon Moth Frame",
        "Hogwarts Castle - Grand Staircase - Ravenclaw Tower Moth Frame",
        "Hogwarts Castle - Grand Staircase - Trophy Room Moth Frame",
        "Hogwarts Castle - Great Hall - Viaduct Courtyard Moth Mirror",
        "Hogwarts Castle - Great Hall - Great Hall Moth Mirror",
        "Hogwarts Castle - Library Annex - Library Moth Frame",
        "Hogwarts Castle - Library Annex - Potions Class Moth Frame",
        "Hogwarts Castle - South Wing - Clock Tower Courtyard (Floo Flame) Moth Frame",
        "Hogwarts Castle - South Wing - Clock Tower Courtyard (Argyllshire Map) Moth Frame",
    ],
    "hogsmeade_village": [
        "Hogsmeade Village - Hog's Head Moth Frame",
        "Hogsmeade Village - Broom Shop Moth Frame",
        "Hogsmeade Village - The Old Fool Moth Frame",
        "Hogsmeade Village - Water Mill Moth Frame",
        "Hogsmeade Village - Dogweed and Deathcap Moth Frame",
    ]
}

flying_page_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle Flying Page - Astronomy Wing - Broken Statue",
        "Hogwarts Castle Flying Page - Astronomy Wing - Defence Against the Dark Arts Tower",
        "Hogwarts Castle Flying Page - Astronomy Wing - Charms Hall",
        "Hogwarts Castle Flying Page - Astronomy Wing - Dungeons",
        "Hogwarts Castle Flying Page - Bell Tower Wing - Bell Tower",
        "Hogwarts Castle Flying Page - Bell Tower Wing - Hogwarts Grounds",
        "Hogwarts Castle Flying Page - Bell Tower Wing - Hieroglyphic Hall",
        "Hogwarts Castle Flying Page - Bell Tower Wing - Beasts Classroom",
        "Hogwarts Castle Flying Page - Bell Tower Wing - Owlery",
        "Hogwarts Castle Flying Page - Grand Staircase - Grand Staircase",
        "Hogwarts Castle Flying Page - Grand Staircase - Quad Courtyard",
        "Hogwarts Castle Flying Page - Great Hall - Great Hall Exterior",
        "Hogwarts Castle Flying Page - Great Hall - Entrance Hall",
        "Hogwarts Castle Flying Page - Great Hall - Deathday Party Room",
        "Hogwarts Castle Flying Page - Library Annex - Central Hall Flying Page #1",
        "Hogwarts Castle Flying Page - Library Annex - Central Hall Flying Page #2",
        "Hogwarts Castle Flying Page - Library Annex - Viaduct Entrance",
        "Hogwarts Castle Flying Page - Library Annex - Library",
        "Hogwarts Castle Flying Page - South Wing - Faculty Tower",
        "Hogwarts Castle Flying Page - South Wing - Hospital Wing",
        "Hogwarts Castle Flying Page - South Wing - Clock Tower"
    ],
    "hogsmeade_village": [
        "Hogsmeade Flying Page – Tomes and Scrolls",
        "Hogsmeade Flying Page #1",
        "Hogsmeade Flying Page #2",
        "Hogsmeade Flying Page #3",
        "Hogsmeade Flying Page #4",
        "Hogsmeade Flying Page #5",
        "Hogsmeade Flying Page #6",
        "Hogsmeade Flying Page #7",
        "Hogsmeade Flying Page #8",
        "Hogsmeade Flying Page #9",
        "Hogsmeade Flying Page #10",
        "Hogsmeade Flying Page #11",
        "Hogsmeade Flying Page #12",
        "Hogsmeade Flying Page #13",
        "Hogsmeade Flying Page #14",
        "Hogsmeade Flying Page #15",
        "Hogsmeade Flying Page #16",
        "Hogsmeade Flying Page #17",
        "Hogsmeade Flying Page #18",
        "Hogsmeade Flying Page #19"
    ]
}

orb_statue_page_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle Orb Statue Page - Astronomy Wing - Transfiguration Class"
        "Hogwarts Castle Orb Statue Page - Astronomy Wing - Astronomy Tower"
        "Hogwarts Castle Orb Statue Page - Astronomy Wing - Dungeons"
        "Hogwarts Castle Orb Statue Page - Bell Tower Wing - Hieroglyphic Hall"
        "Hogwarts Castle Orb Statue Page - Bell Tower Wing - North Hall"
        "Hogwarts Castle Orb Statue Page - Bell Tower Wing - Courtyard"
        "Hogwarts Castle Orb Statue Page - Bell Tower Wing - Owlery"
        "Hogwarts Castle Orb Statue Page - Grand Staircase - Ravenclaw Tower"
        "Hogwarts Castle Orb Statue Page - Great Hall - Entrance Hall Exterior"
        "Hogwarts Castle Orb Statue Page - Great Hall - Entrance Hall Interior"
        "Hogwarts Castle Orb Statue Page - Library Annex - Restricted Section"
        "Hogwarts Castle Orb Statue Page - Library Annex - Central Hall"
        "Hogwarts Castle Orb Statue Page - South Wing - Quad"
        "Hogwarts Castle Orb Statue Page - South Wing - Clock Tower"
        "Hogwarts Castle Orb Statue Page - South Wing - Hospital Wing"
    ]
}

dragon_brazier_page_locations: Dict[str, List[str]] = {
    "hogwarts_castle": [
        "Hogwarts Castle Dragon Brazier - Astronomy Wing - Astronomy Balcony"
        "Hogwarts Castle Dragon Brazier - Bell Tower Wing - Bell Tower"
        "Hogwarts Castle Dragon Brazier - Bell Tower Wing - North Hall"
        "Hogwarts Castle Dragon Brazier - Great Hall - Great Hall"
        "Hogwarts Castle Dragon Brazier - Great Hall - Boathouse"
        "Hogwarts Castle Dragon Brazier - Great Hall - Slytherin Dungeons"
        "Hogwarts Castle Dragon Brazier - Library Annex - Central Hall"
        "Hogwarts Castle Dragon Brazier - South Wing - Gryffindor Tower"
    ]
}

landing_platform_locations: Dict[str, List[str]] = {
    "north_ford_bog": [
        "North Ford Bog Landing Platform"
    ],
    "hogsmeade_valley": [
        "Hogsmeade Valley Landing Platform #1",
        "Hogsmeade Valley Landing Platform #2"
    ],
    "north_hogwarts": [
        "North Hogwarts Landing Platform #1",
        "North Hogwarts Landing Platform #2"
    ],
    "south_hogwarts": [
        "South Hogwarts Landing Platform"
    ],
    "hogwarts_valley": [
        "Hogwarts Valley Landing Platform #1",
        "Hogwarts Valley Landing Platform #2",
        "Hogwarts Valley Landing Platform #3"
    ],
    "feldcroft": [
        "Feldcroft Landing Platform #1",
        "Feldcroft Landing Platform #2",
        "Feldcroft Landing Platform #3",
        "Feldcroft Landing Platform #4"
    ],
    "marunweem_lake": [
        "Marunweem Lake Landing Platform #1",
        "Marunweem Lake Landing Platform #2"
    ],
    "poidsear_coast": [
        "Poidsear Coast Landing Platform"
    ],
    "manor_cape": [
        "Manor Cape Landing Platform #1",
        "Manor Cape Landing Platform #2"
    ],
    "cragcroftshire": [
        "CragcroftShire Landing Platform"
    ],
    "clagmar_coast": [
        "Clagmar Coast Landing Platform"
    ]
}
