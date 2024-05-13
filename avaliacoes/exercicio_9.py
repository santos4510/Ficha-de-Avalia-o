def calculate_average(grades):
   
    total = sum(grades)
    average = total / len(grades)
    return average

def main():
    # Read the four grades
    grades = []
    for i in range(1, 5):
        grade = float(input(f"Insira as notas {i}: "))
        grades.append(grade)

    # Calculate the average
    average = calculate_average(grades)
    print(f"A media das 4 notas é: {average}.")

    # Check if the student is approved or not
    if average >= 7:
        print("APROVADO")
    else:
        # Read the grade of the final exam
        final_exam = float(input("Insira a nota do exame final: "))

        grades.append(final_exam)
        new_average = calculate_average(grades)
        print(f"A nova nota é: {new_average}.")

        if new_average >= 5:
            print("APROVADO")
        else:
            print("REPROVADO")

if __name__ == "__main__":
    main()