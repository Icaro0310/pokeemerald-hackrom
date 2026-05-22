poryOldaleTown_Mart_TM_Seller::
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
