#==========================================#
#                                          #
#       Kovar's Intensity Calculator       #
#             Updated: 8/11/24             #
#       Uses UO-CAH Intensity Values       #
#                                          #
#                                          #
#==========================================#

cliloc_abilities_dict = {
    1028838: "Armor Ignore",
    1028840: "Concussion Blow",
    1028841: "Crushing Blow",
    1028842: "Disarm",
    1028843: "Dismount",
    1028846: "Mortal Strike",
    1028852: "Frenzied Whirlwind",
    1028853: "Block",
    1028854: "Defense Mastery",
    1028855: "Nerve Strike",
    1028856: "Talon Strike",
    1028857: "Feint",
    1028860: "Armor Pierce",
    1028861: "Bladeweave",
    1028864: "Psychic Attack",
    1028866: "Force of Nature",
    1075829: "Bleed",
    1155771: "Magery Mastery",
    1155784: "Wrestling Mastery",
    1157559: "Piercing",
    1157560: "Bashing",
    1157561: "Slashing",
    1157562: "Battle Defense",
    1157459: "Aura of Energy",
    1157461: "Firestorm",
    1157463: "Explosive Goo",
    1157465: "Essence of Earth",
    1157467: "Aura of Nausea",
    1157469: "Essence of Disease",
    1157473: "Necromage",
    1157475: "Poison Breath",
    1157393: "Arcane Pyromancy",
    1157398: "Rune Corruption",
    1157400: "Grasping Claw",
    1157402: "Cold Wind",
    1157404: "Raging Breath",
    1157406: "Conductive Blast",
    1157408: "Lightning Force",
    1157410: "Steal Life",
    1157412: "Angry Fire",
    1157414: "Dragon Breath",
    1157416: "Inferno",
    1157418: "Flurry Force",
    1157420: "Vicious Bite",
    1157422: "Searing Wounds",
    1157424: "Life Leech",
    1157426: "Sticky Skin",
    1157428: "Tail Swipe",
    1157430: "Venomous Bite",
    1157432: "Mana Drain",
    1157434: "Repel",
    1044075: "Discordance",
    1002106: "Magery",
    1002122: "Poisoning",
    1044109: "Necromancy",
    1044111: "Chivalry",
    1044112: "Bushido",
    1044113: "Ninjitsu",
    1044114: "Spellweaving",
    1044115: "Mysticism",
    1151296: "Psychic Attack",
    1002082: "Healing",
    1151310: "Talon Strike",
    3002048: "Paralyze",
    1150005: "Rage",
}

# Magic skills that can be trained
skill_names = [
    "healing", "poisoning", "magery", "necromancy", "mysticism", "spellweaving",
    "discordance", "bushido", "ninjitsu", "chivalry"
]

abilities_dict = {
    "Angry Fire": 100,
    "Armor Ignore": 100,
    "Armor Pierce": 100,
    "Aura of Energy": 100,
    "Aura of Nausea": 100,
    "Bashing": 1,
    "Battle Defense": 1,
    "Bladeweave": 100,
    "Bleed": 100,
    "Block": 1100,
    "Bushido": 500,
    "Chivalry": 500,
    "Conductive Blast": 100,
    "Cold Wind": 100,
    "Concussion Blow": 100,
    "Crushing Blow": 100,
    "Discordance": 500,
    "Disarm": 100,
    "Dismount": 100,
    "Dragon Breath": 100,
    "Essence of Disease": 100,
    "Essence of Earth": 100,
    "Explosive Goo": 100,
    "Feint": 600,
    "Force of Nature": 100,
    "Frenzied Whirlwind": 600,
    "Grasping Claw": 100,
    "Healing": 100,
    "Inferno": 100,
    "Life Leech": 100,
    "Lightning Force": 100,
    "Magery": 1500,
    "Magery Mastery": 1501,
    "Mana Drain": 100,
    "Mysticism": 500,
    "Mortal Strike": 100,
    "Nerve Strike": 600,
    "Necromage": 1501,
    "Necromancy": 1501,
    "Ninjitsu": 500,
    "Paralyze": 100,
    "Piercing": 1,
    "Poison Breath": 100,
    "Poisoning": 100,
    "Poison Spit": 0,
    "Psychic Attack": 100,
    "Rage": 100,
    "Raging Breath": 100,
    "Repel": 100,
    "Rune Corruption": 100,
    "Searing Wounds": 100,
    "Slashing": 1,
    "Spellweaving": 500,
    "Steal Life": 100,
    "Sticky Skin": 100,
    "Talon Strike": 600,
    "Tail Swipe": 100,
    "Venomous Bite": 100,
    "Vicious Bite": 100,
    "Wrestling Mastery": 1,
}

# Base data for pets
BASE_DATA = {
#Bake Kitsune
    "0x00F6": { 
        "spawn_intensity_range": {"min": 4226, "max": 4885},
        "half_on_tame": False,
        "abilities": ["Magery", "Rage"],
        "slot_count": {"min" : 3, "max" : 5},
        },
#Bane Dragon
    "0x031A": { 
        "spawn_intensity_range": {"min": 5583, "max": 6338},
        "half_on_tame": False,
        "abilities": ["Magery", "Poisoning"],
        "slot_count": {"min" : 3, "max" : 5},
        },   
#Blood Fox
    "Blood Fox": { 
        "spawn_intensity_range": {"min": 2576, "max": 2899},
        "half_on_tame": False,
        "abilities": ["Grasping Claw", "Bleed"],
        "slot_count": {"min" : 2, "max" : 3},
        },    
#Bull - Smooth
    "0x00E8": { 
        "spawn_intensity_range": {"min": 572, "max": 771},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 4}
        },      
#Bull - Pattern
    "0x00E9": { 
        "spawn_intensity_range": {"min": 572, "max": 771},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 4}
        },          
#Coconut Crab
    "Coconut Crab": { 
        "spawn_intensity_range": {"min": 2486, "max": 2636},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 3},
        },
#Cold Drake Rough
    "0x003C": { 
        "spawn_intensity_range": {"min": 4480, "max": 5390},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "slot_count": {"min" : 3, "max" : 5},
        },        
#Cold Drake Smooth
    "0x003D": { 
        "spawn_intensity_range": {"min": 4480, "max": 5390},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "slot_count": {"min" : 3, "max" : 5},
        },

#Crimson Drake
    "0x058C": { 
        "spawn_intensity_range": {"min": 2711, "max": 3204},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "slot_count": {"min" : 2, "max" : 5},
        },        
#Cu Sidhe
    "0x0115": { 
        "spawn_intensity_range": {"min": 4624, "max": 5285},
        "half_on_tame": ["hits","stamina","strength","dexterity"],
        "abilities": ["Healing", "Bleed"],
        "slot_count": {"min" : 3, "max" : 5},
        },               
#Deathwatch Beetle
    "0x00F2": { 
        "spawn_intensity_range": {"min": 1354, "max": 1712},
        "half_on_tame": False,
        "abilities": ["Crushing Blow", "Poison Spit"],
        "slot_count": {"min" : 1, "max" : 4},
        }, 
#Dimetrosaur
    "0x0505": { 
        "spawn_intensity_range": {"min": 1354, "max": 1712},
        "half_on_tame": ["hits", "hits", "hits", "stamina", "strength", "dexterity"], #Hits 1/8 on tame
        "abilities": ["Poisoning", "Dismount", "Mortal Strike", "Poison Breath"],
        "wild_ability_caps": {"Wrestling": 130, "Tactics": 120, "Resisting Spells": 140},
        "tamed_ability_caps": {"Wrestling": 117, "Tactics": 108, "Resisting Spells": 126},
        "slot_count": {"min" : 3, "max" : 5},
        },      
#Dire Wolf
    "0x0017": { 
        "spawn_intensity_range": {"min": 2220, "max": 2498},
        "half_on_tame": False,
        "abilities": ["Necromancy"],
        "slot_count": {"min" : 1, "max" : 4},
        },        
#Dragon - Brown
    "0x000C2": { 
        "spawn_intensity_range": {"min": 6599, "max": 6936},
        "half_on_tame": False,
        "abilities": ["Magery", "Dragon Breath"],
        "slot_count": {"min" : 4, "max" : 5},
        },            
#Dragon - Red
    "0x003B2": { 
        "spawn_intensity_range": {"min": 6599, "max": 6936},
        "half_on_tame": False,
        "abilities": ["Magery", "Dragon Breath"],
        "slot_count": {"min" : 4, "max" : 5},
        },          
#Dragon Wolf
    "0x02CF": { 
        "spawn_intensity_range": {"min": 5517, "max": 5760},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "wild_ability_caps": {"Resisting Spells": 140},
        "tamed_ability_caps": {"Resisting Spells": 126},
        "slot_count": {"min" : 3, "max" : 5},
        },   
#Drake - Brown
    "Drake": { 
        "spawn_intensity_range": {"min": 2820, "max": 3144},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "slot_count": {"min" : 2, "max" : 5},
        },   
#Drake - Red
    "Drake": { 
        "spawn_intensity_range": {"min": 2820, "max": 3144},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "slot_count": {"min" : 2, "max" : 5},
        },           
#Dread Spider     
    "0x000B": { 
        "spawn_intensity_range": {"min": 5295, "max": 5721},
        "half_on_tame": False,
        "abilities": ["Magery", "Necromancy", "Poisoning"],
        "slot_count": {"min" : 3, "max" : 5},
        },          
#Eowmu
    "Eowmu": { 
        "spawn_intensity_range": {"min": 2514, "max": 2666},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 3},
        },      
#Fire Beetle
    "0x00A9": { 
        "spawn_intensity_range": {"min": 1890, "max": 1905},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 5},
        },    
#Fire Steed
    "0x00BE": { 
        "spawn_intensity_range": {"min": 2870, "max": 3170},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "wild_ability_caps": {"Resisting Spells": 120},
        "tamed_ability_caps": {"Resisting Spells": 108},
        "slot_count": {"min" : 2, "max" : 5},
        },        
#Frost Dragon 
    "Frost Dragon": { 
        "spawn_intensity_range": {"min": 7128, "max": 9337},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Dragon Breath", "Magery", "Bleed"],
        "wild_ability_caps": {"Wrestling": 145, "Tactics": 140, "Resisting Spells": 140, "Magery": 140},
        "tamed_ability_caps": {"Wrestling": 130, "Tactics": 126, "Resisting Spells": 126, "Magery": 126},
        "slot_count": {"min" : 5, "max" : 5},
        },      
#Frost Drake
    "Frost Drake": { 
        "spawn_intensity_range": {"min": 3051, "max": 3398},
        "half_on_tame": False,
        "abilities": ["Cold Wind"],
        "slot_count": {"min" : 2, "max" : 5},
        },      
#Frost Mite
    "0x0590": { 
        "spawn_intensity_range": {"min": 3909, "max": 4254},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Cold Wind"],
        "wild_ability_caps": {"Wrestling": 120},
        "tamed_ability_caps": {"Wrestling": 108},
        "slot_count": {"min" : 2, "max" : 5},
        },    
#Frost Spider
    "Frost Spider": { 
        "spawn_intensity_range": {"min": 814, "max": 1071},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 4},
        },       
#Gallusaurus
    "0x0506": { 
        "spawn_intensity_range": {"min": 5676, "max": 6212},
        "half_on_tame": False,
        "abilities": ["Bushido", "Ninjitsu", "Grasping Claw", "Block"],
        "wild_ability_caps": {"Bushido": 125},
        "tamed_ability_caps": {"Bushido": 112.5},
        "slot_count": {"min" : 4, "max" : 5},        
        },          
#Gaman
    "0x00F8": { 
        "spawn_intensity_range": {"min": 1495, "max": 2001},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 4},
        },               
#Giant Beetle
    "0x0317": { 
        "spawn_intensity_range": {"min": 1680, "max": 1830},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 5},
        },   
#Greater Dragon - Brown
    "0x000C": { 
        "spawn_intensity_range": {"min": 6139, "max": 7149},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Magery", "Dragon Breath", "Bleed"],
        "wild_ability_caps": {"Wrestling": 145, "Tactics": 140, "Resisting Spells": 140, "Magery": 140},
        "tamed_ability_caps": {"Wrestling": 130, "Tactics": 126, "Resisting Spells": 126, "Magery": 126},
        "slot_count": {"min" : 4, "max" : 5}
        },      
#Greater Dragon - Red
    "0x003B": { 
        "spawn_intensity_range": {"min": 6139, "max": 7149},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Magery", "Dragon Breath", "Bleed"],
        "wild_ability_caps": {"Wrestling": 145, "Tactics": 140, "Resisting Spells": 140, "Magery": 140},
        "tamed_ability_caps": {"Wrestling": 130, "Tactics": 126, "Resisting Spells": 126, "Magery": 126},
        "slot_count": {"min" : 4, "max" : 5},
        },       
#Grizzled Mare
    "Grizzled Mare": { 
        "spawn_intensity_range": {"min": 2718, "max": 2853},
        "half_on_tame": False,
        "abilities": ["Necromancy"],
        "slot_count": {"min" : 1, "max" : 3},
        },      
#Hell Hound
    "Hell Hound": { 
        "spawn_intensity_range": {"min": 2581, "max": 3207},
        "half_on_tame": False,
        "abilities": ["Necromancy", "Dragon Breath"],
        "slot_count": {"min" : 1, "max" : 4},
        },       
#Hellcat
    "Hellcat": { 
        "spawn_intensity_range": {"min": 2340, "max": 2750},
        "half_on_tame": False,
        "abilities": ["Necromancy", "Dragon Breath"],
        "slot_count": {"min" : 1, "max" : 3},
        },           
#High Plains Boura
    "High Plains Boura": { 
        "spawn_intensity_range": {"min": 3701, "max": 4255},
        "half_on_tame": False,
        "abilities": ["Tail Swipe"],
        "slot_count": {"min" : 2, "max" : 5},
        },           
#Hiryu
    "0x00F3": { 
        "spawn_intensity_range": {"min": 4340, "max": 5272},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Grasping Claw", "Dismount"],
        "wild_ability_caps": {"Wrestling": 120},
        "tamed_ability_caps": {"Wrestling": 108},
        "slot_count": {"min" : 3, "max" : 5},
        },     
#Hungry Coconut Crab
    "Hungry Coconut Crab": { 
        "spawn_intensity_range": {"min": 133, "max": 163},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 2},
        },           
#Iron Beetle
    "0x02CA": { 
        "spawn_intensity_range": {"min": 2929, "max": 3458},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": None,
        "wild_ability_caps": {"Resisting Spells": 130},
        "tamed_ability_caps": {"Resisting Spells": 117},
        "slot_count": {"min" : 2, "max" : 5},
        },      
#Kirin
    "Kirin": { 
        "spawn_intensity_range": {"min": 3774, "max": 4117},
        "half_on_tame": False,
        "abilities": ["Magery"],
        "slot_count": {"min" : 2, "max" : 5},
        },           
#Lasher
    "Lasher": { 
        "spawn_intensity_range": {"min": 2514, "max": 2666},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 1, "max" : 3},
        },              
#Lava Lizard
    "0x00CE": { 
        "spawn_intensity_range": {"min": 1169, "max": 1434},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "slot_count": {"min" : 1, "max" : 4},
        },   
#Lesser Hiryu
    "0x00F32": { 
        "spawn_intensity_range": {"min": 2070, "max": 2705},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Grasping Claw", "Dismount"],
        "wild_ability_caps": {"Wrestling": 120},
        "tamed_ability_caps": {"Wrestling": 108},
        "slot_count": {"min" : 1, "max" : 5},
        },
#Lion
    "0x0592": { 
        "spawn_intensity_range": {"min": 2706, "max": 2974},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Piercing", "Armor Ignore", "Bleed", "Paralyze"],
        "slot_count": {"min" : 2, "max" : 5},
        },             
#Najasaurus
    "0x0509": { 
        "spawn_intensity_range": {"min": 3847, "max": 4300},
        "half_on_tame": False,
        "abilities": ["Poisoning"],
        "wild_ability_caps": {"Resisting Spells": 190},
        "tamed_ability_caps": {"Resisting Spells": 171},
        "slot_count": {"min" : 2, "max" : 5},
        },    
#Nightmare Shiny Short Mane
    "0x0074": { 
        "spawn_intensity_range": {"min": 3951, "max": 4254},
        "half_on_tame": False,
        "abilities": ["Magery", "Dragon Breath"],
        "slot_count": {"min" : 2, "max" : 5},
        },
#Nightmare Light Short Mane
    "0x00B2": { 
        "spawn_intensity_range": {"min": 3951, "max": 4254},
        "half_on_tame": False,
        "abilities": ["Magery", "Dragon Breath"],
        "slot_count": {"min" : 2, "max" : 5},
        },        
#Nightmare Dark (Also uses Dread Warhorse Model)
    "0x00B3": { 
        "spawn_intensity_range": {"min": 3951, "max": 4254},
        "half_on_tame": False,
        "abilities": ["Magery", "Dragon Breath"],
        "slot_count": {"min" : 2, "max" : 5},
        },        
#Ossein Ram
    "Ossein Ram": { 
        "spawn_intensity_range": {"min": 53607, "max": 4272},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Necromancy", "Battle Defense", "Life Leech", "Disarm", "Paralyze"],
        "slot_count": {"min" : 2, "max" : 5},
        },        
#Phoenix
    "0x0340": { 
        "spawn_intensity_range": {"min": 5397, "max": 5760},
        "half_on_tame": False,
        "abilities": ["Magery"],
        "wild_ability_caps": {"Resisting Spells": 134},
        "tamed_ability_caps": {"Resisting Spells": 120},
        "slot_count": {"min" : 3, "max" : 5},
        }, 
#Platinum Drake
    "0x058A": { 
        "spawn_intensity_range": {"min": 2711, "max": 3204},
        "half_on_tame": False,
        "abilities": ["Dragon Breath"],
        "slot_count": {"min" : 2, "max" : 5},
        },      
#Raptor
    "Raptor": { 
        "spawn_intensity_range": {"min": 3013, "max": 3615},
        "half_on_tame": False,
        "abilities": None,
        "slot_count": {"min" : 2, "max" : 5},
        },      
#Reptalon
    "Reptalon": { 
        "spawn_intensity_range": {"min": 4027, "max": 4254},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Dragon Breath", "Paralyze"],
        "wild_ability_caps": {"Wrestling": 119},
        "tamed_ability_caps": {"Wrestling": 107.1},
        "slot_count": {"min" : 2, "max" : 5},
        },            
#Rune Beetle
    "0x00F4": { 
        "spawn_intensity_range": {"min": 5111, "max": 5760},
        "half_on_tame": False,
        "abilities": ["Magery", "Poisoning", "Rune Corruption", "Bleed"],
        "wild_ability_caps": {"Evaluating Intelligence": 125, "Poisoning": 140},
        "tamed_ability_caps": {"Evaluating Intelligence": 112, "Poisoning": 126},
        "slot_count": {"min" : 3, "max" : 5}
        },
#Sabre-Toothed Tiger
    "0x0588": { 
        "spawn_intensity_range": {"min": 3370, "max": 3726},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Slashing", "Armor Ignore", "Disarm", "Nerve Strike", "Healing"],
        "slot_count": {"min" : 2, "max" : 5},
        },            
#Saurosaurus
    "0x050B": { 
        "spawn_intensity_range": {"min": 4905, "max": 5599},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Life Leech", "Tail Swipe", "Concussion Blow"],
        "wild_ability_caps": {"Wrestling": 130, "Tactics": 120},
        "tamed_ability_caps": {"Wrestling": 117, "Tactics": 108},
        "slot_count": {"min" : 3, "max" : 5},
        },    
#Serpentine Dragon
    "Serpentine Dragon": { 
        "spawn_intensity_range": {"min": 4027, "max": 4254},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Dragon Breath", "Paralyze"],
        "wild_ability_caps": {"Wrestling": 119},
        "tamed_ability_caps": {"Wrestling": 107.1},
        "slot_count": {"min" : 2, "max" : 5},
        },     
#Shadow Wyrm
    "0x006A": { 
        "spawn_intensity_range": {"min": 8806, "max": 9652},
        "half_on_tame": False,
        "abilities": ["Magery", "Necromancy", "Dragon Breath"],
        "wild_ability_caps": {"Resisting Spells": 130},
        "tamed_ability_caps": {"Resisting Spells": 117},
        "slot_count": {"min" : 5, "max" : 5},
        },     
#Skeletal Cat
    "Skeletal Cat": { 
        "spawn_intensity_range": {"min": 4014, "max": 4166},
        "half_on_tame": False,
        "abilities": ["Necromancy"],
        "slot_count": {"min" : 2, "max" : 4},
        },                    
#Skree
    "0x02DD": {
        "spawn_intensity_range": {"min": 5298, "max": 5760},
        "half_on_tame": False,
        "abilities": ["Magery", "Mysticism"],
        "wild_ability_caps": {"Wrestling": 120, "Magery": 114},
        "tamed_ability_caps": {"Wrestling": 108, "Magery": 102},
        "slot_count": {"min" : 3, "max" : 5},
        },    
#Stone Slith
    "Stone Slith": { 
        "spawn_intensity_range": {"min": 2053, "max": 2511},
        "half_on_tame": False,
        "abilities": ["Grasping Claw", "Tail Swipe", "Bleed"],
        "slot_count": {"min" : 1, "max" : 5},
        },   
#Stygian Drake
    "Stygian Drake": { 
        "spawn_intensity_range": {"min": 6576, "max": 6914},
        "half_on_tame": False,
        "abilities": ["Magery", "Magery Mastery"],
        "slot_count": {"min" : 4, "max" : 5},
        },     
#Triceratops
    "0x0587": { 
        "spawn_intensity_range": {"min": 4548, "max": 5508},
        "half_on_tame": ["hits", "stamina", "strength", "dexterity"],
        "abilities": ["Piercing", "Armor Ignore", "Bleed", "Paralyze", "Healing"],
        "slot_count": {"min" : 3, "max" : 5},
        },            
#Triton
    "0x02D0": { 
        "spawn_intensity_range": {"min": 3556, "max": 4552},
        "half_on_tame": False,
        "abilities": ["Healing"],
        "wild_ability_caps": {"Wrestling": 130, "Resisting Spells": 190},
        "tamed_ability_caps": {"Wrestling": 130, "Resisting Spells": 190},
        "slot_count": {"min" : 2, "max" : 5}
        },        
#Tsuki Wolf
    "0x00FA": { 
        "spawn_intensity_range": {"min": 4850, "max": 5532},
        "half_on_tame": False,
        "abilities": ["Necromancy", "Rage"],
        "slot_count": {"min" : 3, "max" : 5},
        },
#Unicorn
    "Unicorn": { 
        "spawn_intensity_range": {"min": 3834, "max": 4222},
        "half_on_tame": False,
        "abilities": ["Magery"],
        "slot_count": {"min" : 2, "max" : 5},
        },            
#Vollem
    "Vollem": { 
        "spawn_intensity_range": {"min": 4768, "max": 5040},
        "half_on_tame": False,
        "abilities": ["Magery", "Dragon Breath"],
        "slot_count": {"min" : 3, "max" : 5},
        },            
#White Wyrm
    "0x00B4": { 
        "spawn_intensity_range": {"min": 5097, "max": 5760},
        "half_on_tame": False,
        "abilities": ["Magery"],
        "slot_count": {"min" : 3, "max" : 5}
        },      
#Wild Tiger
    "Wild Tiger": { 
        "spawn_intensity_range": {"min": 3511, "max": 4295},
        "half_on_tame": False,
        "abilities": ["Grasping Claw", "Bleed"],
        "slot_count": {"min" : 2, "max" : 5},
        },  
#Wildfire Ostard
    "Wildfire Ostard": { 
        "spawn_intensity_range": {"min": 5425, "max": 5425},
        "half_on_tame": False,
        "abilities": ["Magery", "Poisoning"],
        "slot_count": {"min" : 3, "max" : 5},
        },            
#Windrunner
    "Windrunner": { 
        "spawn_intensity_range": {"min": 4014, "max": 4166},
        "half_on_tame": False,
        "abilities": ["Necromancy"],
        "slot_count": {"min" : 2, "max" : 4},
        },    
#Wolf Spider
    "0x02E0": { 
        "spawn_intensity_range": {"min": 2225, "max": 2647}, # Estimated
        "half_on_tame": False,
        "abilities": ["Poisoning"],
        "slot_count": {"min" : 1, "max" : 3},
        },          
}

def convert_to_hex(n):
    return f"0x%0.4X" % n
    
def find_abilities(cliloc_abilities_dict):
    # Get the raw data from Gump
    raw_data = Gumps.LastGumpRawData()
    data = ""
    for item in raw_data:
        data.join(str(item))
  
    # Initialize abilities list
    abilities = []
    
    # Loop through the dictionary
    for key in cliloc_abilities_dict.keys():
        if str(key) in raw_data:
            abilities.append(cliloc_abilities_dict[key])  # Add the found ability to the list
            
    return abilities  # Return the list of found abilities   
    
    
def adjust_intensity_if_slots_greater(base_slot, max_slot, min_slot, min_value, max_value):
    
    if max_slot > base_slot or max_slot > min_slot:
        num = max_slot - min_slot

        while num > 0:
            min_value += 1501
            max_value += 1501  
            num -= 1
        return min_value, max_value
    
    
class Pet:
    def __init__(self, name, hits, stamina, mana, strength, dexterity, intelligence,
                 physical, fire, cold, poison, energy, pet_type, base_slot, max_slot, max_dmg, half_tame_stats,   
                 hp_regen, stam_regen, mana_regen, wrestling=0, tactics=0, spell_resist=0, 
                 anatomy=0, healing=0, poisoning=0, detect_hidden=0, hiding=0, 
                 parry=0, magery=0, eval_int=0, meditation=0, necromancy=0, spirit_speak=0, 
                 mysticism=0, focus=0, spellweaving=0, discordance=0, bushido=0, ninjitsu=0, chivalry=0, abilities=None):
        self.name = name
        self.hits = float(hits)# if float(hits) >= 125 else 125
        self.stamina = float(stamina)# if float(stamina) >= 125 else 125
        self.mana = float(mana)# if float(mana) >= 125 else 125
        self.strength = float(strength)# if float(strength) >= 125 else 125
        self.dexterity = float(dexterity)# if float(dexterity) >= 125 else 125
        self.intelligence = float(intelligence)# if float(intelligence) >= 125 else 125
        self.physical = float(physical)
        self.fire = float(fire)
        self.cold = float(cold)
        self.poison = float(poison)
        self.energy = float(energy)
        self.pet_type = pet_type
        self.base_slot = float(base_slot)
        self.max_slot = float(max_slot)
        self.max_dmg = float(max_dmg)
        self.half_tame_stats = half_tame_stats
        self.hp_regen = float(hp_regen)
        self.stam_regen = float(stam_regen)
        self.mana_regen = float(mana_regen)
        self.wrestling = float(wrestling)
        self.tactics = float(tactics)
        self.spell_resist = float(spell_resist)
        self.anatomy = float(anatomy)
        self.healing = float(healing)
        self.poisoning = float(poisoning)
        self.detect_hidden = float(detect_hidden)
        self.hiding = float(hiding)
        self.parry = float(parry)
        self.magery = float(magery)
        self.eval_int = float(eval_int)
        self.meditation = float(meditation)
        self.necromancy = float(necromancy)
        self.spirit_speak = float(spirit_speak)
        self.mysticism = float(mysticism)
        self.focus = float(focus)
        self.spellweaving = float(spellweaving)
        self.discordance = float(discordance)
        self.bushido = float(bushido)
        self.ninjitsu = float(ninjitsu)
        self.chivalry = float(chivalry)
        self.abilities = abilities if abilities is not None else ["None"]

    def print_stats(self):
        Misc.SendMessage(f"Pet Name: {self.name}", 5)
        Misc.SendMessage(f"Type: {self.pet_type}", 5)
        Misc.SendMessage(f"Hits: {self.hits}", 5)
        Misc.SendMessage(f"Stamina: {self.stamina}", 5)
        Misc.SendMessage(f"Mana: {self.mana}", 5)
        Misc.SendMessage(f"Strength: {self.strength}", 5)
        Misc.SendMessage(f"Dexterity: {self.dexterity}", 5)
        Misc.SendMessage(f"Intelligence: {self.intelligence}", 5)
        Misc.SendMessage(f"Physical Resistance: {self.physical}", 5)
        Misc.SendMessage(f"Fire Resistance: {self.fire}", 5)
        Misc.SendMessage(f"Cold Resistance: {self.cold}", 5)
        Misc.SendMessage(f"Poison Resistance: {self.poison}", 5)
        Misc.SendMessage(f"Energy Resistance: {self.energy}", 5)
        Misc.SendMessage(f"Base Slot: {self.base_slot}", 5)
        Misc.SendMessage(f"Max Slot: {self.max_slot}", 5)
        Misc.SendMessage(f"Max Damage: {self.max_dmg}", 5)
        Misc.SendMessage(f"Half Tame Stats: {self.half_tame_stats}", 5)
        Misc.SendMessage(f"HP Regeneration: {self.hp_regen}", 5)
        Misc.SendMessage(f"Stamina Regeneration: {self.stam_regen}", 5)
        Misc.SendMessage(f"Mana Regeneration: {self.mana_regen}", 5)
        Misc.SendMessage(f"Wrestling: {self.wrestling}", 5)
        Misc.SendMessage(f"Tactics: {self.tactics}", 5)
        Misc.SendMessage(f"Spell Resist: {self.spell_resist}", 5)
        Misc.SendMessage(f"Magery: {self.magery}", 5)
        Misc.SendMessage(f"Eval Int: {self.eval_int}", 5)
        Misc.SendMessage(f"Poisoning: {self.poisoning}", 5)
        Misc.SendMessage(f"Anatomy: {self.anatomy}", 5)
        Misc.SendMessage(f"Parry: {self.parry}", 5)
        Misc.SendMessage(f"Meditation: {self.meditation}", 5)
        Misc.SendMessage(f"Focus: {self.focus}", 5)
        Misc.SendMessage(f"Healing: {self.healing}", 5)
        Misc.SendMessage(f"Necromancy: {self.necromancy}", 5)
        Misc.SendMessage(f"Spirit Speak: {self.spirit_speak}", 5)
        Misc.SendMessage(f"Chivalry: {self.chivalry}", 5)
        Misc.SendMessage(f"Bushido: {self.bushido}", 5)
        Misc.SendMessage(f"Ninjitsu: {self.ninjitsu}", 5)
        Misc.SendMessage(f"Mysticism: {self.mysticism}", 5)
        Misc.SendMessage(f"Spellweaving: {self.spellweaving}", 5)
        Misc.SendMessage(f"Discordance: {self.discordance}", 5)
        if self.abilities is not None:
            Misc.SendMessage(f"Abilities: {', '.join(self.abilities)}", 5)
        else:
            Misc.SendMessage(f"Abilities: None", 5)

    def halve_tame_stats(self):
        if isinstance(self.half_tame_stats, list) and self.pet_type == 'wild':
            for stat in self.half_tame_stats:
                if hasattr(self, stat):
                    original_value = getattr(self, stat)
                    halved_value = original_value // 2
                    setattr(self, stat, halved_value)

    def calculate_intensity(self, id):
        self.hp_regen = self.hp_regen
        self.stam_regen = self.stam_regen
        self.mana_regen = self.mana_regen
        self.wrestling = self.wrestling
        self.tactics = self.tactics
        self.spell_resist = self.spell_resist
        self.magery = self.magery
        self.eval_int = self.eval_int
        self.poisoning = self.poisoning
        self.halve_tame_stats()
        
        base_intensity = 0
        
        hits_value = 3 * self.hits
        base_intensity += hits_value
        
        stamina_value = 0.5 * self.stamina
        base_intensity += stamina_value
        
        mana_value = 0.5 * self.mana
        base_intensity += mana_value
        
        strength_value = 3 * self.strength
        base_intensity += strength_value
        
        dexterity_value = 0.1 * self.dexterity
        base_intensity += dexterity_value
        
        intelligence_value = 0.5 * self.intelligence
        base_intensity += intelligence_value
        
        physical_value = 3 * self.physical
        base_intensity += physical_value
        
        fire_value = 3 * self.fire
        base_intensity += fire_value
        
        cold_value = 3 * self.cold
        base_intensity += cold_value
        
        poison_value = 3 * self.poison
        base_intensity += poison_value
        
        energy_value = 3 * self.energy
        base_intensity += energy_value
        
        hp_regen_value = 18 * self.hp_regen
        base_intensity += hp_regen_value
        
        stam_regen_value = 12 * self.stam_regen
        base_intensity += stam_regen_value
        
        mana_regen_value = 12 * self.mana_regen
        base_intensity += mana_regen_value
        
        max_dmg_value = 3.3333334 * self.max_dmg
        base_intensity += max_dmg_value
        
        if self.pet_type == 'wild' and "wild_ability_caps" in BASE_DATA[id]:
            for skill in BASE_DATA[id]["wild_ability_caps"]:
                wild_cap = BASE_DATA[id]["wild_ability_caps"][skill]
                tame_cap = BASE_DATA[id]["tamed_ability_caps"][skill]
                if skill == "Wrestling":
                    self.wrestling = max(100, 100 + (wild_cap - tame_cap))
                if skill == "Tactics":
                    self.tactics = max(100, 100 + (wild_cap - tame_cap))
                if skill == "Resisting Spells":
                    self.spell_resist = max(100, 100 + (wild_cap - tame_cap))
                if skill == "Magery":
                    self.magery = max(100, 100 + (wild_cap - tame_cap))
                if skill == "Evaluating Intelligence":
                    self.eval_int = max(100, 100 + (wild_cap - tame_cap))
                if skill == "Poisoning":
                    self.poisoning = max(100, 100 + (wild_cap - tame_cap))
                if skill == "Bushido":
                    self.bushido = max(100, 100 + (wild_cap - tame_cap))
        
        if self.wrestling is not None and self.wrestling > 100.0:
            wrestling_value = 10 * (self.wrestling - 100.0)
            base_intensity += wrestling_value
            
        if self.tactics is not None and self.tactics > 100.0:
            tactics_value = 10 * (self.tactics - 100.0)
            base_intensity += tactics_value
            
        if self.spell_resist is not None and self.spell_resist > 100.0:
            spell_resist_value = 1 * (self.spell_resist - 100.0)
            base_intensity += spell_resist_value
            
        if self.anatomy is not None and self.anatomy > 100.0:
            anatomy_value = 1 * (self.anatomy - 100.0)
            base_intensity += anatomy_value
            
        if self.parry is not None and self.parry > 100.0:
            parry_value = 1 * (self.parry - 100.0)
            base_intensity += parry_value
            
        if self.meditation is not None and self.meditation > 100.0:
            meditation_value = 1 * (self.meditation - 100.0)
            base_intensity += meditation_value
            
        if self.focus is not None and self.focus > 100.0:
            focus_value = 1 * (self.focus - 100.0)
            base_intensity += focus_value
            
        if self.healing is not None and self.healing > 100.0:
            healing_value = 1 * int(self.healing - 100.0)
            base_intensity += healing_value
            
        if self.magery is not None and self.magery > 100.0:
            magery_value = 5 * (self.magery - 100.0)
            base_intensity += magery_value
            
        if self.eval_int is not None and self.eval_int > 100.0:
            eval_int_value = 10 * (self.eval_int - 100.0)
            base_intensity += eval_int_value
            
        if self.necromancy is not None and self.necromancy > 100.0:
            necromancy_value = 5 * (self.necromancy - 100.0)
            base_intensity += necromancy_value
            
        if self.spirit_speak is not None and self.spirit_speak > 100.0:
            spirit_speak_value = 10 * (self.spirit_speak - 100.0)
            base_intensity += spirit_speak_value
            
        if self.chivalry is not None and self.chivalry > 100.0:
            chivalry_value = 5 * (self.chivalry - 100.0)
            base_intensity += chivalry_value
            
        if self.bushido is not None and self.bushido > 100.0:
            bushido_value = 5 * (self.bushido - 100.0)
            base_intensity += bushido_value
            
        if self.ninjitsu is not None and self.ninjitsu > 100.0:
            ninjitsu_value = 5 * (self.ninjitsu - 100.0)
            base_intensity += ninjitsu_value
            
        if self.mysticism is not None and self.mysticism > 100.0:
            mysticism_value = 5 * (self.mysticism - 100.0)
            base_intensity += mysticism_value
            
        if self.spellweaving is not None and self.spellweaving > 100.0:
            spellweaving_value = 5 * (self.spellweaving - 100.0)
            base_intensity += spellweaving_value
            
        if self.discordance is not None and self.discordance > 100.0:
            discordance_value = 5 * (self.discordance - 100.0)
            base_intensity += discordance_value
            
        if self.poisoning is not None and self.poisoning > 100.0:
            poisoning_value = 1 * (self.poisoning - 100.0)
            base_intensity += poisoning_value
        
        for ability in self.abilities:
            if ability in abilities_dict:
                ability_intensity = abilities_dict[ability]
                base_intensity += ability_intensity
                    
        return base_intensity


    def add_abilities(self, ability_list):
        for ability in ability_list:
            if ability in abilities_dict and ability not in self.abilities:
                self.abilities.append(ability)

def calculate_percentage(actual_value, min_value, max_value):
    if max_value == min_value:
        return 100.0 if actual_value == min_value else 0.0
    return 100.0 * (actual_value - min_value) / (max_value - min_value)

def Clean(s):
    return s.replace('<div align=right>','').replace('<BASEFONT COLOR=#FF0000>','').replace(
    '</div>','').replace('<BASEFONT COLOR=#000080>','').replace('<BASEFONT COLOR=#008000>','').replace(
    '<BASEFONT COLOR=#BF80FF>','').replace('<BASEFONT COLOR=#57412F>','').replace('<DIV ALIGN=CENTER>','').replace(
    '<DIV ALIGN=RIGHT>','').replace('%','').split('/')
    
def getNotoriety(mob):
    return mob.Notoriety

def GetPetInfo():
    Misc.SendMessage('Target the creature you wish to appraise', 90)
    targ = Target.PromptTarget()
    pet = Mobiles.FindBySerial(targ)
    id = convert_to_hex(pet.MobileID)
    color = convert_to_hex(pet.Color)
    print(color, "", convert_to_hex(color))
    Mobiles.WaitForProps(pet, 5000)
    Gumps.ResetGump()
    Player.UseSkill('Animal Lore')
    Target.WaitForTarget(4000)
    Target.TargetExecute(pet)
    Gumps.WaitForGump(0x1db, 10000)
    if Gumps.CurrentGump() != 0x1db: return
    Misc.Pause(300)
    unclean_list = Gumps.GetLineList(0x1db)
    n = 0
    if '%' in unclean_list[1]:
        del unclean_list[1]
    gumpList = list(unclean_list)
    clean_list = [Clean(i) for i in gumpList]
    n = 0

    #Name
    pet_name = clean_list[0][0]
    
    #Damage
    dmg_range = clean_list[21][0].split('-')
    pet_max_dmg = dmg_range[1]
    
    #Base Stats
    hits = clean_list[1][1] if clean_list[1][0] != '---' else 0
    stamina = clean_list[2][1] if clean_list[2][0] != '---' else 0
    mana = clean_list[3][1] if clean_list[3][0] != '---' else 0
    strength = clean_list[4][0] if clean_list[4][0] != '---' else 0
    dexterity = clean_list[5][0] if clean_list[5][0] != '---' else 0
    intelligence = clean_list[6][0] if clean_list[6][0] != '---' else 0
    
    #Regens
    hp_regen = clean_list[8][0] if clean_list[8][0] != '---' else 0
    stam_regen = clean_list[9][0] if clean_list[9][0] != '---' else 0
    mana_regen = clean_list[10][0] if clean_list[10][0] != '---' else 0
    
    #Resists
    physical = clean_list[11][0] if clean_list[11][0] != '---' else 0
    fire = clean_list[12][0] if clean_list[12][0] != '---' else 0
    cold = clean_list[13][0] if clean_list[13][0] != '---' else 0
    poison = clean_list[14][0] if clean_list[14][0] != '---' else 0
    energy = clean_list[15][0] if clean_list[15][0] != '---' else 0
    
    #Skills
    wrestling = clean_list[22][1] if clean_list[22][0] != '---' else 0
    tactics = clean_list[23][1] if clean_list[23][0] != '---' else 0
    spell_resist = clean_list[24][1] if clean_list[24][0] != '---' else 0
    anatomy = clean_list[25][1] if clean_list[25][0] != '---' else 0
    healing = clean_list[26][1] if clean_list[26][0] != '---' else 0
    poisoning = clean_list[27][1] if clean_list[27][0] != '---' else 0
    detect_hidden = clean_list[28][1] if clean_list[28][0] != '---' else 0
    hiding = clean_list[29][1] if clean_list[29][0] != '---' else 0
    parry = clean_list[30][1] if clean_list[30][0] != '---' else 0
    magery = clean_list[31][1] if clean_list[31][0] != '---' else 0
    eval_int = clean_list[32][1] if clean_list[32][0] != '---' else 0
    meditation = clean_list[33][1] if clean_list[33][0] != '---' else 0
    necromancy = clean_list[34][1] if clean_list[34][0] != '---' else 0
    spirit_speak = clean_list[35][1] if clean_list[35][0] != '---' else 0
    mysticism = clean_list[36][1] if clean_list[36][0] != '---' else 0
    focus = clean_list[37][1] if clean_list[37][0] != '---' else 0
    spellweaving = clean_list[38][1] if clean_list[38][0] != '---' else 0
    discordance = clean_list[39][1] if clean_list[39][0] != '---' else 0
    bushido = clean_list[40][1] if clean_list[40][0] != '---' else 0
    ninjitsu = clean_list[41][1] if clean_list[41][0] != '---' else 0
    chivalry = clean_list[42][1] if clean_list[42][0] != '---' else 0
    
    #Creatures that share a mobile ID, differentiate with stats #0x00F3
    pet_type = 'wild' if getNotoriety(pet) > 2 and getNotoriety(pet) < 6 else 'tame'
    if pet_type == 'wild':
        if id == '0x000C' and int(hits) < 500: #Brown Dragon
            id = '0x000C2'
        if id == '0x003B' and int(hits) < 500: #Red Dragon
            id = "0x003B2"
        if id == '0x00F3' and int(hits) < 900: #Lesser Hiryu
            id = "0x00F32"
    if pet_type == 'tame':
        if id == '0x000C' and int(hits) < 500: #Brown Dragon
            id = '0x000C2'
        if id == '0x003B' and int(hits) < 500: #Red Dragon
            id = "0x003B2"    
        if id == '0x00F3' and int(hits) < 450: #Lesser Hiryu
            id = "0x00F32"
    #Wild / Tame and stats that change on tame
    
    half_stats = BASE_DATA[id]["half_on_tame"]
    
    #Slot Counts
    slot_nums = clean_list[43][0].split(' => ')
    min_slot = BASE_DATA[id]["slot_count"]["min"]
    base_slot = int(slot_nums[0][0])
    max_slot = BASE_DATA[id]["slot_count"]["max"]
    
    skills_dict = {
        "wrestling": wrestling,
        "tactics": tactics,
        "spell_resist": spell_resist,
        "anatomy": anatomy,
        "healing": healing,
        "poisoning": poisoning,
        "detect_hidden": detect_hidden,
        "hiding": hiding,
        "parry": parry,
        "magery": magery,
        "eval_int": eval_int,
        "meditation": meditation,
        "necromancy": necromancy,
        "spirit_speak": spirit_speak,
        "mysticism": mysticism,
        "focus": focus,
        "spellweaving": spellweaving,
        "discordance": discordance,
        "bushido": bushido,
        "ninjitsu": ninjitsu,
        "chivalry": chivalry
    }
    
    #Intensity Info
    min_value = int(BASE_DATA[id]["spawn_intensity_range"]["min"])
    max_value = int(BASE_DATA[id]["spawn_intensity_range"]["max"])
    print(min_value, max_value, base_slot, max_slot)
    
    if min_slot < max_slot:
        min_value, max_value = adjust_intensity_if_slots_greater(base_slot, max_slot, min_slot, min_value, max_value)
    
    #Abilities
    abilities_list = find_abilities(cliloc_abilities_dict)
    
    
    for skill_name in skill_names:
        # Get the value of the corresponding skill
        skill_value = skills_dict[skill_name]
    
        # Check if the skill value is greater than 0
        if skill_value == 0:
            if skill_name.capitalize() in abilities_list:
                skill_to_pop = abilities_list.index(str(skill_name.capitalize()))
                abilities_list.pop(skill_to_pop)
                
    # Create Pet object
    my_pet = Pet(
        name=pet_name,
        hits=hits,
        stamina=stamina,
        mana=mana,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        physical=physical,
        fire=fire,
        cold=cold,
        poison=poison,
        energy=energy,
        pet_type=pet_type,
        base_slot=base_slot,
        max_slot=max_slot,
        max_dmg=pet_max_dmg,
        half_tame_stats=half_stats,
        hp_regen=hp_regen,
        stam_regen=stam_regen,
        mana_regen=mana_regen,
        wrestling=wrestling,
        tactics=tactics,
        spell_resist=spell_resist,
        anatomy=anatomy,
        healing=healing,
        poisoning=poisoning,
        detect_hidden=detect_hidden,
        hiding=hiding,
        parry=parry,
        magery=magery,
        eval_int=eval_int,
        meditation=meditation,
        necromancy=necromancy,
        spirit_speak=spirit_speak,
        mysticism=mysticism,
        focus=focus,
        spellweaving=spellweaving,
        discordance=discordance,
        bushido=bushido,
        ninjitsu=ninjitsu,
        chivalry=chivalry,
        abilities=abilities_list
    )
    my_pet.print_stats()
    pet_intensity = my_pet.calculate_intensity(id) + (1501 * (max_slot - base_slot))
    percentage = calculate_percentage(pet_intensity, min_value, max_value)
    Player.HeadMessage(5,("{} Pet Intensity: Min: {:.1f} / Actual: {:.1f} / Max: {:.1f}".format(my_pet.name, min_value, pet_intensity, max_value)))
    Player.HeadMessage(5,("Intensity Percent: {:.2f}%".format(percentage)))
    
    return my_pet

GetPetInfo()    