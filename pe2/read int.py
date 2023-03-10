def read_int(prompt, min_value, max_value):
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = int(input(prompt))
            is_valid_input = True
        except ValueError:
            print("Error: Input must be a valid integer.")
        if is_valid_input:
            is_valid_input = user_input >= min_value and user_input <= max_value
        if not is_valid_input:
            print("Error: The input value must be within the permitted range of " + str(min_value) + " to " + str(max_value) + ".")
    return user_input;


number = read_int("Enter a number between -10 and 10: ", -10, 10)

print("The number is:", number)
