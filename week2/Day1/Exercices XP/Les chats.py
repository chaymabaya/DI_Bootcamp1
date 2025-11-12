class cats :
    def __init__(self , name , age):
        self.name = name
        self.age = age
def find_oldest_cat ( cat1 , cat2 , cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest
cat1 = cats( "lolo" , 3)
cat2 = cats("lili" , 4)
cat3 = cats("yala" , 5)
oldest_cat = find_oldest_cat(cat1, cat2, cat3)
print(f"Le chat le plus âgé est {oldest_cat.name}, et il a {oldest_cat.age} ans.")

