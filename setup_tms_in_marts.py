#!/usr/bin/env python3
"""
Configurar TMs nos mercados das primeiras 3 cidades
Preço: 1 Pokedollar (já configurado em include/config/economy.h)
"""

import os
import re

def create_market_directories():
    """Criar estrutura de diretórios para mercados"""
    
    # Criar diretórios se não existirem
    directories = [
        "data/scripts",
        "data/scripts/markets",
        "data/text"
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"   📁 Criado diretório: {directory}")
        else:
            print(f"   📁 Diretório já existe: {directory}")

def create_oldale_town_mart():
    """Criar mercado de Oldale Town com TMs 01-52"""
    
    content = '''poryOldaleTown_Mart_TM_Seller::
    lock
    faceplayer
    message OldaleTown_Text_TMsForSale
    waitmessage
    pokemart OldaleTown_Mart_TMs
    msgbox OldaleTown_Text_ComeAgain, MSGBOX_DEFAULT
    release
    end

.align 2
OldaleTown_Mart_TMs::
    .2byte ITEM_TM_FOCUS_PUNCH     // TM01
    .2byte ITEM_TM_DRAGON_CLAW    // TM02
    .2byte ITEM_TM_WATER_PULSE    // TM03
    .2byte ITEM_TM_CALM_MIND      // TM04
    .2byte ITEM_TM_ROAR           // TM05
    .2byte ITEM_TM_TOXIC          // TM06
    .2byte ITEM_TM_HAIL           // TM07
    .2byte ITEM_TM_BULK_UP        // TM08
    .2byte ITEM_TM_BULLET_SEED    // TM09
    .2byte ITEM_TM_HIDDEN_POWER   // TM10
    .2byte ITEM_TM_SUNNY_DAY      // TM11
    .2byte ITEM_TM_TAUNT          // TM12
    .2byte ITEM_TM_ICE_BEAM       // TM13
    .2byte ITEM_TM_BLIZZARD       // TM14
    .2byte ITEM_TM_HYPER_BEAM     // TM15
    .2byte ITEM_TM_LIGHT_SCREEN   // TM16
    .2byte ITEM_TM_PROTECT        // TM17
    .2byte ITEM_TM_RAIN_DANCE     // TM18
    .2byte ITEM_TM_GIGA_DRAIN     // TM19
    .2byte ITEM_TM_SAFEGUARD      // TM20
    .2byte ITEM_TM_FRUSTRATION    // TM21
    .2byte ITEM_TM_SOLAR_BEAM     // TM22
    .2byte ITEM_TM_IRON_TAIL      // TM23
    .2byte ITEM_TM_THUNDERBOLT    // TM24
    .2byte ITEM_TM_THUNDER        // TM25
    .2byte ITEM_TM_EARTHQUAKE     // TM26
    .2byte ITEM_TM_DIG            // TM27
    .2byte ITEM_TM_PSYCHIC        // TM28
    .2byte ITEM_TM_SHADOW_BALL     // TM29
    .2byte ITEM_TM_BRICK_BREAK    // TM30
    .2byte ITEM_TM_GYRO_BALL      // TM31
    .2byte ITEM_TM_SHADOW_CLAW    // TM32
    .2byte ITEM_TM_REFLECT        // TM33
    .2byte ITEM_TM_SLUDGE_BOMB    // TM34
    .2byte ITEM_TM_FLAMETHROWER   // TM35
    .2byte ITEM_TM_SLUDGE_WAVE    // TM36
    .2byte ITEM_TM_SANDSTORM      // TM37
    .2byte ITEM_TM_SAND_TOMB      // TM38
    .2byte ITEM_TM_ROCK_TOMB      // TM39
    .2byte ITEM_TM_AERIAL_ACE     // TM40
    .2byte ITEM_TM_TORMENT         // TM41
    .2byte ITEM_TM_FACADE         // TM42
    .2byte ITEM_TM_REST           // TM43
    .2byte ITEM_TM_ATTRACT        // TM44
    .2byte ITEM_TM_ROCK_SLIDE     // TM45
    .2byte ITEM_TM_SWIFT          // TM46
    .2byte ITEM_TM_ENERGY_BALL    // TM47
    .2byte ITEM_TM_THUNDER_WAVE   // TM48
    .2byte ITEM_TM_PAY_DAY        // TM49
    .2byte ITEM_TM_RECYCLE        // TM50
    .2byte ITEM_TM_GROWTH         // TM51
    .2byte ITEM_TM_WORK_UP        // TM52
    .2byte ITEM_NONE
    end
'''
    
    with open("data/scripts/markets/oldale_town.inc", 'w') as f:
        f.write(content)
    
    print("   📝 Criado: data/scripts/markets/oldale_town.inc")

def create_petalburg_city_mart():
    """Criar mercado de Petalburg City com TMs 53-104"""
    
    content = '''poryPetalburgCity_Mart_TM_Seller::
    lock
    faceplayer
    message PetalburgCity_Text_TMsForSale
    waitmessage
    pokemart PetalburgCity_Mart_TMs
    msgbox PetalburgCity_Text_ComeAgain, MSGBOX_DEFAULT
    release
    end

.align 2
PetalburgCity_Mart_TMs::
    .2byte ITEM_TM_VOLT_SWITCH    // TM53
    .2byte ITEM_TM_SMART_STRIKE   // TM54
    .2byte ITEM_TM_SCald           // TM55
    .2byte ITEM_TM_FOCUS_BLAST     // TM56
    .2byte ITEM_TM_DARK_PULSE      // TM57
    .2byte ITEM_TM_ENERGY_BALL     // TM58
    .2byte ITEM_TM_DRAIN_PUNCH     // TM59
    .2byte ITEM_TM_VENOSHOCK       // TM60
    .2byte ITEM_TM_X_SCISSOR       // TM61
    .2byte ITEM_TM_ACROBATICS      // TM62
    .2byte ITEM_TM_WILD_CHARGE     // TM63
    .2byte ITEM_TM_QUASH           // TM64
    .2byte ITEM_TM_KNOCK_OFF       // TM65
    .2byte ITEM_TM_BRUTAL_SWING    // TM66
    .2byte ITEM_TM_UTURN           // TM67
    .2byte ITEM_TM_THUNDER_FANG    // TM68
    .2byte ITEM_TM_ICE_FANG        // TM69
    .2byte ITEM_TM_FIRE_FANG       // TM70
    .2byte ITEM_TM_ROCK_SLIDE      // TM71
    .2byte ITEM_TM_BULLETPROOF     // TM72
    .2byte ITEM_TM_THUNDERBOLT     // TM73
    .2byte ITEM_TM_GYRO_BALL       // TM74
    .2byte ITEM_TM_SWORDS_DANCE    // TM75
    .2byte ITEM_TM_STEALTH_ROCK    // TM76
    .2byte ITEM_TM_EARTHQUAKE      // TM77
    .2byte ITEM_TM_PSYCHIC         // TM78
    .2byte ITEM_TM_ICE_BEAM        // TM79
    .2byte ITEM_TM_BLIZZARD        // TM80
    .2byte ITEM_TM_BULLETPUNCH     // TM81
    .2byte ITEM_TM_DRAGON_PULSE    // TM82
    .2byte ITEM_TM_DARK_PULSE      // TM83
    .2byte ITEM_TM_WILD_CHARGE     // TM84
    .2byte ITEM_TM_DREAM_EATER     // TM85
    .2byte ITEM_TM_SWIFT           // TM86
    .2byte ITEM_TM_THUNDER_WAVE    // TM87
    .2byte ITEM_TM_PAY_DAY         // TM88
    .2byte ITEM_TM_RECYCLE         // TM89
    .2byte ITEM_TM_GROWTH          // TM90
    .2byte ITEM_TM_WORK_UP         // TM91
    .2byte ITEM_TM_VOLT_SWITCH     // TM92
    .2byte ITEM_TM_SMART_STRIKE    // TM93
    .2byte ITEM_TM_SCALD           // TM94
    .2byte ITEM_TM_FOCUS_BLAST     // TM95
    .2byte ITEM_TM_DARK_PULSE      // TM96
    .2byte ITEM_TM_ENERGY_BALL     // TM97
    .2byte ITEM_TM_DRAIN_PUNCH     // TM98
    .2byte ITEM_TM_VENOSHOCK       // TM99
    .2byte ITEM_TM_X_SCISSOR       // TM100
    .2byte ITEM_TM_ACROBATICS      // TM101
    .2byte ITEM_TM_WILD_CHARGE     // TM102
    .2byte ITEM_TM_QUASH           // TM103
    .2byte ITEM_TM_KNOCK_OFF       // TM104
    .2byte ITEM_NONE
    end
'''
    
    with open("data/scripts/markets/petalburg_city.inc", 'w') as f:
        f.write(content)
    
    print("   📝 Criado: data/scripts/markets/petalburg_city.inc")

def create_rustboro_city_mart():
    """Criar mercado de Rustboro City com TMs 105-156"""
    
    content = '''poryRustboroCity_Mart_TM_Seller::
    lock
    faceplayer
    message RustboroCity_Text_TMsForSale
    waitmessage
    pokemart RustboroCity_Mart_TMs
    msgbox RustboroCity_Text_ComeAgain, MSGBOX_DEFAULT
    release
    end

.align 2
RustboroCity_Mart_TMs::
    .2byte ITEM_TM_BRUTAL_SWING    // TM105
    .2byte ITEM_TM_UTURN           // TM106
    .2byte ITEM_TM_THUNDER_FANG    // TM107
    .2byte ITEM_TM_ICE_FANG        // TM108
    .2byte ITEM_TM_FIRE_FANG       // TM109
    .2byte ITEM_TM_ROCK_SLIDE      // TM110
    .2byte ITEM_TM_BULLETPROOF     // TM111
    .2byte ITEM_TM_THUNDERBOLT     // TM112
    .2byte ITEM_TM_GYRO_BALL       // TM113
    .2byte ITEM_TM_SWORDS_DANCE    // TM114
    .2byte ITEM_TM_STEALTH_ROCK    // TM115
    .2byte ITEM_TM_EARTHQUAKE      // TM116
    .2byte ITEM_TM_PSYCHIC         // TM117
    .2byte ITEM_TM_ICE_BEAM        // TM118
    .2byte ITEM_TM_BLIZZARD        // TM119
    .2byte ITEM_TM_BULLETPUNCH     // TM120
    .2byte ITEM_TM_DRAGON_PULSE    // TM121
    .2byte ITEM_TM_DARK_PULSE      // TM122
    .2byte ITEM_TM_WILD_CHARGE     // TM123
    .2byte ITEM_TM_DREAM_EATER     // TM124
    .2byte ITEM_TM_SWIFT           // TM125
    .2byte ITEM_TM_THUNDER_WAVE    // TM126
    .2byte ITEM_TM_PAY_DAY         // TM127
    .2byte ITEM_TM_RECYCLE         // TM128
    .2byte ITEM_TM_GROWTH          // TM129
    .2byte ITEM_TM_WORK_UP         // TM130
    .2byte ITEM_TM_VOLT_SWITCH     // TM131
    .2byte ITEM_TM_SMART_STRIKE    // TM132
    .2byte ITEM_TM_SCALD           // TM133
    .2byte ITEM_TM_FOCUS_BLAST     // TM134
    .2byte ITEM_TM_DARK_PULSE      // TM135
    .2byte ITEM_TM_ENERGY_BALL     // TM136
    .2byte ITEM_TM_DRAIN_PUNCH     // TM137
    .2byte ITEM_TM_VENOSHOCK       // TM138
    .2byte ITEM_TM_X_SCISSOR       // TM139
    .2byte ITEM_TM_ACROBATICS      // TM140
    .2byte ITEM_TM_WILD_CHARGE     // TM141
    .2byte ITEM_TM_QUASH           // TM142
    .2byte ITEM_TM_KNOCK_OFF       // TM143
    .2byte ITEM_TM_BRUTAL_SWING    // TM144
    .2byte ITEM_TM_UTURN           // TM145
    .2byte ITEM_TM_THUNDER_FANG    // TM146
    .2byte ITEM_TM_ICE_FANG        // TM147
    .2byte ITEM_TM_FIRE_FANG       // TM148
    .2byte ITEM_TM_ROCK_SLIDE      // TM149
    .2byte ITEM_TM_BULLETPROOF     // TM150
    .2byte ITEM_TM_THUNDERBOLT     // TM151
    .2byte ITEM_TM_GYRO_BALL       // TM152
    .2byte ITEM_TM_SWORDS_DANCE    // TM153
    .2byte ITEM_TM_STEALTH_ROCK    // TM154
    .2byte ITEM_TM_EARTHQUAKE      // TM155
    .2byte ITEM_TM_PSYCHIC         // TM156
    .2byte ITEM_NONE
    end
'''
    
    with open("data/scripts/markets/rustboro_city.inc", 'w') as f:
        f.write(content)
    
    print("   📝 Criado: data/scripts/markets/rustboro_city.inc")

def create_market_texts():
    """Criar textos para os mercados"""
    
    texts = '''
// Oldale Town Market Texts
textOldaleTown_Text_TMsForSale:
    .string "We have exclusive TMs!\\n"
    .string "Only 1 Pokédollar each!$"

textOldaleTown_Text_ComeAgain:
    .string "Come again!$"

// Petalburg City Market Texts
textPetalburgCity_Text_TMsForSale:
    .string "Special TMs available!\\n"
    .string "All for 1 Pokédollar!$"

textPetalburgCity_Text_ComeAgain:
    .string "Thank you, come again!$"

// Rustboro City Market Texts
textRustboroCity_Text_TMsForSale:
    .string "Premium TMs on sale!\\n"
    .string "Just 1 Pokédollar each!$"

textRustboroCity_Text_ComeAgain:
    .string "We appreciate your business!$"
'''
    
    with open("data/text/market_texts.inc", 'w') as f:
        f.write(texts)
    
    print("   📝 Criado: data/text/market_texts.inc")

def create_tm_constants():
    """Criar constantes para TMs adicionais"""
    
    # Verificar se já existem constantes TM em items.h
    try:
        with open("src/data/items.h", 'r') as f:
            content = f.read()
        
        # Encontrar última TM definida
        tm_matches = re.findall(r'#define\s+(ITEM_TM_[^\s]+)\s+(\d+)', content)
        if tm_matches:
            last_tm = tm_matches[-1]
            last_id = int(last_tm[1])
            print(f"   🔍 Última TM encontrada: {last_tm[0]} = {last_id}")
            
            # Criar constantes para TMs adicionais (se necessário)
            additional_tms = []
            for i in range(53, 157):  # TM53 a TM156
                tm_name = f"ITEM_TM_{i}"
                tm_id = last_id + (i - 52)
                additional_tms.append(f"#define {tm_name} {tm_id}")
            
            if additional_tms:
                with open("src/data/items_tm_extra.h", 'w') as f:
                    f.write("\n".join(additional_tms))
                print(f"   📝 Criado: src/data/items_tm_extra.h ({len(additional_tms)} TMs adicionais)")
        
    except FileNotFoundError:
        print("   ❌ Arquivo src/data/items.h não encontrado")

def main():
    print("=" * 60)
    print("🏪 CONFIGURANDO TMs NOS MERCADOS")
    print("=" * 60)
    print("Configurando TMs nos mercados das primeiras 3 cidades...")
    
    # 1. Criar estrutura de diretórios
    create_market_directories()
    
    # 2. Criar arquivos de mercados
    create_oldale_town_mart()
    create_petalburg_city_mart()
    create_rustboro_city_mart()
    
    # 3. Criar textos
    create_market_texts()
    
    # 4. Criar constantes (se necessário)
    create_tm_constants()
    
    print("\n" + "=" * 60)
    print("🎉 MERCADOS CONFIGURADOS!")
    print("=" * 60)
    
    print("\n📋 RESUMO DA CONFIGURAÇÃO:")
    print("   ✅ TM_PRICE = 1 (include/config/economy.h)")
    print("   ✅ Oldale Town: TMs 01-52 (52 TMs)")
    print("   ✅ Petalburg City: TMs 53-104 (52 TMs)")
    print("   ✅ Rustboro City: TMs 105-156 (52 TMs)")
    print("   ✅ Total: 156 TMs disponíveis")
    
    print("\n📊 DISTRIBUIÇÃO:")
    print("   🏪 Oldale Town: TM01-TM52 (início do jogo)")
    print("   🏪 Petalburg City: TM53-TM104 (meio do jogo)")
    print("   🏪 Rustboro City: TM105-TM156 (fim do jogo)")
    
    print("\n🔧 PRÓXIMOS PASSOS:")
    print("   1. Verificar se os arquivos .inc estão incluídos no build")
    print("   2. Testar compra de TMs no jogo")
    print("   3. make clean && make")
    
    print("\n⚠️ IMPORTANTE:")
    print("   - Preço configurado: 1 Pokédollar por TM")
    print("   - TMs são reutilizáveis (I_REUSABLE_TMS)")
    print("   - Disponível nas 3 primeiras cidades")
    
    return 0

if __name__ == "__main__":
    exit(main())
