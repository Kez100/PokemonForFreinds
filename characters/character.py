class Character:
    def __init__(self, name, health,armor,evasion,abilities,dialogue):

        self.name = name

        self.health = health
        self.max_health = health
        self.armor = armor
        self.evasion = evasion
        self.abilities = abilities

        self.dialogue = dialogue
        self.status_effects = []

    def heal(self, amount):

        self.health = min(amount + self.health, self.max_health)
        # add print that says amount of health healed

    def increaseStat(self,stat,amount):

        setattr(self, stat, getattr(self, stat) + amount)

    def decreaseStat(self,stat,amount):

        setattr(self, stat, getattr(self, stat) - amount)

    #def takeDmg


    def displayStats(self):

        print(f"--- {self.name}'s Stats ---")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Armor: {self.armor}")
        print(f"Evasion: {self.evasion}")
        print(f"Abilities: {[ability.name for ability in self.abilities]}")
        print(f"Status Effects: {self.status_effects if self.status_effects else 'None'}")