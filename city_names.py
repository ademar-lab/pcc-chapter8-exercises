def city_country(city, country):
    """Returns a "city, country" formatted string"""
    return(f"{city.title}, {country.title}")

print(city_country("salamanca", "mexico"))
print(city_country("san francisco", "united states"))
print(city_country("kioto", "japan"))