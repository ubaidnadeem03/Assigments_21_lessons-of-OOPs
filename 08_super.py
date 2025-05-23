class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Ameen Alam", "Programming")
print(t.name, t.subject)