class Farm :
    def __init__(self , farm_name):
        self.name = farm_name
        self.animals = {}
    def add_animal ( self , animal_type , count = 1 ):
        if animal_type in self.animals :
            count += self.animals[animal_type]
        else:
            self.animals[animal_type]= count
    def get_info (self):
        info = f"{self.name} s farm  \n "
        info += "-" * 20 + "\n"
        for animal in self.animals.items() :
            info += f"{animal:<10} : {number}\n"
        info += "-" * 20 + "\nEIEI-0 !"
        return info



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

