import math
class Circle :
    def __init__(self , rayan=1):
        self.rayan = rayan
    def périmétre(self ):
        P = 2* self.rayan * math.pi
        return P
    def aire(self ):
        Aire = 2*self.rayan *self.rayan
        return Aire
    def affiche(self):
        print("Un cercle est l'ensemble des points d'un plan situés à une distance constante appelée rayon, d'un point fixe appelé centre.")

circle1 = Circle(2)
print ( f" le périmetre de circle est {circle1.périmétre()}")
print(f"Aire de circle est {circle1.aire()}")
circle1.affiche()


