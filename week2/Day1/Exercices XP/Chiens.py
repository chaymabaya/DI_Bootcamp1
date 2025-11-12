class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} fait ouaf !')

    def jump(self):
        print(f'{self.name} saute {self.height * 2 }  cm de haut ')

davids_dog = Dog( "othmane", 8)
sarahs_dog = Dog("lolo", 8)
sarahs_dog.bark()
sarahs_dog.jump()
davids_dog.bark()
davids_dog.jump()
if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} est plus grand que {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height :
    print(f"{davids_dog.name} est plus petite que {sarahs_dog.name}")
else:
    print(f" {davids_dog.name} et {sarahs_dog.name} ont la méme taille ")