from characters.abilitytype import AbilityType


class Ability :
    def __init__(self,name, ability_type, max_usage = 100):

        self.name = name
        self.ability_type = ability_type
        self.max_usage = max_usage


    def use(self, user, target):
        self.ability_type.execute(user,target)





















# should be different ability types ie we abilities that add restore health add onto max health add armor make themselves invisible for a turn
# add health that increase over a series of turns instead of just one turn, multiple abilities actually that will increase over a series of turns.
# some abilities should do multiple things ie an ability could reduce health but increase armor or an ability could reduce health but increase max health

# to kind of summarize an ability should be versatile and each ability should have ability types, that then have their own unique attributes for example
# we might have an ability type of heal this ability, will then have several options does it heal over time, does it heal instantly, does it heal but also
# reduce dmg, does it heal and then apply an effect maybe a burn that also does tick dmg, this is the complexity of the program and how we structure abilities
# to effect characters

# also of course an ability is not just for this type heal you could have a heal an attack or a buff, probably more but these 3 examples are good to focus on
# to start with


