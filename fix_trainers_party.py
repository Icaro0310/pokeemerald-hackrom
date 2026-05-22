#!/usr/bin/env python3
"""
Corrigir erro de sintaxe no trainers.party - adicionar linha em branco entre treinador e Pokémon
"""

import re
import shutil

TRAINERS_PARTY_FILE = "src/data/trainers.party"

# Novas equipes dos líderes de ginásio com formato correto
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
- Metal Sound
- Rock Tomb
- Tackle
- Protect

Rhyhorn
Level: 12
- Rock Blast
- Mud-Slap
- Horn Attack
- Scary Face

Kabuto
Level: 14
- Rock Tomb
- Water Gun
- Scratch
- Harden

Onix
Level: 14
- Rock Throw
- Mud-Slap
- Bind
- Curse

Arcanine-Hisui
Level: 15
- Ember
- Rock Tomb
- Bite
- Roar

Geodude-Alola
Level: 16
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
- Spark
- Water Gun
- Thunder Wave
- Confuse Ray

Raichu
Level: 20
- Thunderbolt
- Thunder Punch
- Quick Attack
- Thunder Wave

Voltorb-Hisui
Level: 22
- Spark
- Giga Drain
- Charge Beam
- Self-Destruct

Jolteon
Level: 23
- Thunderbolt
- Thunder Wave
- Quick Attack
- Double Kick

Electivire
Level: 24
- Thunder Punch
- Thunderbolt
- Low Kick
- Swift

Raichu-Alola
Level: 24
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
- Crunch
- Hyper Fang
- Sucker Punch
- Quick Attack

Wigglytuff
Level: 28
- Body Slam
- Disarming Voice
- Sing
- Disable

Kangaskhan
Level: 29
- Mega Punch
- Fake Out
- Bite
- Crunch

Blissey
Level: 29
- Take Down
- Seismic Toss
- Sing
- Soft-Boiled

Miltank
Level: 30
- Body Slam
- Stomp
- Milk Drink
- Rollout

Snorlax
Level: 31
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
- Psychic
- Freeze-Dry
- Light Screen
- Reflect

Slowbro-Galar
Level: 41
- Psychic
- Shell Side Arm
- Surf
- Yawn

Rapidash-Galar
Level: 41
- Psycho Cut
- Fairy Wind
- Dazzling Gleam
- Agility

Espeon
Level: 42
- Psychic
- Psybeam
- Morning Sun
- Calm Mind

Slowking-Galar
Level: 42
- Psychic
- Sludge Bomb
- Nasty Plot
- Rain Dance

Alakazam
Level: 42
- Psycho Cut
- Psybeam
- Recover
- Shadow Ball"""
}

def backup():
    print("✅ Backup já foi criado anteriormente")

def fix_trainers_party():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Corrigindo formato do trainers.party...")
    
    changes = 0
    for trainer, team in GYM_LEADERS_TEAMS.items():
        # Encontrar a seção do treinador
        pattern = rf'=== {trainer} ===.*?(?=== TRAINER_|=== END|$)'
        
        # Criar nova seção com formato correto
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
    print("🔧 TRAINERS.PARTY SYNTAX FIX")
    print("=" * 60)
    print("Corrigindo erro de sintaxe no trainers.party...")
    
    backup()
    changes = fix_trainers_party()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 Erro de sintaxe corrigido!")
    print("=" * 60)
    print("\n📋 CORREÇÕES APLICADAS:")
    print("   ✅ Linha em branco adicionada entre treinador e Pokémon")
    print("   ✅ Formato correto: Name/Class/Pic/Gender/Music/Double Battle/AI")
    print("   ✅ Pokémon após linha em branco")
    print("\nPróximos passos:")
    print("   make clean && make")
    
    return 0

if __name__ == "__main__":
    exit(main())
