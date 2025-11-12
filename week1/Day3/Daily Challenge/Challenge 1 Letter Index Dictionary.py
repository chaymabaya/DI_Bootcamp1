mot = input("entrer le mot ")
#print(f"vous avez saisi {mot} ")

dic1 = {}
for index , lettre  in enumerate(mot) :
    if lettre in dic :
      dic1[lettre].append(index)

    else:
       dic1[lettre] = [index]
print(dic1)