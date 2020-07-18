def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    counter = 0
    dict = {}
    for item in weights:
        dict[item] = counter
        counter += 1
    
    print(dict)
    for item in weights:
        temp = limit - item
        if temp in dict:
            1 = [dict[temp]]
            1.append(dict[item])
            print(1)
            return 1

    return None
