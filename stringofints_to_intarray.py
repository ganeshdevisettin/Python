def make_arr(message):
    # Enter string of ints, with a space between each integer
    new_arr = input(f"Enter values for {message}: ").split()
    for i in range(len(new_arr)):
        new_arr[i] = int(new_arr[i])
    return new_arr
