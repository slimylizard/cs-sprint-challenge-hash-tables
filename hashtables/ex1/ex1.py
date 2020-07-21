def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    dict = {}
    for i in range(length):
        dict[weights[i]] = i    
    
    for index, weight in enumerate(weights):
        temp = limit - weight
        if temp in dict:
            i = dict[temp]
            return (index, i) if index > i else (i, index)
    
    return None
