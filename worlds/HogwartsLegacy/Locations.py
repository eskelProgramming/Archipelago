from typing import Dict, List

from BaseClasses import Location


class HogwartsLegacyLocation(Location):
    game: str = "Hogwarts Legacy"

floo_flame_locations: Dict[str, List[str]] = {
    "hogwarts_castle" : [
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
        "Hospital Wing Floo Flame", # TODO: Double check if accessible
        "Hogwarts South Exit Floo Flame"
    ],
    "hogsmeade" : [
        "South Hogsmeade Floo Flame",
        "West Hogsmeade Floo Flame",
        "North Hogsmeade Floo Flame"
    ],
    "south_hogwarts" : [
        "Mooncalf Den Floo Flame",
        "Aranshire Floo Flame",
        "Lower Hogsfield Floo Flame"
    ],
    "north_hogwarts" : [
        "The Collector’s Cave Floo Flame",
        "East North Hogwarts Region Floo Flame",
        "Forbidden Forest Floo Flame",
        "Korrow Ruins Floo Flame"
    ],
    "hogsmeade_valley" : [
        "Upper Hogsfield Floo Flame",
        "East Hogsmeade Valley Floo Flame",
        "Falbarton Castle Floo Flame"
    ],
    "forbidden_forrest" : [
        "West Forbidden Forest Floo Flame",
        "Jackdaw’s Tomb Floo Flame"
    ],
    "north_ford_bog" : [
        "Pitt-Upon-Ford Floo Flame",
        "North Ford Bog Floo Flame",
        "San Bakar’s Tower Floo Flame",
        "East North Ford Bog Floo Flame"
    ],
    "hogwarts_valley" : [
        "Central Hogwarts Valley Floo Flame",
        "Brocburrow Floo Flame",
        "Keenbridge Floo Flame",
        "The Mine’s Eye Floo Flame"
    ],
    "feldcroft" : [
        "West Hogwarts Valley Floo Flame",
        "North Feldcroft Floo Flame",
        "Rookwood Castle Floo Flame",
        "Feldcroft Floo Flame",
        "South Feldcroft Floo Flame",
        "Feldcroft Catacomb Floo Flame",
        "Irondale Floo Flame"
    ],
    "south_sea_bog" : [
        "Northern South Sea Bog Floo Flame"
    ],
    "coastal_cavern" : [
        "East South Sea Bog Floo Flame",
        "North Poidsear Coast Floo Flame"
    ],
    "poidsear_coast" : [
        "Tomb of Treachery Floo Flame",
        "Poidsear Castle Floo Flame",
        "Phoenix Mountain Cave Floo Flame",
        "South Poidsear Coast Floo Flame",
        "Marunweem Bridge Floo Flame"
    ],
    "marunweem_lake" : [
        "Coastal Mine Floo Flame",
        "Tower Tunnel Floo Flame",
        "Marunweem Lake Floo Flame",
        "Marunweem Floo Flame",
        "Marunweem Ruins Floo Flame"
    ],
    "cragcrosftshire" : [
        "Cragcroft Shore Floo Flame",
        "Cragcroft Floo Flame"
    ],
    "manor_cape" : [
        "Bainburgh Floo Flame",
        "West Manor Cape Floo Flame"
    ],
    "clagmar_coast" : [
        "Clagmar Castle Floo Flame",
        "South Clagmar Coast Floo Flame"
    ]
}

ancient_magic_hotspots: Dict[str, List[str]] = {
    "north_hogwarts" : [
        "North Hogwarts Region Ancient Magic Hotspot"
    ],
    "hogsmeade_valley" : [
        "Hogsmeade Valley Ancient Magic Hotspot"
    ],
    "forbidden_forrest" : [
        "Forbidden Forest Ancient Magic Hotspot #1",
        "Forbidden Forest Ancient Magic Hotspot #2"
    ],
    "hogwarts_valley" : [
        "Hogwarts Valley Ancient Magic Hotspot #1",
        "Hogwarts Valley Ancient Magic Hotspot #2",
        "Hogwarts Valley Ancient Magic Hotspot #3",
        "Hogwarts Valley Ancient Magic Hotspot #4",
        "Hogwarts Valley Ancient Magic Hotspot #5",
        "Hogwarts Valley Ancient Magic Hotspot #6"
    ],
    "feldcroft" : [
        "Feldcroft Region Ancient Magic Hotspot #1",
        "Feldcroft Region Ancient Magic Hotspot #2",
        "Feldcroft Region Ancient Magic Hotspot #3",
        "Feldcroft Region Ancient Magic Hotspot #4"
    ],
    "poidsear_coast" : [
        "Poidsear Coast Ancient Magic Hotspot #1",
        "Poidsear Coast Ancient Magic Hotspot #2"
    ],
    "marunweem_lake" : [
        "Marunweem Lake Ancient Magic Hotspot #1",
        "Marunweem Lake Ancient Magic Hotspot #2"
    ],
    "cragcrosftshire" : [
        "CragcrosftShire Ancient Magic Hotspot"
    ],
    "manor_cape" : [
        "Manor Cape Ancient Magic Hotspot"
    ]
}

bandit_camp_locations: Dict[str, List[str]] = {
    "north_ford_bog" : [
        "North Ford Bandit Camp #1",
        "North Ford Bandit Camp #2",
        "North Ford Bandit Camp #3"
    ],
    "forbidden_forrest" : [
        "Forbidden Forrest Bandit Camp #1",
        "Forbidden Forrest Bandit Camp #2",
        "Forbidden Forrest Bandit Camp #3",
        "Forbidden Forrest Bandit Camp #4",
        "Forbidden Forrest Bandit Camp #5"
    ],
    "hogsmeade_valley" : [
        "Hogsmeade Valley Bandit Camp #1",
        "Hogsmeade Valley Bandit Camp #2"
    ],
    "north_hogwarts" : [
        "North Hogwarts Bandit Camp #1",
        "North Hogwarts Bandit Camp #2",
        "North Hogwarts Bandit Camp #3",
        "North Hogwarts Bandit Camp #4"
    ],
    "hogwarts_valley" : [
        "Hogwarts Valley Bandit Camp #1",
        "Hogwarts Valley Bandit Camp #2",
        "Hogwarts Valley Bandit Camp #3"
    ],
    "feldcroft" : [
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
    "south_sea_bog" : [
        "South Sea Bandit Camp"
    ],
    "poidsear_coast" : [
        "Poidsear Coast Bandit Camp #1",
        "Poidsear Coast Bandit Camp #2",
        "Poidsear Coast Bandit Camp #3",
        "Poidsear Coast Bandit Camp #4",
        "Poidsear Coast Bandit Camp #5",
        "Poidsear Coast Bandit Camp #6"
    ],
    "marunweem_lake" : [
        "Marunweem Lake Bandit Camp #1",
        "Marunweem Lake Bandit Camp #2",
        "Marunweem Lake Bandit Camp #3",
        "Marunweem Lake Bandit Camp #4",
        "Marunweem Lake Bandit Camp #5"
    ],
    "manor_cape" : [
        "Manor Cape Bandit Camp #1",
        "Manor Cape Bandit Camp #2"
    ],
    "cragcroftshire" : [
        "Cragcroft Shire Bandit Camp"
    ],
    "clagmar_coast" : [
        "Clagmar Coast Bandit Camp #1",
        "Clagmar Coast Bandit Camp #2",
        "Clagmar Coast Bandit Camp #3",
        "Clagmar Coast Bandit Camp #4"
    ]
}

battle_arena_locations: Dict[str, List[str]] = {
    "north_ford_bog" : [
        "North Fod Bog Battle Arena"
    ],
    "feldcroft" : [
        "Feldcroft Battle Arena"
    ]
}

merlin_trial_locations: Dict[str, List[str]] = {
    "north_ford_bog" : [
        "North Ford Bog Merlin Trial # 1",
        "North Ford Bog Merlin Trial # 2",
        "North Ford Bog Merlin Trial # 3",
        "North Ford Bog Merlin Trial # 4"
    ],
    "forbidden_forest" : [
        "Forbidden Forest Merlin Trial #1",
        "Forbidden Forest Merlin Trial #2",
        "Forbidden Forest Merlin Trial #3"
    ],
    "hogsmeade_valley" : [
        "Hogsmeade Valley Merlin Trial #1",
        "Hogsmeade Valley Merlin Trial #2",
        "Hogsmeade Valley Merlin Trial #3",
        "Hogsmeade Valley Merlin Trial #4",
        "Hogsmeade Valley Merlin Trial #5"
    ],
    "north_hogwarts" : [
        "North Hogwarts Merlin Trial #1",
        "North Hogwarts Merlin Trial #2",
        "North Hogwarts Merlin Trial #3",
        "North Hogwarts Merlin Trial #4",
        "North Hogwarts Merlin Trial #5"
    ],
    "south-hogwarts" : [
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
    "hogwarts" : [
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
    "feldcroft" : [
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
    "south_sea" : [
        "South Sea Merlin Trial #1",
        "South Sea Merlin Trial #2"
    ],
    "poidsear" : [
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
    "marunweem_lake" : [
        "Marunweem Lakes Merlin Trial #1",
        "Marunweem Lakes Merlin Trial #2",
        "Marunweem Lakes Merlin Trial #3",
        "Marunweem Lakes Merlin Trial #4"
    ],
    "manor_cape" : [
        "Manor Capes Merlin Trial #1",
        "Manor Capes Merlin Trial #2",
        "Manor Capes Merlin Trial #3",
        "Manor Capes Merlin Trial #4",
        "Manor Capes Merlin Trial #5"
    ],
    "cragcroftshire" : [
        "Cragcroftshires Merlin Trial #1",
        "Cragcroftshires Merlin Trial #2",
        "Cragcroftshires Merlin Trial #3",
        "Cragcroftshires Merlin Trial #4",
        "Cragcroftshires Merlin Trial #5"
    ],
    "clagmar_coast" : [
        "Clagmar Coast Merlin Trial #1",
        "Clagmar Coast Merlin Trial #2",
        "Clagmar Coast Merlin Trial #3",
        "Clagmar Coast Merlin Trial #4",
        "Clagmar Coast Merlin Trial #5"
    ]
}
