def get_ordered_list(lst=None):
    if lst is None:
        user_input = input("Enter list of integers, seperated by commas")
        lst = list(map(int, user_input.split(',')))
    return sorted(lst)

