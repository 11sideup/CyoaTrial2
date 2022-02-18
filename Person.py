class Person:
    def __init__(self):
        # List of Possible Hints:
        # 1-4 hints (0-3) index because python starts indexing at 0.
        self.hints = []
        # List of Possible Items:
        self.sword = False
        self.shield = False
        self.armor = False
        self.wand = False
        self.dead = False

    # A method to call when the person dies
    @staticmethod
    def print(message):
        print(message)
        return None

    # A method to call when the person finds an item
    def find_item(self, item):
        # Print to users they found something
        if item[0] in ["a", "e", "i", "o", "u"]
            print(f"You found an {item}!")
        else:
            print(f"You found a {item}!")

        # Assign to person the item
        if item == "sword":
            self.sword = True
        elif item == "shield":
            self.shield = True
        elif item == "armor":
            self.armor = True
        elif item == "wand":
            self.wand = True
        else:
            raise(ValueError(f"Item value {item} is not implemented."))
        return None

    # A method to call when the person finds a hint
    def find_hint(self, hint):
        #self.hints = self.hints + hint
        self.hints.append(hint)
        print(self.hints[self.hints.len()])
        return None

    # A method to call when the person dies
    def die(self,):
        self.dead = True
        return None
