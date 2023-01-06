def create_dictionary(key, value):
    """
    Convert two lists into a dictionary
    Args:
        key(list): list of keys
        value(list): list of values
    Returns:
        dict: dictionary with keys and values
    """
    dict1={}
    i=0
    while i<len(key):
        dict1[key[i]]=value[i]
        i+=1
    return dict1
print(create_dictionary([1, 2, 3],["one", "two", "three"]))