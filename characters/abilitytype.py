from characters import character
from characters import ability

class AbilityType:
    def __init__(self, heal= False,damage = False,buff= False, over_time = False,
                 self_damage = False, debuff = False,self_damage_amount = 0,heal_amount=0, damage_amount=0, buff_stat=None, buff_amount=0, debuff_amount = 0):

        # please for the love of god kez refactor this.

        self.heal = heal
        self.damage = damage
        self.buff = buff
        self.over_time = over_time
        self.self_damage = self_damage
        self.debuff = debuff

        self.heal_amount = heal_amount
        self.damage_amount = damage_amount
        self.buff_stat = buff_stat
        self.buff_amount = buff_amount
        self.debuff_amount = debuff_amount
        self.self_damage_amount = self_damage_amount

    def execute(self, user, target):
        if self.heal:
            user.heal(self.heal_amount)
        if self.self_damage:
            user.health -= self.self_damage_amount
        if self.buff:
            user.increaseStat(self.buff_stat, self.buff_amount)
        if self.debuff:
            user.decreaseStat(self.debuff, self.debuff_amount)

        if self.damage:
            target.health -= self.damage_amount
            # call function here that does calculation for how much damage is taken and if its evaded





    #def calculate_dmg(self):




















# now ideally we would create a class that can accept different types ie we create the ability type class and then we can constantly add on different abilites to the game
# like we add on abilities but i guess in order to do that we are i don't know adding in our own logic for what each ability does so we create afunction in ability type that takes that
# logic and works with it against the character, u dunno