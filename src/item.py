class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'{self.name} obtained!')

    def on_drop(self):
        print(f"{self.name} discarded")

class LightSource(Item):
    def on_drop(self):
        # super().__init__(self, name, description)
        answer = input('you should probably keep this y/n')
        answer = str(answer)
        if answer == "y":
            print(f"{self.name} needs to be picked up again")
        else:
            print(f'{self.name} has been dropped!')


