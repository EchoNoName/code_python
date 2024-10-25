def dupeRemover(stuff):
    '''removed dupes from a list
    
    args: 
        stuff: A list of values
    
    returns: A list of values with no duplicates
    '''
    return sorted(list(set(stuff)))

print(dupeRemover(['a', 'a', 'b', 'c', 'c']))