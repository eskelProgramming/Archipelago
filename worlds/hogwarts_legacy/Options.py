from Options import Choice, OptionSet


class Goal(Choice):
    """Defines the Goal to complete the game

    - Defeat Ranrok: Collect the 6 Pensive Artifacts, Completing the "Wand Mastery" Quest and Completing the "The Final
    Repository" Quest

    - Go to Class: Go To Each Class (Defense Against the Dark Arts, Charms, Potions, Herbology, Flying,
    Beasts, Astronomy, History of Magic)"""
    display_name = "Goal"
    option_ranrok = 0
    option_classes = 1
    default = 0

class Locations(OptionSet):
    """Defines the Locations Checks can be in.

    - Floo Flames: Each Floo Flame is a Check

    - Ancient Magic Hotspots: Each Magic Hotspot is a Check

    - Bandit Camps: Each Bandit Camp Collection Chest is a Check

    - Battle Arenas: Both Battle Arenas (DLC Arena not included) are Checks

    - Merlin Trials: Each Merlin Trial is a Check

    - Vendors: Some Vendors have Checks for purchase

    - Astronomy Tables: Each Astronomy Table Location is a Check

    - Ballons: Each Broom Ballon set is a Check

    - Broom Trials: Each Broom Trial is a Check

    - Collection Chests: Each Collection Chest is a Check

    - Demiguise Statues: Each Demiguise Statue is a Check

    - Revelio Pages: Each Revelio Page is a Check

    - Moth Frame Pages: Each Moth Frame Page is a Check

    - Flying Pages: Each Flying Page is a Check

    - Orb Statue(Levioso Statue) Pages : Each Orb Statue Page is a Check

    - Dragon Brazier Pages: Each Dragon Brazier Page is a Check

    - Landing Platforms: Each Landing Platform is a Check

    - Quests: Each Quest is a Check

    - House Tokens(Daedalian Keys): Each House Tokens is a Check"""
    display_name = "Check Locations"
    valid_keys = ["Floo Flames", "Ancient Magic Hotspots", "Bandit Camps", "Battle Arenas", "Merlin Trials",
                  "Vendors", "Astronomy Tables", "Broom Trials", "Collection Chests", "Demiguise Statues",
                  "Revelio Pages", "Moth Frame Pages", "Flying Pages", "Orb Statues", "Dragon Brazier Pages",
                  "Landing Platforms", "Quests", "House Tokens"]

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
