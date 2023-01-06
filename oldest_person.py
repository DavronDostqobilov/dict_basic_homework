def oldest(people:dict):
    """
    Given a dictionary containing the names and ages of a group of people, return the name of the oldest person.
    Args:
        people(dict): parameter
    Returns:
        str: the name of the oldest person
    """
    value=0
    for i in people:
        if value<people[i]:
            value=people[i]
            key=i
          
    return key 
print(oldest({"Javohir": 52, "Sharof": 23, "Tolib": 34, "Rustam": 16}))