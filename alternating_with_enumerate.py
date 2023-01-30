string = 'hi my name is yagiz and i am learning python'


def alternating_with_enumerate(string):
    new_str = ''
    for index, i in enumerate(string):
        if index % 2 == 0:
            new_str += i.upper()
        else:
            new_str += i.lower()

    print(new_str)
    return new_str


alternating_with_enumerate(string)
