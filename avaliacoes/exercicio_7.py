def calcular_idades_em_dias(years, months, days):
   
    days_in_years = years * 365

    days_in_months = months * 30

    total_days = days_in_years + days_in_months + days

    return total_days


years = int(input("Introduza seus anos de idade: \n"))
months = int(input("Introduza seus meses que estão a percorrer ate o proximo aniversario: \n"))
days = int(input("Introduza seus dias que estão a percorrer ate o proximo aniversario: \n"))

age_in_days = calcular_idades_em_dias(years, months, days)

print(f"A sua idade em dias é: {age_in_days}.")