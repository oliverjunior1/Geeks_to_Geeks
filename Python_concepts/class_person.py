class Big_bang:
    def __init__(self, name, comics):
        self.name = name
        self.comics = comics

    def __str__(self):
        return f"The {self.name} has {self.comics} comic-books in his bedroom!"

character = Big_bang("Sheldon", 10000)
character2 = Big_bang("Leonard", 5000)

print(character)
print(character2)