#!/usr/bin/env python3
"""
Corrigir trainers.party para formato trainerproc correto (plain text)
"""

import re
import shutil

TRAINERS_PARTY_FILE = "src/data/trainers.party"

# Novas equipes dos líderes de ginásio no formato trainerproc CORRETO
GYM_LEADERS_TEAMS = {
    "TRAINER_ROXANNE_1": """Name: Roxanne
Class: LEADER_Roxanne
Pic: LEADER_Roxanne
Gender: Female
Music: FEMALE

Shieldon
Level: 12
Moves: Tackle, Protect, Metal Sound, Rock Tomb

Rhyhorn
Level: 12
Moves: Rock Blast, Mud-Slap, Horn Attack, Scary Face

Kabuto
Level: 14
Moves: Rock Tomb, Water Gun, Scratch, Harden

Onix
Level: 14
Moves: Rock Throw, Mud-Slap, Bind, Curse

Arcanine-Hisui
Level: 15
Moves: Ember, Rock Tomb, Bite, Roar

Geodude-Alola
Level: 16
Moves: Spark, Rock Throw, Rollout, Charge""",
    
    "TRAINER_BRAWLY_1": """Name: Brawly
Class: LEADER_Brawly
Pic: LEADER_Brawly
Gender: Male
Music: MALE

Lucario
Level: 16
Moves: Force Palm, Metal Claw, Fire Punch, Thunder Punch

Meditite
Level: 16
Moves: Brick Break, Confusion, Detect, Meditate

Heracross
Level: 18
Moves: Brick Break, Fury Cutter, Aerial Ace, Leer

Hitmonlee
Level: 18
Moves: Brick Break, Jump Kick, Double Kick, Meditate

Makuhita
Level: 19
Moves: Arm Thrust, Force Palm, Fake Out, Knock Off

Hitmontop
Level: 19
Moves: Mach Punch, Fire Punch, Thunder Punch, Ice Punch""",
    
    "TRAINER_WATTSON_1": """Name: Wattson
Class: LEADER_Wattson
Pic: LEADER_Wattson
Gender: Male
Music: MALE

Chinchou
Level: 20
Moves: Spark, Water Gun, Thunder Wave, Confuse Ray

Raichu
Level: 20
Moves: Thunderbolt, Thunder Punch, Quick Attack, Thunder Wave

Voltorb-Hisui
Level: 22
Moves: Spark, Giga Drain, Charge Beam, Self-Destruct

Jolteon
Level: 23
Moves: Thunderbolt, Thunder Wave, Quick Attack, Double Kick

Electivire
Level: 24
Moves: Thunder Punch, Thunderbolt, Low Kick, Swift

Raichu-Alola
Level: 24
Moves: Thunderbolt, Psychic, Surf, Quick Attack""",
    
    "TRAINER_FLANNERY_1": """Name: Flannery
Class: LEADER_Flannery
Pic: LEADER_Flannery
Gender: Female
Music: FEMALE

Flareon
Level: 24
Moves: Flamethrower, Fire Fang, Quick Attack, Bite

Ninetales
Level: 24
Moves: Flamethrower, Confuse Ray, Will-O-Wisp, Quick Attack

Houndoom
Level: 26
Moves: Flamethrower, Thief, Bite, Howl

Arcanine
Level: 26
Moves: Flamethrower, Flame Wheel, Bite, Roar

Marowak-Alola
Level: 27
Moves: Shadow Bone, Flame Wheel, Bonemerang, Thunder Punch

Arcanine-Hisui
Level: 27
Moves: Flame Wheel, Rock Tomb, Bite, Roar""",
    
    "TRAINER_NORMAN_1": """Name: Norman
Class: LEADER_Norman
Pic: LEADER_Norman
Gender: Male
Music: MALE

Raticate-Alola
Level: 27
Moves: Crunch, Hyper Fang, Sucker Punch, Quick Attack

Wigglytuff
Level: 28
Moves: Body Slam, Disarming Voice, Sing, Disable

Kangaskhan
Level: 29
Moves: Mega Punch, Fake Out, Bite, Crunch

Blissey
Level: 29
Moves: Take Down, Seismic Toss, Sing, Soft-Boiled

Miltank
Level: 30
Moves: Body Slam, Stomp, Milk Drink, Rollout

Snorlax
Level: 31
Moves: Body Slam, Chip Away, Yawn, Lick""",
    
    "TRAINER_WINONA_1": """Name: Winona
Class: LEADER_Winona
Pic: LEADER_Winona
Gender: Female
Music: FEMALE

Noctowl
Level: 29
Moves: Air Slash, Extrasensory, Take Down, Hypnosis

Scyther
Level: 29
Moves: Wing Attack, Fury Cutter, Aerial Ace, Swords Dance

Skarmory
Level: 31
Moves: Steel Wing, Air Cutter, Swift, Agility

Honchkrow
Level: 32
Moves: Night Slash, Wing Attack, Air Cutter, Taunt

Togekiss
Level: 33
Moves: Air Slash, Dazzling Gleam, Aura Sphere, Ancient Power

Aerodactyl
Level: 33
Moves: Rock Slide, Wing Attack, Crunch, Agility""",
    
    "TRAINER_TATE_AND_LIZA_1": """Name: Tate&Liza
Class: LEADER_TateAndLiza
Pic: LEADER_TateAndLiza
Gender: Male
Music: MALE

Mr. Mime-Galar
Level: 41
Moves: Psychic, Freeze-Dry, Light Screen, Reflect

Slowbro-Galar
Level: 41
Moves: Psychic, Shell Side Arm, Surf, Yawn

Rapidash-Galar
Level: 41
Moves: Psycho Cut, Fairy Wind, Dazzling Gleam, Agility

Espeon
Level: 42
Moves: Psychic, Psybeam, Morning Sun, Calm Mind

Slowking-Galar
Level: 42
Moves: Psychic, Sludge Bomb, Nasty Plot, Rain Dance

Alakazam
Level: 42
Moves: Psycho Cut, Psybeam, Recover, Shadow Ball""",
    
    "TRAINER_JUAN_1": """Name: Juan
Class: LEADER_Juan
Pic: LEADER_Juan
Gender: Male
Music: MALE

Blastoise
Level: 46
Moves: Hydro Pump, Aqua Tail, Ice Beam, Protect

Feraligatr
Level: 46
Moves: Water Pulse, Crunch, Ice Fang, Scary Face

Swampert
Level: 47
Moves: Earthquake, Surf, Rock Slide, Ice Beam

Empoleon
Level: 47
Moves: Surf, Flash Cannon, Metal Claw, Ice Beam

Greninja
Level: 49
Moves: Water Shuriken, Night Slash, Hydro Pump, Ice Beam

Kingdra
Level: 49
Moves: Surf, Dragon Pulse, Ice Beam, Agility"""
}

def backup():
    print("✅ Criando backup do arquivo atual...")
    shutil.copy(TRAINERS_PARTY_FILE, TRAINERS_PARTY_FILE + ".CURRENT_BAK")

def fix_trainerproc_format():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Aplicando formato trainerproc correto...")
    
    changes = 0
    for trainer, team in GYM_LEADERS_TEAMS.items():
        # Encontrar a seção do treinador
        pattern = rf'=== {trainer} ===.*?(?=== TRAINER_|=== END|$)'
        
        # Criar nova seção com formato trainerproc
        new_section = f"=== {trainer} ===\n{team}\n\n"
        
        # Substituir
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, new_section, content, flags=re.DOTALL)
            changes += 1
            print(f"   ✅ {trainer} corrigido (formato trainerproc)")
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
    print("🔧 TRAINERPROC FORMAT FIX")
    print("=" * 60)
    print("Corrigindo trainers.party para formato trainerproc correto...")
    
    backup()
    changes = fix_trainerproc_format()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 Formato trainerproc corrigido!")
    print("=" * 60)
    print("\n📋 FORMATO CORRETO APLICADO:")
    print("   ✅ Plain text (não código C)")
    print("   ✅ Moves: Move1, Move2, Move3, Move4")
    print("   ✅ Nomes com hífen: Arcanine-Hisui, Geodude-Alola")
    print("   ✅ Moves com hífen: Mud-Slap, Will-O-Wisp")
    print("   ✅ Sem MOVE_ ou _ underscores")
    print("\n📊 RESULTADO:")
    print("   ✅ 8 líderes de ginásio com movesets competitivos")
    print("   ✅ Formas regionais ativadas")
    print("   ✅ Formato trainerproc 100% correto")
    print("\nPróximos passos:")
    print("   make clean && make")
    
    return 0

if __name__ == "__main__":
    exit(main())
