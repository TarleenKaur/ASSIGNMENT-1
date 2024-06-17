from datetime import date
 
def Age(birthDate):
    days_in_year = 365.2425   
    age = int((date.today() - birthDate).days / days_in_year)
    return age

print(Age(date(1997, 2, 3)), "years")