class MenuManager :
    def __init__(self ):
        self.menu = [{"name": "Soup" , "price" : 10 , "spice" : "B" , "gluten" : False } ,
                     {"name": "Hamburger" , "price" : 15 , "spice" : "A" , "gluten" : True } ,
                     {"name": "Salad" , "price" : 18 , "spice" : "A" , "gluten" : False } ,
                     {"name": "French Fries" , "price" : 5 , "spice" : "C" , "gluten" : True }]
    def add_item(self , name , price , spice , gluten):
        new_dish = { "name" : name ,
                     'price' : price ,
                     'spice' : spice ,
                     'gluten' : gluten}
        self.menu.append(new_dish)
        print(f'{name} added to menu')
    def update_item(self,name, price, spice, gluten):
        for dish in self.menu:
            if  dish["name"] == name:
                dish['price']=price
                dish['spice'] = spice
                dish['gluten'] =gluten
                print(f"{name} updated to {dish['name']}")
                return
        print(f"Le plat '{name}' n'est pas au menu.")

    def remove_item(self, name):

        for dish in self.menu:
            if dish["name"]== name:
                self.menu.remove(dish)
                print(f"{name} a été supprimé du menu.")
                return
        print(f"Le plat '{name}' n'est pas au menu.")

menu1 = MenuManager()
print(menu1.menu)
menu1.add_item( 'couscous' , 50 , 0 , True)
menu1.update_item('Soup' , 30 , 1 , False)
menu1.remove_item('Salad')
print(menu1.menu)


