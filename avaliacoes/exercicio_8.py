def calculate_percentage(part, total):

    percentage = (part / total) * 100
    return round(percentage, 2)

# Read the total number of voters
total_voters = int(input("Insira o numero total dos votos: "))

# Read the number of blank votes
blank_votes = int(input("Insira os votos em brancos: "))

# Read the number of null votes
null_votes = int(input("Insira os votos nulos: "))

# Read the number of valid votes
valid_votes = int(input("Insira os votos validos: "))

# Calculate the percentage of each type of vote
blank_percentage = calculate_percentage(blank_votes, total_voters)
null_percentage = calculate_percentage(null_votes, total_voters)
valid_percentage = calculate_percentage(valid_votes, total_voters)

# Print the results
print(f"Percentagem dos votos em brancos: {blank_percentage}%")
print(f"Percentagem dos votos nulos: {null_percentage}%")
print(f"Percentagem dos votos validos: {valid_percentage}%")