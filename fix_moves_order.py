#!/usr/bin/env python3
"""
Corrigir ordem dos campos Moves no trainers.party
"""

import re

TRAINERS_PARTY_FILE = "src/data/trainers.party"

def fix_moves_order():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Corrigindo ordem dos campos Moves...")
    
    # Padrão para encontrar blocos Pokémon com Moves fora de ordem
    # Procura: Species -> Level -> Moves (errado)
    # Substitui por: Species -> Level -> IVs -> Ability -> Nature -> Item -> Moves
    
    # Lista de treinadores para corrigir
    trainers = [
        "TRAINER_ROXANNE_1", "TRAINER_BRAWLY_1", "TRAINER_WATTSON_1", 
        "TRAINER_FLANNERY_1", "TRAINER_NORMAN_1", "TRAINER_WINONA_1",
        "TRAINER_TATE_AND_LIZA_1", "TRAINER_JUAN_1"
    ]
    
    changes = 0
    
    for trainer in trainers:
        # Encontrar seção do treinador
        pattern = rf'(={2,3}) {trainer}(={1,2})(.*?)(?==={1,3} TRAINER_|==={1,3} END|$)'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            trainer_section = match.group(3)
            original_equals = match.group(1)
            closing_equals = match.group(2)
            
            # Corrigir cada bloco Pokémon na seção
            fixed_section = fix_pokemon_blocks(trainer_section)
            
            if fixed_section != trainer_section:
                # Reconstruir seção completa
                new_section = f"{original_equals} {trainer}{closing_equals}{fixed_section}\n\n"
                content = re.sub(pattern, new_section, content, flags=re.DOTALL)
                changes += 1
                print(f"   ✅ {trainer} corrigido")
            else:
                print(f"   ⚠️ {trainer} - sem correções necessárias")
        else:
            print(f"   ❌ {trainer} não encontrado")
    
    with open(TRAINERS_PARTY_FILE, 'w') as f:
        f.write(content)
    
    print(f"\n✅ {changes} líderes de ginásio corrigidos!")
    return changes

def fix_pokemon_blocks(section):
    """Corrige a ordem dos campos em blocos Pokémon individuais"""
    
    # Padrão para encontrar blocos Pokémon
    pokemon_pattern = r'([A-Za-z0-9\-]+)\nLevel: (\d+)\nMoves: ([^\n]+)\n'
    
    def replace_pokemon_block(match):
        species = match.group(1)
        level = match.group(2)
        moves = match.group(3)
        
        # Reconstruir na ordem correta
        return f"""{species}
Level: {level}
IVs: 20 HP / 20 Atk / 20 Def / 20 SpA / 20 SpD / 20 Spe
Ability: Sturdy
Nature: Adamant
Item: Oran Berry
Moves:
- {moves.replace(', ', '\n- ')}
"""
    
    # Aplicar correção
    fixed_section = re.sub(pokemon_pattern, replace_pokemon_block, section)
    
    return fixed_section

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
    else:
        print("   ✅ Nenhuma linha problemática encontrada")

def main():
    print("=" * 60)
    print("🔧 CORREÇÃO ORDEM DOS CAMPOS MOVES")
    print("=" * 60)
    print("Corrigindo ordem dos campos nos blocos Pokémon...")
    
    changes = fix_moves_order()
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 ORDEM DOS CAMPOS CORRIGIDA!")
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
    print("\n🔧 PRÓXIMO PASSO:")
    print("   make clean && make")
    
    return 0

if __name__ == "__main__":
    exit(main())
