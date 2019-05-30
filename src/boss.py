class Boss:
    def __init__(self, name, health, source_mana, current_room):
        self.name = name
        self.health = int(health)
        self.source_mana = int(source_mana)
        self.current_room = current_room


class Dragon(Boss):
    def __init__(self):
        super().__init__(name="Fire Drake", health=100, source_mana=100,
                         current_room=['treasure'])

    def fire_shot(self):
        print("Fires super hot fury!")
