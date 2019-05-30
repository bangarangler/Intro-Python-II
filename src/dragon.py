class Dragon:
    def __init__(self, name, health, source_mana, current_room):
        self.name = name
        self.health = int(health)
        self.source_mana = int(source_mana)
        self.current_room = current_room

    def fire_shot(self):
        print("Fires super hot fury!")
