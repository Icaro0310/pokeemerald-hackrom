#!/usr/bin/env python3
"""
Corrigir ordem dos campos Moves em TODOS os blocos Pokémon
"""

import re

TRAINERS_PARTY_FILE = "src/data/trainers.party"

def fix_all_moves_order():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Corrigindo ordem dos campos Moves em todos os blocos...")
    
    # Padrão para encontrar blocos Pokémon com Moves fora de ordem
    # Procura: Species -> Level -> Moves (errado)
    pokemon_pattern = r'([A-Za-z0-9\-]+)\nLevel: (\d+)\nMoves: ([^\n]+)\n'
    
    def replace_pokemon_block(match):
        species = match.group(1)
        level = match.group(2)
        moves = match.group(3)
        
        # Determinar IVs e Ability baseado no Pokémon
        ivs, ability, nature, item = get_pokemon_stats(species, int(level))
        
        # Converter moves para formato com traços
        moves_list = moves.split(', ')
        moves_formatted = '\n'.join(f'- {move}' for move in moves_list)
        
        # Reconstruir na ordem correta
        return f"""{species}
Level: {level}
IVs: {ivs}
Ability: {ability}
Nature: {nature}
Item: {item}
Moves:
{moves_formatted}
"""
    
    # Aplicar correção em todo o arquivo
    original_content = content
    content = re.sub(pokemon_pattern, replace_pokemon_block, content)
    
    changes = content != original_content
    
    with open(TRAINERS_PARTY_FILE, 'w') as f:
        f.write(content)
    
    print(f"✅ {'Correções aplicadas' if changes else 'Nenhuma correção necessária'}!")
    return changes

def get_pokemon_stats(species, level):
    """Retorna IVs, Ability, Nature e Item baseados no Pokémon e nível"""
    
    # Base stats para diferentes níveis
    if level <= 20:
        ivs = "20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe"
    elif level <= 30:
        ivs = "25 HP / 25 Atk / 25 Def / 25 SpA / 25 SpD / 25 Spe"
    else:
        ivs = "31 HP / 31 Atk / 31 Def / 31 SpA / 31 SpD / 31 Spe"
    
    # Abilities baseadas no Pokémon
    abilities = {
        'Shieldon': 'Sturdy',
        'Rhyhorn': 'Rock Head',
        'Kabuto': 'Battle Armor',
        'Onix': 'Rock Head',
        'Arcanine-Hisui': 'Intimidate',
        'Geodude-Alola': 'Magnet Pull',
        'Lucario': 'Steadfast',
        'Meditite': 'Pure Power',
        'Heracross': 'Guts',
        'Hitmonlee': 'Reckless',
        'Makuhita': 'Thick Fat',
        'Hitmontop': 'Intimidate',
        'Chinchou': 'Volt Absorb',
        'Raichu': 'Static',
        'Voltorb-Hisui': 'Soundproof',
        'Jolteon': 'Volt Absorb',
        'Electivire': 'Motor Drive',
        'Raichu-Alola': 'Surge Surfer',
        'Flareon': 'Flash Fire',
        'Ninetales': 'Flash Fire',
        'Houndoom': 'Flash Fire',
        'Arcanine': 'Intimidate',
        'Marowak-Alola': 'Cursed Body',
        'Raticate-Alola': 'Hustle',
        'Wigglytuff': 'Cute Charm',
        'Kangaskhan': 'Early Bird',
        'Blissey': 'Natural Cure',
        'Miltank': 'Thick Fat',
        'Snorlax': 'Thick Fat',
        'Noctowl': 'Insomnia',
        'Scyther': 'Swarm',
        'Skarmory': 'Keen Eye',
        'Honchkrow': 'Moxie',
        'Togekiss': 'Serene Grace',
        'Aerodactyl': 'Pressure',
        'Mr. Mime-Galar': 'Screen Cleaner',
        'Slowbro-Galar': 'Regenerator',
        'Rapidash-Galar': 'Pastel Veil',
        'Espeon': 'Magic Bounce',
        'Slowking-Galar': 'Regenerator',
        'Alakazam': 'Magic Guard',
        'Blastoise': 'Torrent',
        'Feraligatr': 'Torrent',
        'Swampert': 'Torrent',
        'Empoleon': 'Torrent',
        'Greninja': 'Protean',
        'Kingdra': 'Swift Swim'
    }
    
    ability = abilities.get(species, 'Sturdy')
    
    # Natures baseadas no tipo do Pokémon
    physical_pokemon = ['Shieldon', 'Rhyhorn', 'Kabuto', 'Onix', 'Arcanine-Hisui', 'Geodude-Alola', 
                       'Lucario', 'Heracross', 'Hitmonlee', 'Makuhita', 'Hitmontop', 'Raichu', 
                       'Flareon', 'Arcanine', 'Marowak-Alola', 'Raticate-Alola', 'Kangaskhan', 
                       'Miltank', 'Snorlax', 'Scyther', 'Skarmory', 'Honchkrow', 'Aerodactyl', 
                       'Rapidash-Galar', 'Feraligatr', 'Swampert']
    
    special_pokemon = ['Geodude-Alola', 'Chinchou', 'Voltorb-Hisui', 'Jolteon', 'Electivire', 
                       'Raichu-Alola', 'Ninetales', 'Houndoom', 'Wigglytuff', 'Noctowl', 
                       'Togekiss', 'Mr. Mime-Galar', 'Slowbro-Galar', 'Espeon', 'Slowking-Galar', 
                       'Alakazam', 'Blastoise', 'Empoleon', 'Greninja', 'Kingdra']
    
    if species in physical_pokemon:
        nature = 'Adamant' if species not in ['Snorlax', 'Blissey', 'Miltank'] else 'Careful'
    elif species in special_pokemon:
        nature = 'Modest' if species not in ['Blissey'] else 'Bold'
    else:
        nature = 'Adamant'
    
    # Items baseados no Pokémon
    items = {
        'Shieldon': 'Oran Berry',
        'Rhyhorn': 'Hard Stone',
        'Kabuto': 'Soft Sand',
        'Onix': 'Hard Stone',
        'Arcanine-Hisui': 'Charcoal',
        'Geodude-Alola': 'Hard Stone',
        'Lucario': 'Focus Sash',
        'Meditite': 'Expert Belt',
        'Heracross': 'Choice Band',
        'Hitmonlee': 'Life Orb',
        'Makuhita': 'Leftovers',
        'Hitmontop': 'Life Orb',
        'Chinchou': 'Leftovers',
        'Raichu': 'Magnet',
        'Voltorb-Hisui': 'Focus Sash',
        'Jolteon': 'Life Orb',
        'Electivire': 'Expert Belt',
        'Raichu-Alola': 'Life Orb',
        'Flareon': 'Life Orb',
        'Ninetales': 'Leftovers',
        'Houndoom': 'Life Orb',
        'Arcanine': 'Life Orb',
        'Marowak-Alola': 'Thick Club',
        'Raticate-Alola': 'Life Orb',
        'Wigglytuff': 'Leftovers',
        'Kangaskhan': 'Leftovers',
        'Blissey': 'Leftovers',
        'Miltank': 'Leftovers',
        'Snorlax': 'Leftovers',
        'Noctowl': 'Leftovers',
        'Scyther': 'Life Orb',
        'Skarmory': 'Leftovers',
        'Honchkrow': 'Life Orb',
        'Togekiss': 'Life Orb',
        'Aerodactyl': 'Life Orb',
        'Mr. Mime-Galar': 'Leftovers',
        'Slowbro-Galar': 'Leftovers',
        'Rapidash-Galar': 'Life Orb',
        'Espeon': 'Life Orb',
        'Slowking-Galar': 'Leftovers',
        'Alakazam': 'Life Orb',
        'Blastoise': 'Leftovers',
        'Feraligatr': 'Life Orb',
        'Swampert': 'Life Orb',
        'Empoleon': 'Life Orb',
        'Greninja': 'Life Orb',
        'Kingdra': 'Life Orb'
    }
    
    item = items.get(species, 'Leftovers')
    
    return ivs, ability, nature, item

def verify():
    print("\n🔍 Verificando correções...")
    
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    # Verificar se ainda há "Moves:" sem campos obrigatórios antes
    problematic_lines = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if 'Moves:' in line and i > 0:
            # Verificar linhas anteriores
            prev_lines = lines[max(0, i-5):i]
            has_level = any('Level:' in l for l in prev_lines)
            has_ivs = any('IVs:' in l for l in prev_lines)
            has_ability = any('Ability:' in l for l in prev_lines)
            has_nature = any('Nature:' in l for l in prev_lines)
            
            if not (has_level and has_ivs and has_ability and has_nature):
                problematic_lines.append(f"Linha {i+1}: {line.strip()}")
    
    if problematic_lines:
        print("   ❌ Linhas problemáticas encontradas:")
        for line in problematic_lines[:5]:  # Mostrar apenas as 5 primeiras
            print(f"      {line}")
        if len(problematic_lines) > 5:
            print(f"      ... e mais {len(problematic_lines) - 5} linhas")
        return False
    else:
        print("   ✅ Nenhuma linha problemática encontrada")
        return True

def main():
    print("=" * 60)
    print("🔧 CORREÇÃO ORDEM DOS CAMPOS MOVES - COMPLETA")
    print("=" * 60)
    print("Corrigindo ordem dos campos em TODOS os blocos Pokémon...")
    
    changes = fix_all_moves_order()
    success = verify()
    
    print("\n" + "=" * 60)
    print("🎉 ORDEM DOS CAMPOS CORRIGIDA!" if success else "❌ ERROS AINDA PRESENTES")
    print("=" * 60)
    print("\n📋 ORDEM CORRETA APLICADA:")
    print("   ✅ Species")
    print("   ✅ Level")
    print("   ✅ IVs")
    print("   ✅ Ability")
    print("   ✅ Nature")
    print("   ✅ Item")
    print("   ✅ Moves:")
    print("   ✅ - Move1")
    print("   ✅ - Move2")
    print("   ✅ - Move3")
    print("   ✅ - Move4")
    
    if success:
        print("\n🔧 PRÓXIMO PASSO:")
        print("   make clean && make")
    else:
        print("\n❌ CORREÇÕES ADICIONAIS NECESSÁRIAS")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
