#!/usr/bin/env python3
"""
Inserir TMs TM01-TM100 nas 3 primeiras PokéMarts
E mudar preço de TODOS os TMs para 1 Pokédollar
"""

import re
import shutil

MARTS = [
    "data/maps/OldaleTown_Mart/scripts.inc",
    "data/maps/PetalburgCity_Mart/scripts.inc",
    "data/maps/RustboroCity_Mart/scripts.inc",
]

ITEMS_H_FILE = "src/data/items.h"

TM_GROUPS = [
    list(range(1, 34)),    # Oldale: TM01-TM33
    list(range(34, 67)),   # Petalburg: TM34-TM66
    list(range(67, 101)),  # Rustboro: TM67-TM100
]

def backup():
    for mart in MARTS:
        shutil.copy2(mart, f"{mart}.backup")
    shutil.copy2(ITEMS_H_FILE, f"{ITEMS_H_FILE}.backup")
    print("✅ Backups criados")

def add_tms_to_mart(mart_file, tm_numbers):
    with open(mart_file, 'r') as f:
        content = f.read()
    
    # Encontra pokemartlistend e adiciona TMs antes dele
    pattern = r'(\s*pokemartlistend)'
    match = re.search(pattern, content)
    
    if not match:
        print(f"❌ Padrão não encontrado em {mart_file}")
        return False
    
    tm_lines = [f"    .2byte ITEM_TM{tm:02d}" for tm in tm_numbers]
    old_text = match.group(0)
    new_text = "\n".join(tm_lines) + "\n" + old_text
    
    content = content.replace(old_text, new_text, 1)
    
    with open(mart_file, 'w') as f:
        f.write(content)
    
    city = mart_file.split('/')[-2]
    print(f"✅ {len(tm_numbers)} TMs adicionados a {city}")
    return True

def change_tm_prices():
    with open(ITEMS_H_FILE, 'r') as f:
        content = f.read()
    
    print("\n💰 Mudando preços dos TMs para 1$...")
    
    # Substitui .price = 3000 (ou qualquer número) por .price = 1
    # Apenas dentro das seções ITEM_TMXX
    lines = content.split('\n')
    in_tm = False
    changed = 0
    
    for i, line in enumerate(lines):
        # Detecta início de um TM
        if re.match(r'\s*\[ITEM_TM\d+\]', line):
            in_tm = True
        
        # Substitui preço se estiver dentro de um TM
        if in_tm and '.price' in line:
            new_line = re.sub(r'(\.price\s*=\s*)\d+', r'\g<1>1', line)
            if new_line != line:
                lines[i] = new_line
                changed += 1
        
        # Detecta fim da definição do item
        if in_tm and line.strip() == '},':
            in_tm = False
    
    content = '\n'.join(lines)
    
    with open(ITEMS_H_FILE, 'w') as f:
        f.write(content)
    
    print(f"✅ Preço de {changed} TMs alterado para 1$")
    return True

def verify():
    print("\n🔍 Verificando...")
    
    # Verifica lojas
    for mart in MARTS:
        with open(mart, 'r') as f:
            content = f.read()
        tm_count = content.count('ITEM_TM')
        city = mart.split('/')[-2]
        print(f"   {city}: {tm_count} TMs")
    
    # Verifica preços
    with open(ITEMS_H_FILE, 'r') as f:
        content = f.read()
    
    # Conta TMs com preço 1
    cheap_tms = 0
    tm_sections = content.split('[ITEM_TM')
    for section in tm_sections[1:]:
        if '.price = 1' in section.split('},')[0]:
            cheap_tms += 1
    
    print(f"   TMs com preço 1$: {cheap_tms}")

def main():
    print("=" * 60)
    print("🛒 TM MART + PRICE CHANGER")
    print("=" * 60)
    
    backup()
    
    # Adiciona TMs às lojas
    for mart, tms in zip(MARTS, TM_GROUPS):
        if not add_tms_to_mart(mart, tms):
            return 1
    
    # Muda preços
    change_tm_prices()
    
    verify()
    
    print("\n" + "=" * 60)
    print("🎉 TMs nas lojas + Preço 1$!")
    print("=" * 60)
    print("\nDistribuição:")
    print("   Oldale Town:    TM01-TM33")
    print("   Petalburg City: TM34-TM66")
    print("   Rustboro City:  TM67-TM100")
    print("\nPróximos passos:")
    print("   make clean && make")
    print("   New Game para testar")
    
    return 0

if __name__ == "__main__":
    exit(main())
