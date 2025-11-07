mot = input("entrer le mot ")
#print(f"vous avez saisi {mot} ")

dic = {}
for index , lettre  in enumerate(mot) :
  if lettre in dic :
      dic[lettre].append(index)
  else:
      dic[lettre] = [index]
print(dic)