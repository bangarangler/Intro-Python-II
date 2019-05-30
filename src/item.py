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
        answer = input('are you sure you want to drop the torch? y/n')
        answer = str(answer)
        if answer == "y":
            print(f"{self.name} has been dropped and will probably be missed.")
            return True
        else:
            print(f'{self.name} put back into inventory!')
            return False


