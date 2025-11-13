
class chat :
    def __init__(self , name , age ):
        self.name = name
        self.age = age
    def walk (self):
        return f'{self.name} is walking'
class Siamese(chat):
    def make_sound(self):
        return f"{self.name} (Siamese) fait un miaulement doux !"
class Bengal(chat):
        def make_sound(self):
            return f"{self.name} (Bengal) fait un miaulement sauvage !"
class Chartreux(chat):
    def make_sound(self):
        return f"{self.name} (Chartreux) fait un miaulement grave !"

class Pets:
        def __init__(self, animals):
            self.animals = animals

        def walk(self):
            for animal in self.animals:
                print(animal.walk())

bengal_obj = Bengal("lolo", 3)
chartreux_obj = Chartreux("jiji", 5)
siamese_obj = Siamese("Luna", 2)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]
sara_pets = Pets(all_cats)
sara_pets.walk()
