tupla = ("1", "2", "8", "7", "6", "4", "6", "420")

# Initialize the index variable
i = 0

# Iterate over the tuple using a while loop
while i < len(tupla):
    # Check if the current element is equal to 6
    if tupla[i] == "6":
        # Print the desired message to the console
        print(f"O elemento de índice {i} é igual a 6")

    # Increment the index variable
    i += 1
