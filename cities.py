def describe_city(name, country = "Japan"):
    """Get a personilized description of a city"""
    print(f"{name.title()} is in {country.title()}")

describe_city("tokyo")
describe_city("osaka")
describe_city("vancouver", "canada")