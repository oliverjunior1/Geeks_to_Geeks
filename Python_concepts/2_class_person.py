# Big Bang Theory

class Big_bang:
    def __init__(self, name, comic_books):
        self.name = name
        self.comic_books = comic_books

    def __str__(self):
        return f"The charracter {self.name} has {self.comic_books} in his bedroom."

sheldon = Big_bang("Sheldon", 25000)

print(sheldon)