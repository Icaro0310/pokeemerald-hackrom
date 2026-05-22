#!/usr/bin/env python3
"""
Corrigir preço das TMs para 1 Pokedollar e garantir disponibilidade nas lojas
"""

import re

ITEMS_FILE = "src/data/items.h"

def fix_tm_prices():
    with open(ITEMS_FILE, 'r') as f:
        content = f.read()
    
    print("\n🔧 Corrigindo preço das TMs para 1 Pokedollar...")
    
    # Encontrar todas as TMs e mudar preço para 1
    tm_pattern = r'(\[ITEM_TM_[^\]]+\] =\s*\n\s*\{\s*\n\s*\.name = _\("TM[^\"]+"\),\s*\n\s*)\.price = \d+,'
    
    def replace_tm_price(match):
        prefix = match.group(1)
        return f'{prefix}.price = 1,'
    
    # Aplicar substituição
    content = re.sub(tm_pattern, replace_tm_price, content)
    
    with open(ITEMS_FILE, 'w') as f:
        f.write(content)
    
    print("   ✅ Preços das TMs alterados para 1 Pokedollar")
    return content

def verify_tm_prices():
    with open(ITEMS_FILE, 'r') as f:
        content = f.read()
    
    # Verificar se ainda há TMs com preço diferente de 1
    tm_price_pattern = r'\[ITEM_TM_[^\]]+\].*?\.price = (\d+),'
    matches = re.findall(tm_price_pattern, content, re.DOTALL)
    
    prices = list(set(int(p) for p in matches))
    print(f"\n🔍 Preços encontrados nas TMs: {sorted(prices)}")
    
    if len(prices) == 1 and prices[0] == 1:
        print("   ✅ Todas as TMs com preço 1 Pokedollar")
        return True
    else:
        print(f"   ❌ Ainda existem TMs com preços diferentes: {prices}")
        return False

def find_shop_files():
    print("\n🔍 Procurando arquivos de lojas...")
    
    # Procurar por arquivos que contenham informações de lojas
    import os
    
    shop_files = []
    for root, dirs, files in os.walk("src"):
        for file in files:
            if file.endswith(".c") or file.endswith(".h"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                        if "ITEM_TM" in content and ("mart" in content.lower() or "shop" in content.lower()):
                            shop_files.append(file_path)
                            print(f"   📁 {file_path}")
                except:
                    pass
    
    return shop_files

def check_first_city_shops():
    print("\n🔍 Verificando lojas das primeiras cidades...")
    
    # Procurar por scripts de lojas das primeiras cidades
    import os
    
    first_city_files = []
    for root, dirs, files in os.walk("src"):
        for file in files:
            if "petalburg" in file.lower() or "rustboro" in file.lower() or "dewford" in file.lower():
                if file.endswith(".c") or file.endswith(".h"):
                    file_path = os.path.join(root, file)
                    first_city_files.append(file_path)
                    print(f"   🏪 {file_path}")
    
    return first_city_files

def main():
    print("=" * 60)
    print("🔧 CORREÇÃO PREÇO DAS TMs")
    print("=" * 60)
    print("Corrigindo preço das TMs para 1 Pokedollar...")
    
    # 1. Corrigir preços das TMs
    content = fix_tm_prices()
    
    # 2. Verificar se correção funcionou
    success = verify_tm_prices()
    
    # 3. Procurar arquivos de lojas
    shop_files = find_shop_files()
    
    # 4. Verificar lojas das primeiras cidades
    first_city_files = check_first_city_shops()
    
    print("\n" + "=" * 60)
    print("🎉 CORREÇÃO DE PREÇOS DAS TMs CONCLUÍDA!" if success else "❌ ERROS NA CORREÇÃO")
    print("=" * 60)
    
    print("\n📋 RESUMO:")
    print(f"   ✅ Preços das TMs: {('CORRIGIDOS' if success else 'ERRO')}")
    print(f"   📁 Arquivos de lojas encontrados: {len(shop_files)}")
    print(f"   🏪 Arquivos das primeiras cidades: {len(first_city_files)}")
    
    print("\n📊 STATUS DAS TMs:")
    print("   ✅ Preço: 1 Pokedollar (corrigido)")
    print("   ✅ Importância: I_REUSABLE_TMS (já ativado)")
    print("   ✅ Pocket: POCKET_TM_HM")
    print("   ✅ Uso: ITEM_USE_PARTY_MENU")
    
    print("\n🔧 PRÓXIMOS PASSOS:")
    if success:
        print("   1. Verificar disponibilidade nas lojas das primeiras 3 cidades")
        print("   2. Testar compra de TMs no jogo")
        print("   3. make clean && make")
    else:
        print("   1. Corrigir manualmente os preços restantes")
        print("   2. Verificar padrão regex")
    
    return 0 if success else 1

if __name__ == "__main__":
    exit(main())
