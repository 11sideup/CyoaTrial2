class Person:
    def __init__(self, hp, attack, defense, magic, name):
        if hp <= 0:
            raise ValueError(f"hp attribute must be > 0.")
        self._hp = hp
        self._attack = attack
        self._defense = defense
        self._magic = magic
        self._name = name

    @property
    def hp(self):
        '''
        Person.hp is a property
        This is the getter method
        '''
        return self._hp

    @hp.setter
    def hp(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        self._hp = value
        if value <= 0:
            self.die()

    @property
    def attack(self):
        '''
        Person.attack is a property
        This is the getter method
        '''
        return self._attack

    @attack.setter
    def attack(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value < 0:
            raise ValueError("Must be >= 0")
        self._attack = value

    @property
    def defense(self):
        '''
        Person.defense is a property
        This is the getter method
        '''
        return self._defense

    @defense.setter
    def defense(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value < 0:
            raise ValueError("Must be >= 0")
        self._defense = value

    @property
    def magic(self):
        '''
        Person.magic is a property
        This is the getter method
        '''
        return self._magic

    @magic.setter
    def magic(self, value):
        """
        This is the setter method
        where I can check it's not assigned a value < 0
        """
        if value < 0:
            raise ValueError("Must be >= 0")
        self._magic = value

    @property
    # Since there is no setter, you can't change the name value.
    def name(self):
        return self._name

    def die(self):
        print(f"{self.name} has died...")
        return


class NPC(Person):
    def __init__(self, hp, attack, defense, magic, name, drops):
        super().__init__(hp=hp, attack=attack, defense=defense, magic=magic, name = name)
        self._drops = drops

    @property
    def drops(self):
        return self._drops

    def die(self):
        if self.hp <= 0:
            print(f"{self.name} has died!!! {self.name} dropped {self.drops}.")
            return self.drops
        else:
            raise(ValueError(f"{self.name} tried to die, but has hp {self.hp}"))


class PC(Person):
    def __init__(self, hp, attack, defense, magic, name, inventory):
        super().__init__(hp=hp, attack=attack, defense=defense, magic=magic, name=name)
        self._inventory = [inventory, ]

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        """
        This is the setter method
        where we append the new item to the inventory
        """
        self._inventory.append(value)


    def die(self):
        if self.hp == 0:
            print(f"{self.name} has died!!! You've lost.")
            return
        else:
            raise(ValueError(f"{self.name} tried to die, but has hp {self.hp}"))

    # A method to call when the person finds an item
    def find_item(self, item):
        # Print to users they found something
        if item[0] in ["a", "e", "i", "o", "u"]:
            print(f"{self.name} found an {item}!")
        else:
            print(f"{self.name} found a {item}!")
        # Add item to inventory list
        self.inventory = item
