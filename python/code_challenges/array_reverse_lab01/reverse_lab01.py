def reverse_list(linked_list):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    # put your function implementation here

    revarsed_list = linked_list[::-1]
    print(revarsed_list)
    return revarsed_list

if __name__ == '__main__':
    my_list=[1,2,3,4,5]
    reverse_list(my_list)
