# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self,name,description,is_light, has_boss):
        self.name = name
        self.description = description
        self.items = []
        self.is_light = is_light
        self.has_boss = has_boss
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __repr__(self):
        return_string = f"*******\n\n{self.name}\n\n {self.description}\n\n*********"
        return_string += f"Items laying around room: \n"
        return_string += f"{[item.name for item in self.items]}"
        return return_string


    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
