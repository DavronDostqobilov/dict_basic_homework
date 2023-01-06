def cities_dict(cities:list):
    """
    Given a list of cities names, Return dictionary with keys ordered by city name.
    Args:
        cities(list): list of cities names
    Returns:
        dict: dictionary with keys ordered by city name
    """
    i = 0
    c = {}
    while  i < len(cities):
        c[i] = cities[i]
        i += 1
    return c
print(cities_dict(['New York', 'Los Angeles', 'Chicago', 'Boston', 'San Francisco']))