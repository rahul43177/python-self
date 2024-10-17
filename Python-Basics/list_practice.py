# def get_unique_elements(arr):
#     return list(set(arr))

# # Example usage
# if __name__ == "__main__":
#     array_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
#     unique_elements = get_unique_elements(array_with_duplicates)
#     print("Unique elements:", unique_elements)

def unique_elements(array):
    array.sort()
    unique_set = set(array)
    unique_list = list(unique_set)
    unique_list.sort()
    return unique_list

array = [1,2,2,2,3,4,5,5,55,12,66,12,55]

unique_element_list = unique_elements(array)
print(unique_element_list)