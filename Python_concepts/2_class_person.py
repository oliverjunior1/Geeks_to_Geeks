# Two and a half man

class Two_and_a_half_man:
    def __init__(self, character, dolls):
        self.character = character
        self.dolls = dolls

    def __str__(self):
        return f"The character {self.character} has {self.dolls} dolls in his bedroom."

charlie = Two_and_a_half_man("Charlie", 2)
allan = Two_and_a_half_man("Allan", 100)

print(charlie)
print(allan)