def make_arr(message):
    new_arr = input(f"Enter values for {message}: ").split()
    for i in range(len(new_arr)):
        new_arr[i] = int(new_arr[i])
    print(new_arr)