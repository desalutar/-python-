# def get_city_country(country, city, population=''):
#     full_name = f"{country} {city} {population}"
#     return full_name.title()

def get_city_country(country, city, population=''):
    if population:
        full_name = f"{country} {city} {population}"
    else:
        full_name = f"{country} {city}"

    return full_name.title()