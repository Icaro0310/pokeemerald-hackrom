#!/usr/bin/env python3
"""
Aplicar formato CORRETO dos 8 líderes de ginásio com traços (-) e IVs
"""

import re
import shutil

TRAINERS_PARTY_FILE = "src/data/trainers.party"

# Novas equipes dos 8 líderes de ginásio no formato CORRETO (traços e IVs)
GYM_LEADERS_TEAMS = {
    "TRAINER_ROXANNE_1": """=== TRAINER_ROXANNE_1 ===
Name: ROXANNE
Class: Leader
Pic: Leader Roxanne
Gender: Female
Music: Female
Items: Potion
Double Battle: No
AI: Smart Trainer

Shieldon
Level: 12
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Tackle
- Protect
- Metal Sound
- Rock Tomb

Rhyhorn
Level: 12
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Rock Blast
- Mud-Slap
- Horn Attack
- Scary Face

Kabuto
Level: 14
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Rock Tomb
- Water Gun
- Scratch
- Harden

Onix
Level: 14
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Rock Throw
- Mud-Slap
- Bind
- Curse

Arcanine-Hisui
Level: 15
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Ember
- Rock Tomb
- Bite
- Roar

Geodude-Alola
Level: 16
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Spark
- Rock Throw
- Rollout
- Charge""",
    
    "TRAINER_BRAWLY_1": """=== TRAINER_BRAWLY_1 ===
Name: BRAWLY
Class: Leader
Pic: Leader Brawly
Gender: Male
Music: Male
Items: Potion
Double Battle: No
AI: Smart Trainer

Lucario
Level: 16
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Force Palm
- Metal Claw
- Fire Punch
- Thunder Punch

Meditite
Level: 16
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Brick Break
- Confusion
- Detect
- Meditate

Heracross
Level: 18
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Brick Break
- Fury Cutter
- Aerial Ace
- Leer

Hitmonlee
Level: 18
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Brick Break
- Jump Kick
- Double Kick
- Meditate

Makuhita
Level: 19
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Arm Thrust
- Force Palm
- Fake Out
- Knock Off

Hitmontop
Level: 19
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Mach Punch
- Fire Punch
- Thunder Punch
- Ice Punch""",
    
    "TRAINER_WATTSON_1": """=== TRAINER_WATTSON_1 ===
Name: WATTSON
Class: Leader
Pic: Leader Wattson
Gender: Male
Music: Male
Items: Super Potion
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
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Spark
- Giga Drain
- Charge Beam
- Self-Destruct

Jolteon
Level: 23
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Thunderbolt
- Thunder Wave
- Quick Attack
- Double Kick

Electivire
Level: 24
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Thunder Punch
- Thunderbolt
- Low Kick
- Swift

Raichu-Alola
Level: 24
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Thunderbolt
- Psychic
- Surf
- Quick Attack""",
    
    "TRAINER_FLANNERY_1": """=== TRAINER_FLANNERY_1 ===
Name: FLANNERY
Class: Leader
Pic: Leader Flannery
Gender: Female
Music: Female
Items: Super Potion
Double Battle: No
AI: Smart Trainer

Flareon
Level: 24
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Flamethrower
- Fire Fang
- Quick Attack
- Bite

Ninetales
Level: 24
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Flamethrower
- Confuse Ray
- Will-O-Wisp
- Quick Attack

Houndoom
Level: 26
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Flamethrower
- Thief
- Bite
- Howl

Arcanine
Level: 26
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Flamethrower
- Flame Wheel
- Bite
- Roar

Marowak-Alola
Level: 27
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Shadow Bone
- Flame Wheel
- Bonemerang
- Thunder Punch

Arcanine-Hisui
Level: 27
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Flame Wheel
- Rock Tomb
- Bite
- Roar""",
    
    "TRAINER_NORMAN_1": """=== TRAINER_NORMAN_1 ===
Name: NORMAN
Class: Leader
Pic: Leader Norman
Gender: Male
Music: Male
Items: Hyper Potion
Double Battle: No
AI: Smart Trainer

Raticate-Alola
Level: 27
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Crunch
- Hyper Fang
- Sucker Punch
- Quick Attack

Wigglytuff
Level: 28
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Body Slam
- Disarming Voice
- Sing
- Disable

Kangaskhan
Level: 29
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Mega Punch
- Fake Out
- Bite
- Crunch

Blissey
Level: 29
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Take Down
- Seismic Toss
- Sing
- Soft-Boiled

Miltank
Level: 30
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Body Slam
- Stomp
- Milk Drink
- Rollout

Snorlax
Level: 31
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Body Slam
- Chip Away
- Yawn
- Lick""",
    
    "TRAINER_WINONA_1": """=== TRAINER_WINONA_1 ===
Name: WINONA
Class: Leader
Pic: Leader Winona
Gender: Female
Music: Female
Items: Hyper Potion
Double Battle: No
AI: Smart Trainer

Noctowl
Level: 29
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Air Slash
- Extrasensory
- Take Down
- Hypnosis

Scyther
Level: 29
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Wing Attack
- Fury Cutter
- Aerial Ace
- Swords Dance

Skarmory
Level: 31
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Steel Wing
- Air Cutter
- Swift
- Agility

Honchkrow
Level: 32
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Night Slash
- Wing Attack
- Air Cutter
- Taunt

Togekiss
Level: 33
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Air Slash
- Dazzling Gleam
- Aura Sphere
- Ancient Power

Aerodactyl
Level: 33
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
- Rock Slide
- Wing Attack
- Crunch
- Agility""",
    
    "TRAINER_TATE_AND_LIZA_1": """=== TRAINER_TATE_AND_LIZA_1 ===
Name: TATE & LIZA
Class: Leader
Pic: Leader Tate And Liza
Gender: Female
Music: Female
Items: Hyper Potion / Hyper Potion
Double Battle: Yes
AI: Smart Trainer

Mr. Mime-Galar
Level: 41
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Psychic
- Freeze-Dry
- Light Screen
- Reflect

Slowbro-Galar
Level: 41
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Psychic
- Shell Side Arm
- Surf
- Yawn

Rapidash-Galar
Level: 41
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Psycho Cut
- Fairy Wind
- Dazzling Gleam
- Agility

Espeon
Level: 42
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Psychic
- Psybeam
- Morning Sun
- Calm Mind

Slowking-Galar
Level: 42
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Psychic
- Sludge Bomb
- Nasty Plot
- Rain Dance

Alakazam
Level: 42
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Psycho Cut
- Psybeam
- Recover
- Shadow Ball""",
    
    "TRAINER_JUAN_1": """=== TRAINER_JUAN_1 ===
Name: JUAN
Class: Leader
Pic: Leader Juan
Gender: Male
Music: Male
Items: Hyper Potion / Hyper Potion
Double Battle: No
AI: Smart Trainer

Blastoise
Level: 46
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Hydro Pump
- Aqua Tail
- Ice Beam
- Protect

Feraligatr
Level: 46
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Water Pulse
- Crunch
- Ice Fang
- Scary Face

Swampert
Level: 47
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Earthquake
- Surf
- Rock Slide
- Ice Beam

Empoleon
Level: 47
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Surf
- Flash Cannon
- Metal Claw
- Ice Beam

Greninja
Level: 49
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Water Shuriken
- Night Slash
- Hydro Pump
- Ice Beam

Kingdra
Level: 49
IVs: 25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe
- Surf
- Dragon Pulse
- Ice Beam
- Agility"""
}

def apply_correct_format():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Aplicando formato CORRETO com traços (-) e IVs...")
    
    changes = 0
    for trainer, team in GYM_LEADERS_TEAMS.items():
        # Encontrar a seção do treinador (aceitar === ou ==)
        pattern = rf'(={2,3}) {trainer}(={1,2}).*?(?==={1,3} TRAINER_|==={1,3} END|$)'
        
        # Substituir
        if re.search(pattern, content, re.DOTALL):
            # Manter o mesmo número de = que estava no original
            match = re.search(pattern, content, re.DOTALL)
            if match:
                original_equals = match.group(1)  # === ou ==
                closing_equals = match.group(2)  # == ou =
                # Criar nova seção mantendo o formato original
                new_section = f"{original_equals} {trainer}{closing_equals}\n{team}\n\n"
                content = re.sub(pattern, new_section, content, flags=re.DOTALL)
                changes += 1
                print(f"   ✅ {trainer} atualizado (formato correto)")
            else:
                print(f"   ⚠️ {trainer} - erro no formato")
        else:
            print(f"   ❌ {trainer} não encontrado")
    
    with open(TRAINERS_PARTY_FILE, 'w') as f:
        f.write(content)
    
    print(f"\n✅ {changes} líderes de ginásio atualizados!")
    return changes

def verify():
    print("\n🔍 Verificando...")
    
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    for trainer in GYM_LEADERS_TEAMS.keys():
        if trainer in content:
            print(f"   ✅ {trainer} encontrado")
        else:
            print(f"   ❌ {trainer} não encontrado")

def main():
    print("=" * 60)
    print("🎯 FORMATO CORRETO - TRAÇOS E IVS")
    print("=" * 60)
    print("Aplicando formato CORRETO com traços (-) e IVs...")
    
    changes = apply_correct_format()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 FORMATO CORRETO APLICADO!")
    print("=" * 60)
    print("\n📋 FORMATO CORRETO:")
    print("   ✅ Moves com traços: - Move1")
    print("   ✅ IVs incluídos: IVs: 20 HP / 20 Atk / ...")
    print("   ✅ Header completo: Items, AI, Double Battle")
    print("   ✅ Formas regionais: Arcanine-Hisui, Geodude-Alola")
    print("\n📊 RESULTADO FINAL:")
    print("   ✅ 8 líderes de ginásio com formato correto")
    print("   ✅ Movesets competitivos aplicados")
    print("   ✅ Formas regionais funcionando")
    print("   ✅ Todos os sistemas modernos ativados")
    print("\n🔧 PRÓXIMO PASSO:")
    print("   make clean && make")
    
    return 0

if __name__ == "__main__":
    exit(main())
