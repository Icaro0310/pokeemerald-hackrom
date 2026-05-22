#!/usr/bin/env python3
"""
Atualizar equipes dos líderes de ginásio com movesets competitivos
"""

import re
import shutil

TRAINERS_FILE = "src/data/trainers.h"

# Novas equipes dos líderes de ginásio
GYM_LEADERS_TEAMS = {
    "sParty_Roxanne1": [
        "{.lvl = 12, .species = SPECIES_SHIELDON, .moves = {MOVE_TACKLE, MOVE_PROTECT, MOVE_METAL_SOUND, MOVE_ROCK_TOMB}}",
        "{.lvl = 12, .species = SPECIES_RHYHORN, .moves = {MOVE_HORN_ATTACK, MOVE_ROCK_TOMB, MOVE_BULLDOZE, MOVE_TAIL_WHIP}}",
        "{.lvl = 14, .species = SPECIES_KABUTO, .moves = {MOVE_AQUA_JET, MOVE_ROCK_TOMB, MOVE_SCRATCH, MOVE_HARDEN}}",
        "{.lvl = 14, .species = SPECIES_ONIX, .moves = {MOVE_ROCK_THROW, MOVE_BIND, MOVE_CURSE, MOVE_STEALTH_ROCK}}",
        "{.lvl = 15, .species = SPECIES_ARCANINE_HISUI, .moves = {MOVE_BITE, MOVE_FLAME_WHEEL, MOVE_ROCK_SLIDE, MOVE_EXTREME_SPEED}}",
        "{.lvl = 16, .species = SPECIES_GEODUDE_ALOLA, .moves = {MOVE_TACKLE, MOVE_ROCK_THROW, MOVE_SPARK, MOVE_ROLLOUT}}"
    ],
    "sParty_Brawly1": [
        "{.lvl = 16, .species = SPECIES_LUCARIO, .moves = {MOVE_FORCE_PALM, MOVE_METAL_CLAW, MOVE_COUNTER, MOVE_QUICK_ATTACK}}",
        "{.lvl = 16, .species = SPECIES_MEDITITE, .moves = {MOVE_CONFUSION, MOVE_HIGH_JUMP_KICK, MOVE_MEDITATE, MOVE_DETECT}}",
        "{.lvl = 18, .species = SPECIES_HERACROSS, .moves = {MOVE_HORN_ATTACK, MOVE_AERIAL_ACE, MOVE_COUNTER, MOVE_LEER}}",
        "{.lvl = 18, .species = SPECIES_HITMONLEE, .moves = {MOVE_DOUBLE_KICK, MOVE_BULK_UP, MOVE_MACH_PUNCH, MOVE_FAKE_OUT}}",
        "{.lvl = 19, .species = SPECIES_MAKUHITA, .moves = {MOVE_ARM_THRUST, MOVE_VITAL_THROW, MOVE_FAKE_OUT, MOVE_BULK_UP}}",
        "{.lvl = 19, .species = SPECIES_HITMONTOP, .moves = {MOVE_TRIPLE_KICK, MOVE_MACH_PUNCH, MOVE_QUICK_ATTACK, MOVE_DETECT}}"
    ],
    "sParty_Wattson1": [
        "{.lvl = 20, .species = SPECIES_CHINCHOU, .moves = {MOVE_BUBBLE_BEAM, MOVE_THUNDER_WAVE, MOVE_SPARK, MOVE_SUPERSONIC}}",
        "{.lvl = 20, .species = SPECIES_RAICHU, .moves = {MOVE_THUNDERBOLT, MOVE_QUICK_ATTACK, MOVE_TAIL_WHIP, MOVE_THUNDER_WAVE}}",
        "{.lvl = 22, .species = SPECIES_VOLTORB_HISUI, .moves = {MOVE_SPARK, MOVE_ENERGY_BALL, MOVE_THUNDER_WAVE, MOVE_SELF_DESTRUCT}}",
        "{.lvl = 23, .species = SPECIES_JOLTEON, .moves = {MOVE_THUNDERBOLT, MOVE_QUICK_ATTACK, MOVE_DOUBLE_KICK, MOVE_THUNDER_WAVE}}",
        "{.lvl = 24, .species = SPECIES_ELECTIVIRE, .moves = {MOVE_THUNDER_PUNCH, MOVE_LOW_KICK, MOVE_THUNDER_WAVE, MOVE_QUICK_ATTACK}}",
        "{.lvl = 24, .species = SPECIES_RAICHU_ALOLA, .moves = {MOVE_PSYCHIC, MOVE_THUNDERBOLT, MOVE_QUICK_ATTACK, MOVE_NASTY_PLOT}}"
    ],
    "sParty_Flannery1": [
        "{.lvl = 24, .species = SPECIES_FLAREON, .moves = {MOVE_FLAMETHROWER, MOVE_QUICK_ATTACK, MOVE_BITE, MOVE_WILL_O_WISP}}",
        "{.lvl = 24, .species = SPECIES_NINETALES, .moves = {MOVE_FLAMETHROWER, MOVE_CONFUSE_RAY, MOVE_WILL_O_WISP, MOVE_QUICK_ATTACK}}",
        "{.lvl = 26, .species = SPECIES_HOUNDOOM, .moves = {MOVE_FLAMETHROWER, MOVE_BITE, MOVE_SMOG, MOVE_NASTY_PLOT}}",
        "{.lvl = 26, .species = SPECIES_ARCANINE, .moves = {MOVE_FLAMETHROWER, MOVE_EXTREME_SPEED, MOVE_CRUNCH, MOVE_AGILITY}}",
        "{.lvl = 27, .species = SPECIES_MAROWAK_ALOLA, .moves = {MOVE_FLARE_BLITZ, MOVE_SHADOW_BONE, MOVE_BONE_CLUB, MOVE_WILL_O_WISP}}",
        "{.lvl = 27, .species = SPECIES_ARCANINE_HISUI, .moves = {MOVE_ROCK_SLIDE, MOVE_FLAME_WHEEL, MOVE_EXTREME_SPEED, MOVE_CRUNCH}}"
    ],
    "sParty_Norman1": [
        "{.lvl = 27, .species = SPECIES_RATICATE_ALOLA, .moves = {MOVE_CRUNCH, MOVE_QUICK_ATTACK, MOVE_SUPER_FANG, MOVE_HYPER_FANG}}",
        "{.lvl = 28, .species = SPECIES_WIGGLYTUFF, .moves = {MOVE_BODY_SLAM, MOVE_PLAY_ROUGH, MOVE_SING, MOVE_DISABLE}}",
        "{.lvl = 29, .species = SPECIES_KANGASKHAN, .moves = {MOVE_COMET_PUNCH, MOVE_BITE, MOVE_TAIL_WHIP, MOVE_FAKE_OUT}}",
        "{.lvl = 29, .species = SPECIES_BLISSEY, .moves = {MOVE_SOFT_BOILED, MOVE_SEISMIC_TOSS, MOVE_SING, MOVE_MINIMIZE}}",
        "{.lvl = 30, .species = SPECIES_MILTANK, .moves = {MOVE_BODY_SLAM, MOVE_MILK_DRINK, MOVE_ROLLOUT, MOVE_ATTRACT}}",
        "{.lvl = 31, .species = SPECIES_SNORLAX, .moves = {MOVE_BODY_SLAM, MOVE_YAWN, MOVE_DEFENSE_CURL, MOVE_LICK}}"
    ],
    "sParty_Winona1": [
        "{.lvl = 29, .species = SPECIES_NOCTOWL, .moves = {MOVE_AIR_SLASH, MOVE_EXTRASENSORY, MOVE_HYPNOSIS, MOVE_REFLECT}}",
        "{.lvl = 29, .species = SPECIES_SCYTHER, .moves = {MOVE_AERIAL_ACE, MOVE_X_SCISSOR, MOVE_QUICK_ATTACK, MOVE_SLASH}}",
        "{.lvl = 31, .species = SPECIES_SKARMORY, .moves = {MOVE_AIR_SLASH, MOVE_STEEL_WING, MOVE_SPIKES, MOVE_AGILITY}}",
        "{.lvl = 32, .species = SPECIES_HONCHKROW, .moves = {MOVE_NIGHT_SLASH, MOVE_DRILL_PECK, MOVE_HAZE, MOVE_TAILWIND}}",
        "{.lvl = 33, .species = SPECIES_TOGEKISS, .moves = {MOVE_AIR_SLASH, MOVE_AURA_SPHERE, MOVE_ANCIENT_POWER, MOVE_YAWN}}",
        "{.lvl = 33, .species = SPECIES_AERODACTYL, .moves = {MOVE_ROCK_SLIDE, MOVE_WING_ATTACK, MOVE_BITE, MOVE_AGILITY}}"
    ],
    "sParty_TateAndLiza1": [
        "{.lvl = 41, .species = SPECIES_MR_MIME_GALAR, .moves = {MOVE_PSYCHIC, MOVE_FREEZE_DRY, MOVE_LIGHT_SCREEN, MOVE_REFLECT}}",
        "{.lvl = 41, .species = SPECIES_SLOWBRO_GALAR, .moves = {MOVE_SHELL_SIDE_ARM, MOVE_PSYCHIC, MOVE_SURF, MOVE_YAWN}}",
        "{.lvl = 41, .species = SPECIES_RAPIDASH_GALAR, .moves = {MOVE_PSYCHO_CUT, MOVE_PLAY_ROUGH, MOVE_MEGAHORN, MOVE_WILL_O_WISP}}",
        "{.lvl = 42, .species = SPECIES_ESPEON, .moves = {MOVE_PSYCHIC, MOVE_SHADOW_BALL, MOVE_MORNING_SUN, MOVE_CALM_MIND}}",
        "{.lvl = 42, .species = SPECIES_SLOWKING_GALAR, .moves = {MOVE_EERIE_SPELL, MOVE_SURF, MOVE_POWER_GEM, MOVE_NASTY_PLOT}}",
        "{.lvl = 42, .species = SPECIES_ALAKAZAM, .moves = {MOVE_PSYCHIC, MOVE_SHADOW_BALL, MOVE_RECOVER, MOVE_CALM_MIND}}"
    ],
    "sParty_Juan1": [
        "{.lvl = 46, .species = SPECIES_BLASTOISE, .moves = {MOVE_HYDRO_PUMP, MOVE_ICE_BEAM, MOVE_FLASH_CANNON, MOVE_PROTECT}}",
        "{.lvl = 46, .species = SPECIES_FERALIGATR, .moves = {MOVE_AQUA_TAIL, MOVE_CRUNCH, MOVE_ICE_FANG, MOVE_DRAGON_DANCE}}",
        "{.lvl = 47, .species = SPECIES_SWAMPERT, .moves = {MOVE_EARTHQUAKE, MOVE_SURF, MOVE_ICE_BEAM, MOVE_HAMMER_ARM}}",
        "{.lvl = 47, .species = SPECIES_EMPOLEON, .moves = {MOVE_HYDRO_PUMP, MOVE_FLASH_CANNON, MOVE_ICE_BEAM, MOVE_DRILL_PECK}}",
        "{.lvl = 49, .species = SPECIES_GRENINJA, .moves = {MOVE_HYDRO_PUMP, MOVE_DARK_PULSE, MOVE_ICE_BEAM, MOVE_EXTRASENSORY}}",
        "{.lvl = 49, .species = SPECIES_KINGDRA, .moves = {MOVE_HYDRO_PUMP, MOVE_DRAGON_PULSE, MOVE_ICE_BEAM, MOVE_AGILITY}}"
    ]
}

def backup():
    print("✅ Backup já foi criado anteriormente")

def update_gym_leaders():
    with open(TRAINERS_FILE, 'r') as f:
        content = f.read()
    
    print("\n🏋️ Atualizando equipes dos líderes de ginásio...")
    
    changes = 0
    for leader, team in GYM_LEADERS_TEAMS.items():
        # Encontrar o array existente
        pattern = rf'static const struct TrainerMon {leader}\[\s*=\s*\{{[^}}]*\}}'
        
        # Criar novo array
        new_array = f"static const struct TrainerMon {leader}[] = {{\n"
        new_array += ",\n".join(f"    {pokemon}" for pokemon in team)
        new_array += "\n};"
        
        # Substituir
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_array, content, flags=re.DOTALL)
            changes += 1
            print(f"   ✅ {leader} atualizado")
        else:
            print(f"   ⚠️ {leader} não encontrado")
    
    with open(TRAINERS_FILE, 'w') as f:
        f.write(content)
    
    print(f"\n✅ {changes} líderes de ginásio atualizados!")
    return changes

def verify():
    print("\n🔍 Verificando...")
    
    with open(TRAINERS_FILE, 'r') as f:
        content = f.read()
    
    for leader in GYM_LEADERS_TEAMS.keys():
        if f"static const struct TrainerMon {leader}" in content:
            print(f"   ✅ {leader} encontrado")
        else:
            print(f"   ❌ {leader} não encontrado")

def main():
    print("=" * 60)
    print("🏋️ GYM LEADERS UPDATER")
    print("=" * 60)
    print("Atualizando equipes dos líderes de ginásio com movesets competitivos...")
    
    backup()
    changes = update_gym_leaders()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 Líderes de ginásio atualizados!")
    print("=" * 60)
    print("\n⚠️ AVISO IMPORTANTE:")
    print("   - P_GEN_4_POKEMON foi ativado (requer NEW GAME)")
    print("   - Formas regionais agora disponíveis")
    print("   - Movesets competitivos aplicados")
    print("\nPróximos passos:")
    print("   make clean && make")
    print("   NEW GAME requerido devido à mudança no saveblock")
    
    return 0

if __name__ == "__main__":
    exit(main())
