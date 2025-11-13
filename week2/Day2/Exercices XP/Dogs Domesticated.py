from Dogs import Dog
import random

class PetDog(Dog):
    def __init__(self , name , age , weight , trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        self.bark()
        self.trained = True
        print(f"{self.name} est maintenant dressé !")
    def play (self , *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dog_names)} tous jouent ensemble !")

    def do_a_trick(self):
        if self.trained:
           tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
           print(f"{self.name} {random.choice(tricks)}")

my_dog = PetDog("Rex", 5, 20)
Buddy = PetDog("Buddy", 3, 15)
Max = PetDog("Max", 2, 12)
my_dog.play(Buddy, Max)
my_dog.train()
my_dog.do_a_trick()