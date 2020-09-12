def print_enumerated_list(l):
    print(enumerated_list_str(l))

def enumerated_list_str(l):
    list_with_numbers = [f'{i + 1} - {str_item}' for i, str_item in enumerate(l)]
    return '\n'.join(list_with_numbers)
