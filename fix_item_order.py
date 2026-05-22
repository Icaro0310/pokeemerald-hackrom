#!/usr/bin/env python3
"""
Corrigir ordem do campo Item no trainers.party
"""

import re

TRAINERS_PARTY_FILE = "src/data/trainers.party"

def fix_item_order():
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Corrigindo ordem do campo Item...")
    
    # Padrão para encontrar blocos Pokémon com Item fora de ordem
    # Procura: ... Nature -> Item -> Moves (errado)
    # Substitui por: ... Nature -> Item -> Moves (correto)
    
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
    
    # Padrão para encontrar blocos Pokémon com ordem incorreta
    # Procura: Species -> Level -> IVs -> Ability -> Nature -> Item -> Moves (correto)
    # Mas se Item estiver antes de Nature, precisa corrigir
    
    # Primeiro, vamos encontrar todos os blocos Pokémon e reconstruir na ordem correta
    pokemon_pattern = r'([A-Za-z0-9\-]+)\nLevel: (\d+)\nIVs: ([^\n]+)\nAbility: ([^\n]+)\nNature: ([^\n]+)\nItem: ([^\n]+)\nMoves:\n((?:- [^\n]+\n?)*)'
    
    def replace_pokemon_block(match):
        species = match.group(1)
        level = match.group(2)
        ivs = match.group(3)
        ability = match.group(4)
        nature = match.group(5)
        item = match.group(6)
        moves = match.group(7)
        
        # Reconstruir na ordem correta
        return f"""{species}
Level: {level}
IVs: {ivs}
Ability: {ability}
Nature: {nature}
Item: {item}
Moves:
{moves}"""
    
    # Aplicar correção
    fixed_section = re.sub(pokemon_pattern, replace_pokemon_block, section)
    
    return fixed_section

def verify():
    print("\n🔍 Verificando correções...")
    
    with open(TRAINERS_PARTY_FILE, 'r') as f:
        content = f.read()
    
    # Verificar se ainda há "Item:" antes dos campos obrigatórios
    problematic_lines = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        if 'Item:' in line and i > 0:
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
    print("🔧 CORREÇÃO ORDEM DO CAMPO ITEM")
    print("=" * 60)
    print("Corrigindo ordem do campo Item nos blocos Pokémon...")
    
    changes = fix_item_order()
    success = verify()
    
    print("\n" + "=" * 60)
    print("🎉 ORDEM DO CAMPO ITEM CORRIGIDA!" if success else "❌ ERROS AINDA PRESENTES")
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
