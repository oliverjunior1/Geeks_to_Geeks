# Big_bang_theory

class Big_bang_theory():
    def __init__(self, name, comic_books):
        self.name = name
        self.comic_books = comic_books
    def __str__(self):
        return f"The character {self.name} has {self.comic_books} in his bedroom."


character = Big_bang_theory('Sheldon', 50000)
character2 = Big_bang_theory('Leonard', 15135)
character3 = Big_bang_theory('Rajesh', 8008)
character4 = Big_bang_theory('Howard', 12000)

print(character)
print(character2)
print(character3)
print(character4)