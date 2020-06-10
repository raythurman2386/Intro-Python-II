# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        output = f"\nWelcome to the {self.name}!"
        output += f"\n\n{self.description}"
        return output

    def show_items(self):
        i = 1
        for item in self.items:
            print(f"\n {i}: {item}")
            i += 1

    def remove_item(self, item):
        del self.items[item]
        return f"You removed the {item.name} from {self.name}"

    def add_item(self, item):
        self.items.append(item)
        return f"You added {item.name} to {self.name}"
