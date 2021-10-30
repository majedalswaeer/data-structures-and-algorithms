def validate_brackets(characters):
    """
    This function validate if the brackets balanced or not
    """
    modified_stack = []
    stack=[]
    open=['(','{','[']
    close=[')','}',']']

    for i in characters:
        if i in open:
            modified_stack.append(i)
        elif i in close:
            modified_stack.append(i)

    for char in modified_stack:
        if char in open:
            stack.append(char)
        else:
            if not stack:
                return False
            cur = stack.pop()
            if cur == '(':
                if char != ")":
                    return False
            if cur == '{':
                if char != "}":
                    return False
            if cur == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True

if __name__ == '__main__':
    s='{}{Code}[Fellows](())'
    print(validate_brackets(s))
