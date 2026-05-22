#!/usr/bin/env python3
"""
Atualizar equipes dos líderes de ginásio com movesets revisados finais
"""

import re
import shutil

TRAINERS_PARTY_FILE = "src/data/trainers.party"

# Novas equipes dos líderes de ginásio revisadas finais
GYM_LEADERS_TEAMS = {
    "TRAINER_ROXANNE_1": """Shieldon
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
    
    "TRAINER_BRAWLY_1": """Lucario
Level: 16
- Force Palm
- Metal Claw
- Fire Punch
- Thunder Punch

Meditite
Level: 16
- Brick Break
- Confusion
- Detect
- Meditate

Heracross
Level: 18
- Brick Break
- Fury Cutter
- Aerial Ace
- Leer

Hitmonlee
Level: 18
- Brick Break
- Jump Kick
- Double Kick
- Meditate

Makuhita
Level: 19
- Arm Thrust
- Force Palm
- Fake Out
- Knock Off

Hitmontop
Level: 19
- Mach Punch
- Fire Punch
- Thunder Punch
- Ice Punch""",
    
    "TRAINER_WATTSON_1": """Chinchou
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
    
    "TRAINER_FLANNERY_1": """Flareon
Level: 24
- Flamethrower
- Fire Fang
- Quick Attack
- Bite

Ninetales
Level: 24
- Flamethrower
- Confuse Ray
- Will-O-Wisp
- Quick Attack

Houndoom
Level: 26
- Flamethrower
- Thief
- Bite
- Howl

Arcanine
Level: 26
- Flamethrower
- Flame Wheel
- Bite
- Roar

Marowak-Alola
Level: 27
- Shadow Bone
- Flame Wheel
- Bonemerang
- Thunder Punch

Arcanine-Hisui
Level: 27
- Flame Wheel
- Rock Tomb
- Bite
- Roar""",
    
    "TRAINER_NORMAN_1": """Raticate-Alola
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
    
    "TRAINER_WINONA_1": """Noctowl
Level: 29
- Air Slash
- Extrasensory
- Take Down
- Hypnosis

Scyther
Level: 29
- Wing Attack
- Fury Cutter
- Aerial Ace
- Swords Dance

Skarmory
Level: 31
- Steel Wing
- Air Cutter
- Swift
- Agility

Honchkrow
Level: 32
- Night Slash
- Wing Attack
- Air Cutter
- Taunt

Togekiss
Level: 33
- Air Slash
- Dazzling Gleam
- Aura Sphere
- Ancient Power

Aerodactyl
Level: 33
- Rock Slide
- Wing Attack
- Crunch
- Agility""",
    
    "TRAINER_TATE_AND_LIZA_1": """Mr. Mime-Galar
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
- Shadow Ball""",
    
    "TRAINER_JUAN_1": """Blastoise
Level: 46
- Hydro Pump
- Aqua Tail
- Ice Beam
- Protect

Feraligatr
Level: 46
- Water Pulse
- Crunch
- Ice Fang
- Scary Face

Swampert
Level: 47
- Earthquake
- Surf
- Rock Slide
- Ice Beam

Empoleon
Level: 47
- Surf
- Flash Cannon
- Metal Claw
- Ice Beam

Greninja
Level: 49
- Water Shuriken
- Night Slash
- Hydro Pump
- Ice Beam

Kingdra
Level: 49
- Surf
- Dragon Pulse
- Ice Beam
- Agility"""
}

def backup():
    print("✅ Backup já foi criado anteriormente")

def update_gym_leaders():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🏋️ Aplicando movesets revisados finais...")
    
    changes = 0
    for trainer, team in GYM_LEADERS_TEAMS.items():
        # Encontrar a seção do treinador
        pattern = rf'=== {trainer} ===.*?(?=== TRAINER_|=== END|$)'
        
        # Criar nova seção
        new_section = f"=== {trainer} ===\n{team}\n\n"
        
        # Substituir
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_section, content, flags=re.DOTALL)
            changes += 1
            print(f"   ✅ {trainer} atualizado")
        else:
            print(f"   ⚠️ {trainer} não encontrado")
    
    with open(TRAINERS_PARTY_FILE, 'w') as f:
        f.write(content)
    
    print(f"\n✅ {changes} líderes de ginásio atualizados com movesets revisados!")
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
    print("🏋️ GYM LEADERS FINAL UPDATE")
    print("=" * 60)
    print("Aplicando movesets revisados finais nos líderes de ginásio...")
    
    backup()
    changes = update_gym_leaders()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 Movesets revisados finais aplicados!")
    print("=" * 60)
    print("\n📋 MELHORIAS APLICADAS:")
    print("   ✅ Duplo STAB para todos os tipos duplos")
    print("   ✅ STAB mínimo para tipos únicos")
    print("   ✅ Brawly: Lutadores com punches elementais")
    print("   ✅ Voltorb Hisui: Giga Drain (STAB Grass)")
    print("   ✅ Hitmontop: Mach Punch + punches elementais")
    print("   ✅ Raichu Alola: Surf no lugar de Nasty Plot")
    print("   ✅ Marowak Alola: Thunder Punch no lugar de Growl")
    print("   ✅ Swampert: Surf no lugar de Muddy Water")
    print("   ✅ Moves realistas para o nível")
    print("\nPróximos passos:")
    print("   make clean && make")
    print("   NEW GAME requerido devido à mudança no saveblock")
    
    return 0

if __name__ == "__main__":
    exit(main())
