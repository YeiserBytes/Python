total_account = float(input('Ingrese el total de la cuenta: $'))
perce_tip = int(input('Ingrese el porcentaje de propina que desea dejar (por ejemplo, 15 o 20): '))

count_tip = total_account * (perce_tip / 100)
total_tip = total_account + count_tip

print(f'El total de la cuenta es: ${total_account:.2f}')
print(f'La cantidad de propina a dejar es: ${count_tip:.2f}')
print(f'El total de la cuenta con la propina incluida es: ${total_tip:.2f}')