#!/usr/bin/env python3
"""
Atualizar todos os trainers para usar IA inteligente
AI_FLAG_SMART_TRAINER - IA inteligente completa
AI_FLAG_SMART_SWITCHING - Troca inteligente de Pokémon
AI_FLAG_SMART_MON_CHOICES - Escolha inteligente de Pokémon
"""

import re
import shutil

TRAINERS_FILE = "src/data/trainers.h"

# Flags de IA inteligente
SMART_AI_FLAGS = "AI_FLAG_SMART_TRAINER"  # Inclui todas as flags inteligentes

def backup():
    shutil.copy2(TRAINERS_FILE, f"{TRAINERS_FILE}.backup")
    print("✅ Backup criado")

def update_all_trainers():
    with open(TRAINERS_FILE, 'r') as f:
        content = f.read()
    
    print("\n🤖 Atualizando IA de todos os trainers...")
    
    # Substitui todas as flags de IA básicas por IA inteligente
    # Procura por .aiFlags = AI_FLAG_BASIC_TRAINER ou outras flags
    patterns = [
        (r'\.aiFlags\s*=\s*AI_FLAG_BASIC_TRAINER', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_CHECK_BAD_MOVE', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_TRY_TO_FAINT', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_CHECK_VIABILITY', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_OMNISCIENT', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_SMART_SWITCHING', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_SMART_MON_CHOICES', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PP_STALL_PREVENTION', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_RISKY', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_TRY_TO_2HKO', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PREFER_BATON_PASS', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_DOUBLE_BATTLE', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_HP_AWARE', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_POWERFUL_STATUS', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_NEGATE_UNAWARE', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_WILL_SUICIDE', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PREFER_STATUS_MOVES', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_STALL', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_ACE_POKEMON', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_CONSERVATIVE', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_SEQUENCE_SWITCHING', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_DOUBLE_ACE_POKEMON', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_WEIGH_ABILITY_PREDICTION', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PREFER_HIGHEST_DAMAGE_MOVE', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PREDICT_SWITCH', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PREDICT_INCOMING_MON', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PP_STALL_PREVENTION', SMART_AI_FLAGS),
        (r'\.aiFlags\s*=\s*AI_FLAG_PREDICT_MOVE', SMART_AI_FLAGS),
    ]
    
    changes = 0
    for pattern, replacement in patterns:
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, f'.aiFlags = {replacement}', content)
            changes += len(matches)
    
    # Também substitui combinações de flags (ex: AI_FLAG_BASIC_TRAINER | AI_FLAG_OMNISCIENT)
    combined_pattern = r'\.aiFlags\s*=\s*(AI_FLAG_[A-Z_]+\s*\|\s*AI_FLAG_[A-Z_]+(?:\s*\|\s*AI_FLAG_[A-Z_]+)*)'
    combined_matches = re.findall(combined_pattern, content)
    if combined_matches:
        content = re.sub(combined_pattern, f'.aiFlags = {SMART_AI_FLAGS}', content)
        changes += len(combined_matches)
    
    with open(TRAINERS_FILE, 'w') as f:
        f.write(content)
    
    print(f"✅ {changes} trainers atualizados para IA inteligente!")
    return changes

def verify():
    print("\n🔍 Verificando...")
    
    with open(TRAINERS_FILE, 'r') as f:
        content = f.read()
    
    # Conta trainers com IA inteligente
    smart_count = content.count('AI_FLAG_SMART_TRAINER')
    basic_count = content.count('AI_FLAG_BASIC_TRAINER')
    
    print(f"   Trainers com IA inteligente: {smart_count}")
    print(f"   Trainers com IA básica: {basic_count}")
    
    if basic_count == 0:
        print("✅ Todos os trainers atualizados!")
    else:
        print(f"⚠️ Ainda existem {basic_count} trainers com IA básica")

def main():
    print("=" * 60)
    print("🤖 TRAINER AI UPDATER")
    print("=" * 60)
    print("Atualizando todos os trainers para IA inteligente...")
    
    backup()
    changes = update_all_trainers()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 IA inteligente ativada para todos os trainers!")
    print("=" * 60)
    print("\nFlags ativadas:")
    print("   AI_FLAG_SMART_TRAINER (inclui todas as inteligentes)")
    print("   AI_FLAG_SMART_SWITCHING")
    print("   AI_FLAG_SMART_MON_CHOICES")
    print("   AI_FLAG_OMNISCIENT")
    print("   AI_FLAG_PP_STALL_PREVENTION")
    print("\nPróximos passos:")
    print("   make clean && make")
    print("   New Game para testar")
    
    return 0

if __name__ == "__main__":
    exit(main())
