import datetime
def minutes_depuis_anniversaire(date_anniv_str):
    anniversaire = datetime.datetime.strptime(date_anniv_str, "%d/%m/%Y")
    maintenant = datetime.datetime.now()
    difference = maintenant - anniversaire
    minutes = difference.total_seconds() / 60
    print(f"Tu as vécu environ {int(minutes):,} minutes.")

minutes_depuis_anniversaire("22/02/2000")