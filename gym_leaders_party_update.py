#!/usr/bin/env python3
"""
Atualizar equipes dos líderes de ginásio no arquivo trainers.party
"""

import re
import shutil

TRAINERS_PARTY_FILE = "src/data/trainers.party"

# Novas equipes dos líderes de ginásio no formato competitive syntax
GYM_LEADERS_TEAMS = {
    "TRAINER_ROXANNE_1": """Shieldon
Level: 12
- Tackle
- Protect
- Metal Sound
- Rock Tomb

Rhyhorn
Level: 12
- Horn Attack
- Rock Tomb
- Bulldoze
- Tail Whip

Kabuto
Level: 14
- Aqua Jet
- Rock Tomb
- Scratch
- Harden

Onix
Level: 14
- Rock Throw
- Bind
- Curse
- Stealth Rock

Arcanine-Hisui
Level: 15
- Bite
- Flame Wheel
- Rock Slide
- Extreme Speed

Geodude-Alola
Level: 16
- Tackle
- Rock Throw
- Spark
- Rollout""",
    
    "TRAINER_BRAWLY_1": """Lucario
Level: 16
- Force Palm
- Metal Claw
- Counter
- Quick Attack

Meditite
Level: 16
- Confusion
- High Jump Kick
- Meditate
- Detect

Heracross
Level: 18
- Horn Attack
- Aerial Ace
- Counter
- Leer

Hitmonlee
Level: 18
- Double Kick
- Bulk Up
- Mach Punch
- Fake Out

Makuhita
Level: 19
- Arm Thrust
- Vital Throw
- Fake Out
- Bulk Up

Hitmontop
Level: 19
- Triple Kick
- Mach Punch
- Quick Attack
- Detect""",
    
    "TRAINER_WATTSON_1": """Chinchou
Level: 20
- Bubble Beam
- Thunder Wave
- Spark
- Supersonic

Raichu
Level: 20
- Thunderbolt
- Quick Attack
- Tail Whip
- Thunder Wave

Voltorb-Hisui
Level: 22
- Spark
- Energy Ball
- Thunder Wave
- Self-Destruct

Jolteon
Level: 23
- Thunderbolt
- Quick Attack
- Double Kick
- Thunder Wave

Electivire
Level: 24
- Thunder Punch
- Low Kick
- Thunder Wave
- Quick Attack

Raichu-Alola
Level: 24
- Psychic
- Thunderbolt
- Quick Attack
- Nasty Plot""",
    
    "TRAINER_FLANNERY_1": """Flareon
Level: 24
- Flamethrower
- Quick Attack
- Bite
- Will-O-Wisp

Ninetales
Level: 24
- Flamethrower
- Confuse Ray
- Will-O-Wisp
- Quick Attack

Houndoom
Level: 26
- Flamethrower
- Bite
- Smog
- Nasty Plot

Arcanine
Level: 26
- Flamethrower
- Extreme Speed
- Crunch
- Agility

Marowak-Alola
Level: 27
- Flare Blitz
- Shadow Bone
- Bone Club
- Will-O-Wisp

Arcanine-Hisui
Level: 27
- Rock Slide
- Flame Wheel
- Extreme Speed
- Crunch""",
    
    "TRAINER_NORMAN_1": """Raticate-Alola
Level: 27
- Crunch
- Quick Attack
- Super Fang
- Hyper Fang

Wigglytuff
Level: 28
- Body Slam
- Play Rough
- Sing
- Disable

Kangaskhan
Level: 29
- Comet Punch
- Bite
- Tail Whip
- Fake Out

Blissey
Level: 29
- Soft-Boiled
- Seismic Toss
- Sing
- Minimize

Miltank
Level: 30
- Body Slam
- Milk Drink
- Rollout
- Attract

Snorlax
Level: 31
- Body Slam
- Yawn
- Defense Curl
- Lick""",
    
    "TRAINER_WINONA_1": """Noctowl
Level: 29
- Air Slash
- Extrasensory
- Hypnosis
- Reflect

Scyther
Level: 29
- Aerial Ace
- X-Scissor
- Quick Attack
- Slash

Skarmory
Level: 31
- Air Slash
- Steel Wing
- Spikes
- Agility

Honchkrow
Level: 32
- Night Slash
- Drill Peck
- Haze
- Tailwind

Togekiss
Level: 33
- Air Slash
- Aura Sphere
- Ancient Power
- Yawn

Aerodactyl
Level: 33
- Rock Slide
- Wing Attack
- Bite
- Agility""",
    
    "TRAINER_TATE_AND_LIZA_1": """Mr. Mime-Galar
Level: 41
- Psychic
- Freeze-Dry
- Light Screen
- Reflect

Slowbro-Galar
Level: 41
- Shell Side Arm
- Psychic
- Surf
- Yawn

Rapidash-Galar
Level: 41
- Psycho Cut
- Play Rough
- Megahorn
- Will-O-Wisp

Espeon
Level: 42
- Psychic
- Shadow Ball
- Morning Sun
- Calm Mind

Slowking-Galar
Level: 42
- Eerie Spell
- Surf
- Power Gem
- Nasty Plot

Alakazam
Level: 42
- Psychic
- Shadow Ball
- Recover
- Calm Mind""",
    
    "TRAINER_JUAN_1": """Blastoise
Level: 46
- Hydro Pump
- Ice Beam
- Flash Cannon
- Protect

Feraligatr
Level: 46
- Aqua Tail
- Crunch
- Ice Fang
- Dragon Dance

Swampert
Level: 47
- Earthquake
- Surf
- Ice Beam
- Hammer Arm

Empoleon
Level: 47
- Hydro Pump
- Flash Cannon
- Ice Beam
- Drill Peck

Greninja
Level: 49
- Hydro Pump
- Dark Pulse
- Ice Beam
- Extrasensory

Kingdra
Level: 49
- Hydro Pump
- Dragon Pulse
- Ice Beam
- Agility"""
}

def backup():
    print("✅ Backup já foi criado anteriormente")

def update_gym_leaders():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🏋️ Atualizando equipes dos líderes de ginásio...")
    
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
    
    print(f"\n✅ {changes} líderes de ginásio atualizados!")
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
    print("🏋️ GYM LEADERS PARTY UPDATER")
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
    print("   - trainers.party atualizado")
    print("\nPróximos passos:")
    print("   Reativar COMPETITIVE_PARTY_SYNTAX em general.h")
    print("   make clean && make")
    print("   NEW GAME requerido devido à mudança no saveblock")
    
    return 0

if __name__ == "__main__":
    exit(main())
