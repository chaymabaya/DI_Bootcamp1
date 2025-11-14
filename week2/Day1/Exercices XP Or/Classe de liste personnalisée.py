class Mylist:
    def __init__(self , list =[] ):
        self.list = list
    def list_inverse(self):
        self.list.reverse()
        return self.list
    def list_triée (self):
        self.list.sort()
        return self.list

list1 = Mylist([1,2,9,0, 4])
print (list1.list_inverse())
print(list1.list_triée())

