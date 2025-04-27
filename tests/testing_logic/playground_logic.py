from character_libary import base_characters
from character_libary.base_characters import henry_west
from character_libary.base_characters import reese_rainey

#Display original stats of both characters
henry_west.displayStats()
reese_rainey.displayStats()

print("\n" * 3)

#initiate fight

# Reese attacks Henry

reese_rainey.abilities[0].use(reese_rainey,henry_west)

# Henry's health drops
henry_west.displayStats()

# Henry uses a healing ability
henry_west.abilities[0].use(henry_west,reese_rainey)

print("\n * 3")

# Henry's health increases
henry_west.displayStats()






