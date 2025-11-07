users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dic1 = { user : index for index , user  in enumerate(users)}
print(dic1)
dic2 = { index : user for index , user  in enumerate(users)}
print(dic2)
dic3 = {user : index for index , user in enumerate(sorted(users))}
print (dic3)
