#!/usr/bin/env python3
"""
Script para transformar o Aide do Professor Birch em um reviver de fósseis
no pokeemerald-expansion.

Execute na raiz do projeto: python3 fossil_reviver.py
"""

import json
import shutil
import os

# ============================================================
# CONFIGURAÇÕES
# ============================================================

MAP_DIR = "data/maps/LittlerootTown_ProfessorBirchsLab"
MAP_JSON = f"{MAP_DIR}/map.json"
SCRIPTS_INC = f"{MAP_DIR}/scripts.inc"

# NPC a ser modificado (object_event 1 - Aide/Cientista)
TARGET_OBJECT_ID = 0  # Índice 0 = object_event 1

# Novo nome do script
NEW_SCRIPT_NAME = "LittlerootTown_ProfessorBirchsLab_EventScript_FossilReviver"

# Script antigo a ser substituído
OLD_SCRIPT_NAME = "LittlerootTown_ProfessorBirchsLab_EventScript_Aide"

# ============================================================
# SCRIPT DE REVIVER FÓSSEIS (nível 1)
# ============================================================

FOSSIL_SCRIPT = f'''
{NEW_SCRIPT_NAME}::
    lock
    faceplayer
    msgbox {NEW_SCRIPT_NAME}_Text_Intro, MSGBOX_DEFAULT
    checkitem ITEM_HELIX_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Helix
    checkitem ITEM_DOME_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Dome
    checkitem ITEM_OLD_AMBER
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_OldAmber
    checkitem ITEM_ROOT_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Root
    checkitem ITEM_CLAW_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Claw
    checkitem ITEM_SKULL_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Skull
    checkitem ITEM_ARMOR_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Armor
    checkitem ITEM_COVER_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Cover
    checkitem ITEM_PLUME_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Plume
    checkitem ITEM_JAW_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Jaw
    checkitem ITEM_SAIL_FOSSIL
    compare VAR_RESULT, TRUE
    goto_if_eq {NEW_SCRIPT_NAME}_Sail
    msgbox {NEW_SCRIPT_NAME}_Text_NoFossil, MSGBOX_DEFAULT
    release
    end

{NEW_SCRIPT_NAME}_Helix:
    removeitem ITEM_HELIX_FOSSIL, 1
    givemon SPECIES_OMANYTE, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Dome:
    removeitem ITEM_DOME_FOSSIL, 1
    givemon SPECIES_KABUTO, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_OldAmber:
    removeitem ITEM_OLD_AMBER, 1
    givemon SPECIES_AERODACTYL, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Root:
    removeitem ITEM_ROOT_FOSSIL, 1
    givemon SPECIES_LILEEP, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Claw:
    removeitem ITEM_CLAW_FOSSIL, 1
    givemon SPECIES_ANORITH, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Skull:
    removeitem ITEM_SKULL_FOSSIL, 1
    givemon SPECIES_CRANIDOS, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Armor:
    removeitem ITEM_ARMOR_FOSSIL, 1
    givemon SPECIES_SHIELDON, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Cover:
    removeitem ITEM_COVER_FOSSIL, 1
    givemon SPECIES_TIRTOUGA, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Plume:
    removeitem ITEM_PLUME_FOSSIL, 1
    givemon SPECIES_ARCHEN, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Jaw:
    removeitem ITEM_JAW_FOSSIL, 1
    givemon SPECIES_TYRUNT, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Sail:
    removeitem ITEM_SAIL_FOSSIL, 1
    givemon SPECIES_AMAURA, 1
    goto_if_eq VAR_RESULT, 0, {NEW_SCRIPT_NAME}_Success
    goto {NEW_SCRIPT_NAME}_Fail

{NEW_SCRIPT_NAME}_Success:
    msgbox {NEW_SCRIPT_NAME}_Text_Success, MSGBOX_DEFAULT
    release
    end

{NEW_SCRIPT_NAME}_Fail:
    msgbox {NEW_SCRIPT_NAME}_Text_Fail, MSGBOX_DEFAULT
    release
    end

{NEW_SCRIPT_NAME}_Text_Intro:
    .string "Eu sou o assistente de pesquisa do\\nProfessor Birch.\\pPosso reviver Pokémon de fósseis\\nantigos! Quer tentar?$"

{NEW_SCRIPT_NAME}_Text_Success:
    .string "O fóssil foi revivido com sucesso!\\nEle está no seu party!$"

{NEW_SCRIPT_NAME}_Text_Fail:
    .string "Hmm... parece que você não tem\\nespaço no party. Volte depois!$"

{NEW_SCRIPT_NAME}_Text_NoFossil:
    .string "Você não tem nenhum fóssil comigo\\nagora. Tente encontrar um!$"
'''

# ============================================================
# FUNÇÕES
# ============================================================

def backup_files():
    """Cria backups dos arquivos originais."""
    print("🔄 Criando backups...")
    shutil.copy2(MAP_JSON, f"{MAP_JSON}.backup")
    shutil.copy2(SCRIPTS_INC, f"{SCRIPTS_INC}.backup")
    print("✅ Backups criados!")

def modify_map_json():
    """Modifica o map.json para apontar o NPC para o novo script."""
    print(f"📝 Modificando {MAP_JSON}...")
    
    with open(MAP_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Verifica se o object_event existe
    if 'object_events' not in data or len(data['object_events']) <= TARGET_OBJECT_ID:
        print(f"❌ Erro: object_event {TARGET_OBJECT_ID} não encontrado!")
        return False
    
    old_script = data['object_events'][TARGET_OBJECT_ID].get('script', '')
    print(f"   Script antigo: {old_script}")
    
    # Modifica o script
    data['object_events'][TARGET_OBJECT_ID]['script'] = NEW_SCRIPT_NAME
    print(f"   Novo script: {NEW_SCRIPT_NAME}")
    
    # Salva o arquivo
    with open(MAP_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("✅ map.json modificado!")
    return True

def modify_scripts_inc():
    """Modifica o scripts.inc para adicionar o novo script e remover o antigo."""
    print(f"📝 Modificando {SCRIPTS_INC}...")
    
    with open(SCRIPTS_INC, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verifica se o script antigo existe
    if OLD_SCRIPT_NAME not in content:
        print(f"⚠️ Aviso: Script antigo '{OLD_SCRIPT_NAME}' não encontrado.")
        print("   Pode já ter sido modificado ou ter nome diferente.")
    
    # Remove o script antigo (se existir)
    # Procura pelo label do script antigo até o próximo label ou fim de arquivo
    lines = content.split('\n')
    new_lines = []
    skip_mode = False
    removed_old = False
    
    for line in lines:
        stripped = line.strip()
        
        # Se encontrar o início do script antigo, começa a pular
        if stripped.startswith(f"{OLD_SCRIPT_NAME}::") or stripped.startswith(f"{OLD_SCRIPT_NAME}:"):
            skip_mode = True
            removed_old = True
            print(f"   Removendo script antigo: {OLD_SCRIPT_NAME}")
            continue
        
        # Se encontrar outro label enquanto está pulando, para de pular
        if skip_mode and stripped.endswith('::') and not stripped.startswith(f"{OLD_SCRIPT_NAME}"):
            skip_mode = False
        
        # Se encontrar uma string do script antigo, pula também
        if skip_mode and stripped.startswith('.string'):
            continue
        
        # Se não está pulando, adiciona a linha
        if not skip_mode:
            new_lines.append(line)
    
    # Se não removeu o antigo, apenas adiciona o novo no final
    if not removed_old:
        print("   Script antigo não encontrado, adicionando novo no final...")
    
    # Junta as linhas e adiciona o novo script no final
    new_content = '\n'.join(new_lines).rstrip() + '\n' + FOSSIL_SCRIPT
    
    # Salva o arquivo
    with open(SCRIPTS_INC, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ scripts.inc modificado!")
    return True

def verify_changes():
    """Verifica se as mudanças foram aplicadas corretamente."""
    print("\n🔍 Verificando mudanças...")
    
    # Verifica map.json
    with open(MAP_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    new_script = data['object_events'][TARGET_OBJECT_ID].get('script', '')
    if new_script == NEW_SCRIPT_NAME:
        print(f"✅ map.json: Script correto ({new_script})")
    else:
        print(f"❌ map.json: Script incorreto ({new_script})")
        return False
    
    # Verifica scripts.inc
    with open(SCRIPTS_INC, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if NEW_SCRIPT_NAME in content:
        print(f"✅ scripts.inc: Novo script encontrado")
    else:
        print(f"❌ scripts.inc: Novo script NÃO encontrado")
        return False
    
    # Conta quantos fósseis são suportados
    fossil_count = content.count('checkitem ITEM_') - 1  # -1 por causa do intro
    print(f"✅ {fossil_count} fósseis suportados")
    
    return True

def main():
    """Função principal."""
    print("=" * 60)
    print("🦴 FOSSIL REVIVER - Instalador para pokeemerald-expansion")
    print("=" * 60)
    print()
    
    # Verifica se está na pasta correta
    if not os.path.exists(MAP_JSON):
        print(f"❌ Erro: Arquivo não encontrado: {MAP_JSON}")
        print("   Execute este script na raiz do projeto pokeemerald!")
        return 1
    
    if not os.path.exists(SCRIPTS_INC):
        print(f"❌ Erro: Arquivo não encontrado: {SCRIPTS_INC}")
        return 1
    
    try:
        # Executa as mudanças
        backup_files()
        
        if not modify_map_json():
            return 1
        
        if not modify_scripts_inc():
            return 1
        
        if verify_changes():
            print()
            print("=" * 60)
            print("🎉 SUCESSO! Reviver de fósseis instalado!")
            print("=" * 60)
            print()
            print("📋 Resumo:")
            print(f"   • NPC: Aide/Cientista (object_event 1)")
            print(f"   • Local: Laboratório do Professor Birch, Littleroot Town")
            print(f"   • Script: {NEW_SCRIPT_NAME}")
            print(f"   • Pokémon nível: 1")
            print(f"   • Fósseis suportados: 12")
            print()
            print("⚠️  IMPORTANTE:")
            print("   • Faça 'make clean && make' para recompilar")
            print("   • Inicie um NOVO JOGO para testar")
            print("   • O NPC só aparece após os eventos iniciais do jogo")
            print()
            return 0
        else:
            print()
            print("❌ Verificação falhou! Verifique os arquivos manualmente.")
            return 1
            
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("   Restaurando backups...")
        shutil.copy2(f"{MAP_JSON}.backup", MAP_JSON)
        shutil.copy2(f"{SCRIPTS_INC}.backup", SCRIPTS_INC)
        print("   Backups restaurados!")
        return 1

if __name__ == "__main__":
    exit(main())
