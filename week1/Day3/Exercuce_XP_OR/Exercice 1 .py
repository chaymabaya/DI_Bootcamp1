#foction to calculate age based on birth datete
def get_age(year, month, day):
    current_year = 2025
    current_month = 1
    current_day = 1
    age = current_year - year
    if (current_month, current_day) < (month, day):
        age -= 1   
    return age
def can_retire( gender , date_of_birth ):
    year, month, day = map(int, date_of_birth.split('/'))
    age = get_age(year, month, day)
    if gender.lower() == 'male':
        return age >= 67
    elif gender.lower() == 'female':
        return age >= 62
    else:
        raise ValueError("Gender must be 'male' or 'female'")    

gender = input("Entrez votre sexe (male ou female) : ")
date_of_birth = input("Entrez votre date de naissance (aaaa/mm/jj) : ")
if can_retire(gender, date_of_birth):
    print("Vous pouvez prendre votre retraite.")
else:
    print("Vous ne pouvez pas encore prendre votre retraite.")