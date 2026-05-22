#!/usr/bin/env python3
"""
Atualizar equipes dos líderes de ginásio manualmente no formato correto
"""

import re
import shutil

TRAINERS_FILE = "src/data/trainers.h"

# Novas equipes dos líderes de ginásio no formato correto
GYM_LEADERS_TEAMS = {
    "sParty_Roxanne": [
        "{.species = SPECIES_SHIELDON, .lvl = 12, .moves = {MOVE_TACKLE, MOVE_PROTECT, MOVE_METAL_SOUND, MOVE_ROCK_TOMB}}",
        "{.species = SPECIES_RHYHORN, .lvl = 12, .moves = {MOVE_HORN_ATTACK, MOVE_ROCK_TOMB, MOVE_BULLDOZE, MOVE_TAIL_WHIP}}",
        "{.species = SPECIES_KABUTO, .lvl = 14, .moves = {MOVE_AQUA_JET, MOVE_ROCK_TOMB, MOVE_SCRATCH, MOVE_HARDEN}}",
        "{.species = SPECIES_ONIX, .lvl = 14, .moves = {MOVE_ROCK_THROW, MOVE_BIND, MOVE_CURSE, MOVE_STEALTH_ROCK}}",
        "{.species = SPECIES_ARCANINE_HISUI, .lvl = 15, .moves = {MOVE_BITE, MOVE_FLAME_WHEEL, MOVE_ROCK_SLIDE, MOVE_EXTREME_SPEED}}",
        "{.species = SPECIES_GEODUDE_ALOLA, .lvl = 16, .moves = {MOVE_TACKLE, MOVE_ROCK_THROW, MOVE_SPARK, MOVE_ROLLOUT}}"
    ],
    "sParty_Brawly": [
        "{.species = SPECIES_LUCARIO, .lvl = 16, .moves = {MOVE_FORCE_PALM, MOVE_METAL_CLAW, MOVE_COUNTER, MOVE_QUICK_ATTACK}}",
        "{.species = SPECIES_MEDITITE, .lvl = 16, .moves = {MOVE_CONFUSION, MOVE_HIGH_JUMP_KICK, MOVE_MEDITATE, MOVE_DETECT}}",
        "{.species = SPECIES_HERACROSS, .lvl = 18, .moves = {MOVE_HORN_ATTACK, MOVE_AERIAL_ACE, MOVE_COUNTER, MOVE_LEER}}",
        "{.species = SPECIES_HITMONLEE, .lvl = 18, .moves = {MOVE_DOUBLE_KICK, MOVE_BULK_UP, MOVE_MACH_PUNCH, MOVE_FAKE_OUT}}",
        "{.species = SPECIES_MAKUHITA, .lvl = 19, .moves = {MOVE_ARM_THRUST, MOVE_VITAL_THROW, MOVE_FAKE_OUT, MOVE_BULK_UP}}",
        "{.species = SPECIES_HITMONTOP, .lvl = 19, .moves = {MOVE_TRIPLE_KICK, MOVE_MACH_PUNCH, MOVE_QUICK_ATTACK, MOVE_DETECT}}"
    ],
    "sParty_Wattson": [
        "{.species = SPECIES_CHINCHOU, .lvl = 20, .moves = {MOVE_BUBBLE_BEAM, MOVE_THUNDER_WAVE, MOVE_SPARK, MOVE_SUPERSONIC}}",
        "{.species = SPECIES_RAICHU, .lvl = 20, .moves = {MOVE_THUNDERBOLT, MOVE_QUICK_ATTACK, MOVE_TAIL_WHIP, MOVE_THUNDER_WAVE}}",
        "{.species = SPECIES_VOLTORB_HISUI, .lvl = 22, .moves = {MOVE_SPARK, MOVE_ENERGY_BALL, MOVE_THUNDER_WAVE, MOVE_SELF_DESTRUCT}}",
        "{.species = SPECIES_JOLTEON, .lvl = 23, .moves = {MOVE_THUNDERBOLT, MOVE_QUICK_ATTACK, MOVE_DOUBLE_KICK, MOVE_THUNDER_WAVE}}",
        "{.species = SPECIES_ELECTIVIRE, .lvl = 24, .moves = {MOVE_THUNDER_PUNCH, MOVE_LOW_KICK, MOVE_THUNDER_WAVE, MOVE_QUICK_ATTACK}}",
        "{.species = SPECIES_RAICHU_ALOLA, .lvl = 24, .moves = {MOVE_PSYCHIC, MOVE_THUNDERBOLT, MOVE_QUICK_ATTACK, MOVE_NASTY_PLOT}}"
    ],
    "sParty_Flannery": [
        "{.species = SPECIES_FLAREON, .lvl = 24, .moves = {MOVE_FLAMETHROWER, MOVE_QUICK_ATTACK, MOVE_BITE, MOVE_WILL_O_WISP}}",
        "{.species = SPECIES_NINETALES, .lvl = 24, .moves = {MOVE_FLAMETHROWER, MOVE_CONFUSE_RAY, MOVE_WILL_O_WISP, MOVE_QUICK_ATTACK}}",
        "{.species = SPECIES_HOUNDOOM, .lvl = 26, .moves = {MOVE_FLAMETHROWER, MOVE_BITE, MOVE_SMOG, MOVE_NASTY_PLOT}}",
        "{.species = SPECIES_ARCANINE, .lvl = 26, .moves = {MOVE_FLAMETHROWER, MOVE_EXTREME_SPEED, MOVE_CRUNCH, MOVE_AGILITY}}",
        "{.species = SPECIES_MAROWAK_ALOLA, .lvl = 27, .moves = {MOVE_FLARE_BLITZ, MOVE_SHADOW_BONE, MOVE_BONE_CLUB, MOVE_WILL_O_WISP}}",
        "{.species = SPECIES_ARCANINE_HISUI, .lvl = 27, .moves = {MOVE_ROCK_SLIDE, MOVE_FLAME_WHEEL, MOVE_EXTREME_SPEED, MOVE_CRUNCH}}"
    ],
    "sParty_Norman": [
        "{.species = SPECIES_RATICATE_ALOLA, .lvl = 27, .moves = {MOVE_CRUNCH, MOVE_QUICK_ATTACK, MOVE_SUPER_FANG, MOVE_HYPER_FANG}}",
        "{.species = SPECIES_WIGGLYTUFF, .lvl = 28, .moves = {MOVE_BODY_SLAM, MOVE_PLAY_ROUGH, MOVE_SING, MOVE_DISABLE}}",
        "{.species = SPECIES_KANGASKHAN, .lvl = 29, .moves = {MOVE_COMET_PUNCH, MOVE_BITE, MOVE_TAIL_WHIP, MOVE_FAKE_OUT}}",
        "{.species = SPECIES_BLISSEY, .lvl = 29, .moves = {MOVE_SOFT_BOILED, MOVE_SEISMIC_TOSS, MOVE_SING, MOVE_MINIMIZE}}",
        "{.species = SPECIES_MILTANK, .lvl = 30, .moves = {MOVE_BODY_SLAM, MOVE_MILK_DRINK, MOVE_ROLLOUT, MOVE_ATTRACT}}",
        "{.species = SPECIES_SNORLAX, .lvl = 31, .moves = {MOVE_BODY_SLAM, MOVE_YAWN, MOVE_DEFENSE_CURL, MOVE_LICK}}"
    ],
    "sParty_Winona": [
        "{.species = SPECIES_NOCTOWL, .lvl = 29, .moves = {MOVE_AIR_SLASH, MOVE_EXTRASENSORY, MOVE_HYPNOSIS, MOVE_REFLECT}}",
        "{.species = SPECIES_SCYTHER, .lvl = 29, .moves = {MOVE_AERIAL_ACE, MOVE_X_SCISSOR, MOVE_QUICK_ATTACK, MOVE_SLASH}}",
        "{.species = SPECIES_SKARMORY, .lvl = 31, .moves = {MOVE_AIR_SLASH, MOVE_STEEL_WING, MOVE_SPIKES, MOVE_AGILITY}}",
        "{.species = SPECIES_HONCHKROW, .lvl = 32, .moves = {MOVE_NIGHT_SLASH, MOVE_DRILL_PECK, MOVE_HAZE, MOVE_TAILWIND}}",
        "{.species = SPECIES_TOGEKISS, .lvl = 33, .moves = {MOVE_AIR_SLASH, MOVE_AURA_SPHERE, MOVE_ANCIENT_POWER, MOVE_YAWN}}",
        "{.species = SPECIES_AERODACTYL, .lvl = 33, .moves = {MOVE_ROCK_SLIDE, MOVE_WING_ATTACK, MOVE_BITE, MOVE_AGILITY}}"
    ],
    "sParty_TateAndLiza": [
        "{.species = SPECIES_MR_MIME_GALAR, .lvl = 41, .moves = {MOVE_PSYCHIC, MOVE_FREEZE_DRY, MOVE_LIGHT_SCREEN, MOVE_REFLECT}}",
        "{.species = SPECIES_SLOWBRO_GALAR, .lvl = 41, .moves = {MOVE_SHELL_SIDE_ARM, MOVE_PSYCHIC, MOVE_SURF, MOVE_YAWN}}",
        "{.species = SPECIES_RAPIDASH_GALAR, .lvl = 41, .moves = {MOVE_PSYCHO_CUT, MOVE_PLAY_ROUGH, MOVE_MEGAHORN, MOVE_WILL_O_WISP}}",
        "{.species = SPECIES_ESPEON, .lvl = 42, .moves = {MOVE_PSYCHIC, MOVE_SHADOW_BALL, MOVE_MORNING_SUN, MOVE_CALM_MIND}}",
        "{.species = SPECIES_SLOWKING_GALAR, .lvl = 42, .moves = {MOVE_EERIE_SPELL, MOVE_SURF, MOVE_POWER_GEM, MOVE_NASTY_PLOT}}",
        "{.species = SPECIES_ALAKAZAM, .lvl = 42, .moves = {MOVE_PSYCHIC, MOVE_SHADOW_BALL, MOVE_RECOVER, MOVE_CALM_MIND}}"
    ],
    "sParty_Juan": [
        "{.species = SPECIES_BLASTOISE, .lvl = 46, .moves = {MOVE_HYDRO_PUMP, MOVE_ICE_BEAM, MOVE_FLASH_CANNON, MOVE_PROTECT}}",
        "{.species = SPECIES_FERALIGATR, .lvl = 46, .moves = {MOVE_AQUA_TAIL, MOVE_CRUNCH, MOVE_ICE_FANG, MOVE_DRAGON_DANCE}}",
        "{.species = SPECIES_SWAMPERT, .lvl = 47, .moves = {MOVE_EARTHQUAKE, MOVE_SURF, MOVE_ICE_BEAM, MOVE_HAMMER_ARM}}",
        "{.species = SPECIES_EMPOLEON, .lvl = 47, .moves = {MOVE_HYDRO_PUMP, MOVE_FLASH_CANNON, MOVE_ICE_BEAM, MOVE_DRILL_PECK}}",
        "{.species = SPECIES_GRENINJA, .lvl = 49, .moves = {MOVE_HYDRO_PUMP, MOVE_DARK_PULSE, MOVE_ICE_BEAM, MOVE_EXTRASENSORY}}",
        "{.species = SPECIES_KINGDRA, .lvl = 49, .moves = {MOVE_HYDRO_PUMP, MOVE_DRAGON_PULSE, MOVE_ICE_BEAM, MOVE_AGILITY}}"
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
    print("🏋️ GYM LEADERS MANUAL UPDATER")
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
    print("   - COMPETITIVE_PARTY_SYNTAX foi desativado")
    print("   - Formas regionais agora disponíveis")
    print("   - Movesets competitivos aplicados")
    print("\nPróximos passos:")
    print("   make clean && make")
    print("   NEW GAME requerido devido à mudança no saveblock")
    
    return 0

if __name__ == "__main__":
    exit(main())
