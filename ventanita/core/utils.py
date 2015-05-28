def get_item_from_list(my_list, index):
    try:
        value = my_list[index]
    except IndexError:
        value = ''
    return value
