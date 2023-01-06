def count_all(txt):
    """
    Given a function that takes a string and calculates the number of letters and digits within it.
    Return the result in a dictionary.
    Args:
        txt(str): count letters and digits
    Returns:
        dict: dictionary with letters and digits
    """
    k=0
    j=0
    i=0
    while i<len(txt):
        if txt[i].isalpha():
            j+=1
        if txt[i].isdigit():
            k+=1
        i+=1
        
    dict1={'LETTERS': j,'DIGITS': k}
    return dict1
print(count_all('davr1on boy'))