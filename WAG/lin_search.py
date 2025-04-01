def lin_search(ordered_array, search_value):
    # iterate through every element in the array
    search_index = 0
    for index,value in enumerate(ordered_array):
        if value > search_value:
            print(f"{search_value} is not in this array!")
            break
        elif value == search_value:
            print(f"{search_value} is in array at index {index}")
            search_index = index
            break
    if search_index != 1:
        return 0
    else:
        return search_index


array = [3, 17, 75,80, 202]

lin_search(array, 3)
