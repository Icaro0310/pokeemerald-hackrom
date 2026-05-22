#!/usr/bin/env python3
"""
Fix TM 51-100 strings with correct C multiline format
"""

import re

ITEMS = "src/data/items.h"

# Mapeamento TM51-100
MOVES = [
    "WILL_O_WISP","SWORDS_DANCE","TRICK_ROOM","SLEEP_TALK","DRAGON_DANCE",
    "THUNDER_FANG","ICE_FANG","FIRE_FANG","PSYCHIC_FANGS","ROCK_SLIDE",
    "X_SCISSOR","ICE_PUNCH","FIRE_PUNCH","THUNDER_PUNCH","DRAIN_PUNCH",
    "PLAY_ROUGH","U_TURN","POISON_JAB","INCINERATE","SCALD","VOLT_SWITCH",
    "DAZZLING_GLEAM","HEX","GRASS_KNOT","SHADOW_CLAW","STONE_EDGE",
    "AVALANCHE","ZEN_HEADBUTT","MOONBLAST","BRUTAL_SWING","LIQUIDATION",
    "DRACO_METEOR","METEOR_MASH","STEEL_BEAM","CHILLING_WATER","TRAILBLAZE",
    "SYNTHESIS","HYPER_VOICE","SACRED_SWORD","FUSION_BOLT","FUSION_FLARE",
    "BLUE_FLARE","BOLT_STRIKE","BRAVE_BIRD","STEALTH_ROCK","CRUNCH",
    "HYDRO_PUMP","HI_JUMP_KICK","FLAME_CHARGE","BULLDOZE"
]

# Descrições em formato C multiline correto
DESC = {
    "WILL_O_WISP": '''            "Inflicts a burn on\\n"
            "the foe with intense\\n"
            "mystical fire."''',
    "SWORDS_DANCE": '''            "A frenetic dance that\\n"
            "sharply raises the\\n"
            "users Attack stat."''',
    "TRICK_ROOM": '''            "Twists dimensions to\\n"
            "make slower Pokemon\\n"
            "move first."''',
    "SLEEP_TALK": '''            "Uses an available\\n"
            "move randomly while\\n"
            "the user sleeps."''',
    "DRAGON_DANCE": '''            "A mystic dance that\\n"
            "boosts Attack and\\n"
            "Speed stats."''',
    "THUNDER_FANG": '''            "Bites with electrified\\n"
            "fangs. May paralyze\\n"
            "or make foe flinch."''',
    "ICE_FANG": '''            "Bites with icy fangs.\\n"
            "May freeze or make\\n"
            "the foe flinch."''',
    "FIRE_FANG": '''            "Bites with flaming\\n"
            "fangs. May burn or\\n"
            "make foe flinch."''',
    "PSYCHIC_FANGS": '''            "Bites with psychic\\n"
            "fangs. Breaks the\\n"
            "foes barrier."''',
    "ROCK_SLIDE": '''            "Large boulders are\\n"
            "hurled at the foe.\\n"
            "May cause flinching."''',
    "X_SCISSOR": '''            "The user slashes at\\n"
            "the foe by crossing\\n"
            "its sharp claws."''',
    "ICE_PUNCH": '''            "A chilling punch that\\n"
            "may freeze the foe\\n"
            "solid on contact."''',
    "FIRE_PUNCH": '''            "A fiery punch that\\n"
            "may burn the foe on\\n"
            "contact."''',
    "THUNDER_PUNCH": '''            "An electrified punch\\n"
            "that may paralyze\\n"
            "the foe."''',
    "DRAIN_PUNCH": '''            "An energy-draining\\n"
            "punch that restores\\n"
            "HP by half damage."''',
    "PLAY_ROUGH": '''            "Plays rough with the\\n"
            "foe. May lower the\\n"
            "foes Attack stat."''',
    "U_TURN": '''            "After making its\\n"
            "attack, the user\\n"
            "rushes to switch out."''',
    "POISON_JAB": '''            "A stabbing attack\\n"
            "that may poison\\n"
            "the foe."''',
    "INCINERATE": '''            "Burns up the foes\\n"
            "held Berry, making\\n"
            "it unusable."''',
    "SCALD": '''            "A boiling water\\n"
            "attack that may\\n"
            "burn the foe."''',
    "VOLT_SWITCH": '''            "After attacking, the\\n"
            "user rushes back to\\n"
            "switch with a partner."''',
    "DAZZLING_GLEAM": '''            "Damages foes by\\n"
            "emitting a powerful\\n"
            "flash of light."''',
    "HEX": '''            "Does double damage\\n"
            "if the foe has a\\n"
            "status condition."''',
    "GRASS_KNOT": '''            "The heavier the foe,\\n"
            "the greater this\\n"
            "attacks power."''',
    "SHADOW_CLAW": '''            "Strikes with a shadowy\\n"
            "claw. High critical-\\n"
            "hit ratio."''',
    "STONE_EDGE": '''            "Stabs the foe with\\n"
            "jagged stones. High\\n"
            "critical-hit ratio."''',
    "AVALANCHE": '''            "An attack that does\\n"
            "double damage if the\\n"
            "user has been hurt."''',
    "ZEN_HEADBUTT": '''            "Hits with a strong\\n"
            "headbutt. May make\\n"
            "the foe flinch."''',
    "MOONBLAST": '''            "Attacks with moonlight\\n"
            "power. May lower the\\n"
            "foes Sp. Atk."''',
    "BRUTAL_SWING": '''            "Swings the body wildly\\n"
            "to strike everything\\n"
            "around the user."''',
    "LIQUIDATION": '''            "Slams the foe with\\n"
            "water. May lower the\\n"
            "foes Defense."''',
    "DRACO_METEOR": '''            "Unleashes a comet-like\\n"
            "blast, but harshly\\n"
            "lowers Sp. Atk."''',
    "METEOR_MASH": '''            "A hard punch like a\\n"
            "meteor. May raise the\\n"
            "users Attack."''',
    "STEEL_BEAM": '''            "Fires a beam of steel\\n"
            "energy. Damages the\\n"
            "user slightly too."''',
    "CHILLING_WATER": '''            "Sprays cold water on\\n"
            "the foe. May lower\\n"
            "the foes Attack."''',
    "TRAILBLAZE": '''            "Attacks while blazing\\n"
            "a trail. Raises the\\n"
            "users Speed stat."''',
    "SYNTHESIS": '''            "Restores HP. Amount\\n"
            "varies with the\\n"
            "weather."''',
    "HYPER_VOICE": '''            "Lets out a horribly\\n"
            "loud shout to damage\\n"
            "the foe."''',
    "SACRED_SWORD": '''            "Ignores the foes\\n"
            "stat changes and\\n"
            "slashes with a blade."''',
    "FUSION_BOLT": '''            "Blasts with a bolt\\n"
            "of electricity. Power\\n"
            "rises with Fusion Flare."''',
    "FUSION_FLARE": '''            "Blasts with a giant\\n"
            "fireball. Power rises\\n"
            "with Fusion Bolt."''',
    "BLUE_FLARE": '''            "Engulfs the foe in\\n"
            "blue flames. May burn\\n"
            "the target."''',
    "BOLT_STRIKE": '''            "Strikes with a great\\n"
            "thunderbolt. May\\n"
            "paralyze the foe."''',
    "BRAVE_BIRD": '''            "A reckless dive that\\n"
            "also hurts the user\\n"
            "quite a lot."''',
    "STEALTH_ROCK": '''            "Lays floating stones\\n"
            "that hurt foes when\\n"
            "they switch in."''',
    "CRUNCH": '''            "Crunches with sharp\\n"
            "fangs. May lower the\\n"
            "foes Defense."''',
    "HYDRO_PUMP": '''            "Blasts the foe with\\n"
            "a huge volume of\\n"
            "water under pressure."''',
    "HI_JUMP_KICK": '''            "A jumping knee kick.\\n"
            "If it misses, the\\n"
            "user is hurt instead."''',
    "FLAME_CHARGE": '''            "Attacks while cloaked\\n"
            "in flames. Raises\\n"
            "the users Speed."''',
    "BULLDOZE": '''            "Stomps the ground\\n"
            "and attacks. Lowers\\n"
            "the foes Speed."''',
}

with open(ITEMS, 'r') as f:
    content = f.read()

for i, move in enumerate(MOVES, start=51):
    item = f"ITEM_TM{i:02d}"
    desc = DESC.get(move, '''            "Teaches a move\\n"
            "to a compatible\\n"
            "Pokemon."''')
    
    # Bloco CORRETO com formato C multiline
    new_block = f'''    [{item}] =
    {{
        .name = _("TM{i:02d}"),
        .price = 3000,
        .description = COMPOUND_STRING(
{desc}
        ),
        .importance = I_REUSABLE_TMS,
        .pocket = POCKET_TM_HM,
        .type = ITEM_USE_PARTY_MENU,
        .fieldUseFunc = ItemUseOutOfBattle_TMHM,
        .secondaryId = MOVE_{move},
    }},
'''
    
    # Regex: substitui o bloco inteiro
    pattern = rf'\[{item}\] =\s*\{{.*?\}}\,'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_block.strip(), content, flags=re.DOTALL, count=1)
        print(f"  CORRECTED TM{i:02d} -> {move}")
    else:
        print(f"  SKIP TM{i:02d} -> block not found")

with open(ITEMS, 'w') as f:
    f.write(content)

print("\nCORRECTED! Now compile with: make clean && make")