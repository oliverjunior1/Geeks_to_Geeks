# family

class family:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"The name is {self.name} and the age is {self.age} years old."

name1 = family("Joao",12)
name2 =family("Mariane",4)

print(name1)
print(name2)