OldaleTown_Mart_MapScripts::
	.byte 0

OldaleTown_Mart_EventScript_Clerk::
	lock
	faceplayer
	message gText_HowMayIServeYou
	waitmessage
	goto_if_set FLAG_ADVENTURE_STARTED, OldaleTown_Mart_ExpandedItems
	pokemart OldaleTown_Mart_Pokemart_Basic
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
OldaleTown_Mart_Pokemart_Basic:
	.2byte ITEM_POTION
	.2byte ITEM_ANTIDOTE
	.2byte ITEM_PARALYZE_HEAL
	.2byte ITEM_AWAKENING
    .2byte ITEM_TM01
    .2byte ITEM_TM02
    .2byte ITEM_TM03
    .2byte ITEM_TM04
    .2byte ITEM_TM05
    .2byte ITEM_TM06
    .2byte ITEM_TM07
    .2byte ITEM_TM08
    .2byte ITEM_TM09
    .2byte ITEM_TM10
    .2byte ITEM_TM11
    .2byte ITEM_TM12
    .2byte ITEM_TM13
    .2byte ITEM_TM14
    .2byte ITEM_TM15
    .2byte ITEM_TM16
    .2byte ITEM_TM17
    .2byte ITEM_TM18
    .2byte ITEM_TM19
    .2byte ITEM_TM20
    .2byte ITEM_TM21
    .2byte ITEM_TM22
    .2byte ITEM_TM23
    .2byte ITEM_TM24
    .2byte ITEM_TM25
    .2byte ITEM_TM26
    .2byte ITEM_TM27
    .2byte ITEM_TM28
    .2byte ITEM_TM29
    .2byte ITEM_TM30
    .2byte ITEM_TM31
    .2byte ITEM_TM32
    .2byte ITEM_TM33

	pokemartlistend

OldaleTown_Mart_ExpandedItems::
	pokemart OldaleTown_Mart_Pokemart_Expanded
	msgbox gText_PleaseComeAgain, MSGBOX_DEFAULT
	release
	end

	.align 2
OldaleTown_Mart_Pokemart_Expanded:
	.2byte ITEM_POKE_BALL
	.2byte ITEM_POTION
	.2byte ITEM_ANTIDOTE
	.2byte ITEM_PARALYZE_HEAL
	.2byte ITEM_AWAKENING
	pokemartlistend

OldaleTown_Mart_EventScript_Woman::
	lock
	faceplayer
	goto_if_set FLAG_ADVENTURE_STARTED, OldaleTown_Mart_EventScript_PokeBallsInStock
	msgbox OldaleTown_Mart_Text_PokeBallsAreSoldOut, MSGBOX_DEFAULT
	release
	end

OldaleTown_Mart_EventScript_PokeBallsInStock::
	msgbox OldaleTown_Mart_Text_ImGoingToBuyPokeBalls, MSGBOX_DEFAULT
	release
	end

OldaleTown_Mart_EventScript_Boy::
	msgbox OldaleTown_Mart_Text_RestoreHPWithPotion, MSGBOX_NPC
	end

OldaleTown_Mart_Text_PokeBallsAreSoldOut:
	.string "The clerk says they're all sold out.\n"
	.string "I can't buy any POKé BALLS.$"

OldaleTown_Mart_Text_ImGoingToBuyPokeBalls:
	.string "I'm going to buy a bunch of POKé BALLS\n"
	.string "and catch a bunch of POKéMON!$"

OldaleTown_Mart_Text_RestoreHPWithPotion:
	.string "If a POKéMON gets hurt and loses its HP\n"
	.string "and faints, it won't be able to battle.\p"
	.string "To prevent your POKéMON from fainting,\n"
	.string "restore its HP with a POTION.$"

