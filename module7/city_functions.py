# James Buzzell
# 11/23/2025
# assignment 7.2


def cit_cou(cit_name, cou_name, popu = '', lang = ''):
    if lang:
        city = f"{cit_name}, {cou_name} " + "- " + f"population {popu}, {lang}"
    elif popu:
        city = f"{cit_name}, {cou_name} " + "- " + f"population {popu}" 
    else:
        city = f"{cit_name}, {cou_name}"
    return city

print(cit_cou("Warsaw", "Poland"))
print(cit_cou("Moscow", "Russia"))
print(cit_cou("Paris", "France"))

print(cit_cou("Warsaw", "Poland", 587588))
print(cit_cou("Moscow", "Russia", 55555555))
print(cit_cou("Paris", "France", 54888888))

print(cit_cou("Warsaw", "Poland", 587588, "Polish"))
print(cit_cou("Moscow", "Russia", 55555555, "Russian"))
print(cit_cou("Paris", "France", 54888888, "French"))