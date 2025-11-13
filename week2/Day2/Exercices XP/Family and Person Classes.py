class Person :
    def __init__(self , First_name , age , Last_name = "" ):
        self.first_name = First_name
        self.age = age
        self.last_name = Last_name
    def is_18(self):
        return True if self.age>= 18 else False
class Family :
    def __init__ (self , Last_name):
        self.last_name = Last_name
        self.membres = []
    def born(self , First_name , age ):
        self.first_name = First_name
        self.age = age
        new_member = Person(First_name, age, self.last_name)
        self.membres.append(new_member)
    def check_majority(self , First_name):
        for member in self.membres :
            if member.first_name == First_name :
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return

    def family_presentation(self ):
        print(f"Nom de famille : {self.last_name}")
        print("Membres de la famille :")
        for member in self.membres:
            print(f" {member.first_name}, âge : {member.age}")

famille = Family("Dupont")
famille.born("Alice", 20)
famille.born("Bob", 15)

famille.check_majority("Alice")
famille.family_presentation()