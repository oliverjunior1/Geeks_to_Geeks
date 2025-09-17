# class big bang

class Big_bang:
    def __init__(self, character, comic_books):
        self.character = character
        self.comic_books = comic_books

    def __str__(self):
        return f"The character {self.character} has {self.comic_books} comic-books in the plastic, and in his bedroom."

Sheldon = Big_bang("Sheldon", 25000)
Leonard = Big_bang("Leonard", 19758)
Howard = Big_bang("Howard", 15001)
Hajesh = Big_bang("Hajesh", 8008)

print(Sheldon)
print(Leonard)
print(Howard)
print(Hajesh)
