# class two_and_a_half

class Two_and_a_half:
    def __init__(self, name, doll):
        self.name = name
        self.doll = doll

    def __str__(self):
        return f"The character {self.name} has {self.doll} dolls in his bedroom."

charlie = Two_and_a_half("Charlie", 1)
Allan = Two_and_a_half("Allan", 25)

print(charlie)
print(Allan)

