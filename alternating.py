def alternating(string):
    new_str = ''

    for str_index in range(len(string)):
        if str_index % 2 == 0:
            new_str += string[str_index].upper()
        else:
            new_str += string[str_index].lower()

    print(new_str)


alternating('hi my name is yagiz and i am learning python')