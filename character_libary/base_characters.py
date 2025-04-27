from characters.dialogue import Dialogue
from characters.character import Character
from characters.ability import Ability
from characters.abilitytype import AbilityType


# Creation of Henry

henrys_dialogue = Dialogue(
    "My name is Henry West, I got a first btw",
    "Should of paid my mortgage off",
    "it appears i have got the better of you",
    "Take that you twit",
    "Oh well...")

sings_in_welsh = Ability("Sings In Welsh", AbilityType(heal = True, buff = True, heal_amount=100, buff_stat="armor"))
sips_one_slither_of_rum =Ability("Sips one slither of rum", AbilityType(heal=True, heal_amount=3))
puts_on_clam_bopers = Ability(" Puts on clam bopers", AbilityType(damage= True, self_damage=True, damage_amount=45, self_damage_amount= 20))
talks_about_the_political_state_of_the_country = Ability("talks about the political state of the country", AbilityType(debuff= "armor", debuff_amount=10))


henry_west = Character("Henry West",225,33,10,[sings_in_welsh,sips_one_slither_of_rum,puts_on_clam_bopers,
                                               talks_about_the_political_state_of_the_country], henrys_dialogue)



#Creation of Reese

reeses_dialogue = Dialogue()

pulling_up_in_the_landrover = Ability("pulling up in the landrover", AbilityType(damage = True, damage_amount=150))
cooking_up_some_spag_bol = Ability("Cooking up some spag bol", AbilityType(heal=True, heal_amount=75))

reese_rainey = Character("Reese Rainey", 250,45,20,[pulling_up_in_the_landrover, cooking_up_some_spag_bol], reeses_dialogue)


