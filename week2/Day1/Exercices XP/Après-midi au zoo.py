

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []  # petit changement : "animals" au pluriel (plus clair)

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f'{new_animal} a été ajouté au zoo {self.name}.')
        else:
            print(f'{new_animal} est déjà dans le zoo.')

    def get_animals(self):
        if self.animals:
            print("Animaux dans le zoo :", ", ".join(self.animals))
        else:
            print("Aucun animal dans le zoo.")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} a été vendu.")
        else:
            print(f"{animal_sold} n’est pas présent dans le zoo.")

    def sort_animals(self):
        if self.animals:
            self.animals.sort()  # trie la liste directement
            print("Animaux triés :", ", ".join(self.animals))
        else:
            print("Aucun animal à trier.")

# --- Test du programme ---
brooklyn_safari = Zoo("Brooklyn Safari")

brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Tiger")

print()
brooklyn_safari.get_animals()

print()
brooklyn_safari.sell_animal("Bear")

print()
brooklyn_safari.get_animals()

print()
brooklyn_safari.sort_animals()
