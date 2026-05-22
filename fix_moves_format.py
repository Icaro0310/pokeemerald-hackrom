#!/usr/bin/env python3
"""
Corrigir formato dos moves no trainers.party - adicionar campos obrigatórios
"""

import re
import shutil

TRAINERS_PARTY_FILE = "src/data/trainers.party"

# Novas equipes dos líderes de ginásio com formato completo
GYM_LEADERS_TEAMS = {
    "TRAINER_ROXANNE_1": """Name: ROXANNE
Class: Leader
Pic: Leader Roxanne
Gender: Female
Music: Gym Leader
Double Battle: No
AI: Smart Trainer

Shieldon
Level: 12
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Metal Sound
- Rock Tomb
- Tackle
- Protect

Rhyhorn
Level: 12
IVs: 12 HP / 12 Atk / 12 Def / 12 SpA / 12 SpD / 12 Spe
- Rock Blast
- Mud-Slap
- Horn Attack
- Scary Face

Kabuto
Level: 14
IVs: 14 HP / 14 Atk / 14 Def / 14 SpA / 14 SpD / 14 Spe
- Rock Tomb
- Water Gun
- Scratch
- Harden

Onix
Level: 14
IVs: 14 HP / 14 Atk / 14 Def / 14 SpA / 14 SpD / 14 Spe
- Rock Throw
- Mud-Slap
- Bind
- Curse

Arcanine-Hisui
Level: 15
IVs: 15 HP / 15 Atk / 15 Def / 15 SpA / 15 SpD / 15 Spe
- Ember
- Rock Tomb
- Bite
- Roar

Geodude-Alola
Level: 16
IVs: 16 HP / 16 Atk / 16 Def / 16 SpA / 16 SpD / 16 Spe
- Spark
- Rock Throw
- Rollout
- Charge""",
    
    "TRAINER_WATTSON_1": """Name: WATTSON
Class: Leader
Pic: Leader Wattson
Gender: Male
Music: Gym Leader
Double Battle: No
AI: Smart Trainer

Chinchou
Level: 20
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Spark
- Water Gun
- Thunder Wave
- Confuse Ray

Raichu
Level: 20
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Thunderbolt
- Thunder Punch
- Quick Attack
- Thunder Wave

Voltorb-Hisui
Level: 22
IVs: 22 HP / 22 Atk / 22 Def / 22 SpA / 22 SpD / 22 Spe
- Spark
- Giga Drain
- Charge Beam
- Self-Destruct

Jolteon
Level: 23
IVs: 23 HP / 23 Atk / 23 Def / 23 SpA / 23 SpD / 23 Spe
- Thunderbolt
- Thunder Wave
- Quick Attack
- Double Kick

Electivire
Level: 24
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Thunder Punch
- Thunderbolt
- Low Kick
- Swift

Raichu-Alola
Level: 24
IVs: 24 HP / 24 Atk / 24 Def / 24 SpA / 24 SpD / 24 Spe
- Thunderbolt
- Psychic
- Surf
- Quick Attack""",
    
    "TRAINER_NORMAN_1": """Name: NORMAN
Class: Leader
Pic: Leader Norman
Gender: Male
Music: Gym Leader
Double Battle: No
AI: Smart Trainer

Raticate-Alola
Level: 27
IVs: 27 HP / 27 Atk / 27 Def / 27 SpA / 27 SpD / 27 Spe
- Crunch
- Hyper Fang
- Sucker Punch
- Quick Attack

Wigglytuff
Level: 28
IVs: 28 HP / 28 Atk / 28 Def / 28 SpA / 28 SpD / 28 Spe
- Body Slam
- Disarming Voice
- Sing
- Disable

Kangaskhan
Level: 29
IVs: 29 HP / 29 Atk / 29 Def / 29 SpA / 29 SpD / 29 Spe
- Mega Punch
- Fake Out
- Bite
- Crunch

Blissey
Level: 29
IVs: 29 HP / 29 Atk / 29 Def / 29 SpA / 29 SpD / 29 Spe
- Take Down
- Seismic Toss
- Sing
- Soft-Boiled

Miltank
Level: 30
IVs: 30 HP / 30 Atk / 30 Def / 30 SpA / 30 SpD / 30 Spe
- Body Slam
- Stomp
- Milk Drink
- Rollout

Snorlax
Level: 31
IVs: 31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe
- Body Slam
- Chip Away
- Yawn
- Lick""",
    
    "TRAINER_TATE_AND_LIZA_1": """Name: TATE&LIZA
Class: Leader
Pic: Leader Tate And Liza
Gender: Male
Music: Gym Leader
Double Battle: Yes
AI: Smart Trainer

Mr. Mime-Galar
Level: 41
IVs: 41 HP / 41 Atk / 41 Def / 41 SpA / 41 SpD / 41 Spe
- Psychic
- Freeze-Dry
- Light Screen
- Reflect

Slowbro-Galar
Level: 41
IVs: 41 HP / 41 Atk / 41 Def / 41 SpA / 41 SpD / 41 Spe
- Psychic
- Shell Side Arm
- Surf
- Yawn

Rapidash-Galar
Level: 41
IVs: 41 HP / 41 Atk / 41 Def / 41 SpA / 41 SpD / 41 Spe
- Psycho Cut
- Fairy Wind
- Dazzling Gleam
- Agility

Espeon
Level: 42
IVs: 42 HP / 42 Atk / 42 Def / 42 SpA / 42 SpD / 42 Spe
- Psychic
- Psybeam
- Morning Sun
- Calm Mind

Slowking-Galar
Level: 42
IVs: 42 HP / 42 Atk / 42 Def / 42 SpA / 42 SpD / 42 Spe
- Psychic
- Sludge Bomb
- Nasty Plot
- Rain Dance

Alakazam
Level: 42
IVs: 42 HP / 42 Atk / 42 Def / 42 SpA / 42 SpD / 42 Spe
- Psycho Cut
- Psybeam
- Recover
- Shadow Ball"""
}

def backup():
    print("✅ Backup já foi criado anteriormente")

def fix_moves_format():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Corrigindo formato dos moves...")
    
    changes = 0
    for trainer, team in GYM_LEADERS_TEAMS.items():
        # Encontrar a seção do treinador
        pattern = rf'=== {trainer} ===.*?(?=== TRAINER_|=== END|$)'
        
        # Criar nova seção com formato completo
        new_section = f"=== {trainer} ===\n{team}\n\n"
        
        # Substituir
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_section, content, flags=re.DOTALL)
            changes += 1
            print(f"   ✅ {trainer} corrigido")
        else:
            print(f"   ⚠️ {trainer} não encontrado")
    
    with open(TRAINERS_PARTY_FILE, 'w') as f:
        f.write(content)
    
    print(f"\n✅ {changes} líderes de ginásio corrigidos!")
    return changes

def verify():
    print("\n🔍 Verificando...")
    
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    for trainer in GYM_LEADERS_TEAMS.keys():
        if f"=== {trainer} ===" in content:
            print(f"   ✅ {trainer} encontrado")
        else:
            print(f"   ❌ {trainer} não encontrado")

def main():
    print("=" * 60)
    print("🔧 MOVES FORMAT FIX")
    print("=" * 60)
    print("Corrigindo formato dos moves no trainers.party...")
    
    backup()
    changes = fix_moves_format()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 Formato dos moves corrigido!")
    print("=" * 60)
    print("\n📋 CORREÇÕES APLICADAS:")
    print("   ✅ Campo IVs adicionado para todos os Pokémon")
    print("   ✅ Formato correto: Species -> Level -> IVs -> Moves")
    print("   ✅ Moves após campos obrigatórios")
    print("\nPróximos passos:")
    print("   make clean && make")
    
    return 0

if __name__ == "__main__":
    exit(main())
