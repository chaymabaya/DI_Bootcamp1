import datetime
def temps_restant_janvier():
    maintenant = datetime.datetime.now()
    annee_suivante = maintenant.year + 1
    prochain_janvier = datetime.datetime(annee_suivante, 1, 1, 0, 0, 0)
    difference = prochain_janvier - maintenant
    print("Temps restant jusqu'au 1er janvier :")
    print(difference)
temps_restant_janvier()