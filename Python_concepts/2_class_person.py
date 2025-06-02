# Big bang, two and a half man and family

class two_and_a_half_man:
    def __init__(self, name, womans):
        self.name = name
        self.womans = womans


    def __str__(self):
        return f'The character {self.name} has {self.womans} women in his bedroom'

character = two_and_a_half_man("Charlie", 5)
character2 = two_and_a_half_man("Alan", -2)

print(character2)
print(character)