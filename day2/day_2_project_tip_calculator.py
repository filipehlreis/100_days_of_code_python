# 1. Dar saudações ao usuario.
print('\n\nWelcome to the tip calculator!')

# 2. Peça ao usuario o total da conta.
bill = float(input('What was the total bill? $'))

# 3. Pergunte ao usuario a porcentagem de gorjeta
tip_percentage = int(input('What percentage tip would you like to give? ' +
                           '10, 12, or 15? ')
                     )

# 4. Calculo do total da conta com a gorgeta inclusa.
total_bill = bill * (1+tip_percentage/100)

# 5. Pergunte em quantas pessoas deve-se dividir a conta.
qtd_people = int(input('How many people to split the bill? '))

# 6. Calculo do total por pessoa.
total_per_person = round((total_bill / qtd_people), 2)

# 7. Informe ao usuario quanto cada pessoa deve pagar.
print(f'Each person should pay: ${total_per_person:.2f}')
