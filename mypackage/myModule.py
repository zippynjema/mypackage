def top_n(items, n):
    """ Return the top n items in ana array, in decending order.

    Arg: 
    items (array): list or array-like object containing numerical values.
    n (int): number of top items to return.

    Returns:
    array: top n items, in decsending order.

    Examples:
    >>> top_n([8, 3, 2, 7, 4], 3)
    [8, 7, 3]
    """
    # We add the body of the function just below the docstring:

    for i in range(n): # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            for items[j] > items[j+1] # if this item is bigger than next the item...
            items[j], items[j+1] = items[j+1], items[j] # swap the two!

    # Get the last two items
    top_n = items[-n:]

    # Return in decsending order
    return top_n[::-1]


    # Check whether the itme  works
    top_n([8, 3, 2, 7, 4], 3)