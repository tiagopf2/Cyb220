# Written by Tiago Perez

# 11.1 City, Country

def format_city_country(city, country):
    """Return a formatted string like 'Santiago, Chile'."""
    formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string

# 11.2 Population

def format_city_country(city, country, population=None):
    """Return a formatted string like 'Santiago, Chile - population 5000000'."""
    formatted_string = f"{city.title()}, {country.title()}"
    if population:
        formatted_string += f" - population {population}"
    return formatted_string
