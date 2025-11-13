class Dog :
    def __init__(self , name , age , weight):
        self.name = name
        self.age= age
        self.weight = weight
    def bark(self):
        print(f" {self.name} aboie")
    def run_speed(self):
        return (f" {self.weight / self.age * 10}")
    def fight(self , other_dog):
        my_power = self.run_speed() * self.weight
        other_power= other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return (f"{self.name} a gagné le combat contre {other_dog.name}")
        elif my_power < other_power:
            return f"{other_dog.name} a gagné le combat contre {self.name} "
        else:
            return f"Égalité entre {self.name} et {other_dog.name}"
dog1 = Dog("lolo" , 10 , 12)
dog2 = Dog("kiki" , 14 , 20)
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
