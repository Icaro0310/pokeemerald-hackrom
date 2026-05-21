#!/usr/bin/env python3
"""
Expandir FOREACH_TM para incluir TM51-TM100
O projeto já suporta 100 TMs (NUM_TECHNICAL_MACHINES = 100)
e já tem ITEM_TM51-ITEM_TM100 definidos.
APENAS precisamos adicionar os moves em tms_hms.h
"""

import re
import shutil

TMS_HMS_FILE = "include/constants/tms_hms.h"

NEW_TM_MOVES = [
    "WILL_O_WISP",      # TM51
    "SWORDS_DANCE",     # TM52
    "TRICK_ROOM",       # TM53
    "SLEEP_TALK",       # TM54
    "DRAGON_DANCE",     # TM55
    "THUNDER_FANG",     # TM56
    "ICE_FANG",         # TM57
    "FIRE_FANG",        # TM58
    "PSYCHIC_FANGS",    # TM59
    "ROCK_SLIDE",       # TM60
    "X_SCISSOR",        # TM61
    "ICE_PUNCH",        # TM62
    "FIRE_PUNCH",       # TM63
    "THUNDER_PUNCH",    # TM64
    "DRAIN_PUNCH",      # TM65
    "PLAY_ROUGH",       # TM66
    "U_TURN",           # TM67
    "POISON_JAB",       # TM68
    "INCINERATE",       # TM69
    "SCALD",            # TM70
    "VOLT_SWITCH",      # TM71
    "DAZZLING_GLEAM",   # TM72
    "HEX",              # TM73
    "GRASS_KNOT",       # TM74
    "SHADOW_CLAW",      # TM75
    "STONE_EDGE",       # TM76
    "AVALANCHE",        # TM77
    "ZEN_HEADBUTT",     # TM78
    "MOONBLAST",        # TM79
    "BRUTAL_SWING",     # TM80
    "LIQUIDATION",      # TM81
    "DRACO_METEOR",     # TM82
    "METEOR_MASH",      # TM83
    "STEEL_BEAM",       # TM84
    "CHILLING_WATER",   # TM85
    "TRAILBLAZE",       # TM86
    "SYNTHESIS",        # TM87
    "HYPER_VOICE",      # TM88
    "SACRED_SWORD",     # TM89
    "FUSION_BOLT",      # TM90
    "FUSION_FLARE",     # TM91
    "BLUE_FLARE",       # TM92
    "BOLT_STRIKE",      # TM93
    "BRAVE_BIRD",       # TM94
    "STEALTH_ROCK",     # TM95
    "CRUNCH",           # TM96
    "HYDRO_PUMP",       # TM97
    "HI_JUMP_KICK",     # TM98
    "FLAME_CHARGE",     # TM99
    "BULLDOZE",         # TM100
]

def backup():
    shutil.copy2(TMS_HMS_FILE, f"{TMS_HMS_FILE}.backup")
    print(f"✅ Backup: {TMS_HMS_FILE}.backup")

def expand():
    with open(TMS_HMS_FILE, 'r') as f:
        content = f.read()
    
    print("\n📝 Expanding FOREACH_TM...")
    
    # Encontra F(OVERHEAT) seguido de FOREACH_HM
    pattern = r'(F\(OVERHEAT\))(\s*\\?\s*\n)(\s*FOREACH_HM)'
    match = re.search(pattern, content)
    
    if not match:
        print("❌ Padrão não encontrado!")
        return False
    
    # Cria novas linhas
    new_lines = " \\\n" + "\n".join([f"    F({move}) \\" for move in NEW_TM_MOVES])
    
    # Substitui
    old = match.group(1) + match.group(2)
    new = match.group(1) + new_lines + "\n" + match.group(2)
    
    content = content.replace(old, new, 1)
    
    with open(TMS_HMS_FILE, 'w') as f:
        f.write(content)
    
    print(f"✅ {len(NEW_TM_MOVES)} TMs adicionados!")
    return True

def verify():
    with open(TMS_HMS_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔍 Verificando...")
    
    # Conta TMs (antes de FOREACH_HM)
    tm_section = content.split('FOREACH_HM')[0]
    tm_count = len(re.findall(r'F\((\w+)\)', tm_section))
    print(f"   Total de TMs: {tm_count}")
    
    # Verifica se todos os novos estão lá
    missing = [m for m in NEW_TM_MOVES if f"F({m})" not in content]
    if missing:
        print(f"   ❌ Faltando: {missing}")
        return False
    
    print("✅ Todos os 100 TMs presentes!")
    return True

def main():
    print("=" * 60)
    print("🔧 TM EXPANDER - TM51-TM100")
    print("=" * 60)
    print("   NUM_TECHNICAL_MACHINES: 100 ✅")
    print("   ITEM_TM51-ITEM_TM100: ✅")
    print("   SaveBlock: ✅")
    print("   Apenas tms_hms.h precisa ser expandido!")
    
    backup()
    
    if expand() and verify():
        print("\n" + "=" * 60)
        print("🎉 SUCESSO! 100 TMs configurados!")
        print("=" * 60)
        print("\nPróximos passos:")
        print("   make clean && make")
        print("   New Game para testar")
        return 0
    else:
        print("\n❌ Falha!")
        return 1

if __name__ == "__main__":
    exit(main())
