print('Calculadora de IMC \n')
weight = float(input('Ingrese su peso en kilogramos: '))
height = float(input('Ingrese su altura en metros: '))

bmi = weight / height ** 2

print(f'Su indice de masa corporal (BMI) es: {bmi:.2f}')
if bmi < 18.5:
    print('Usted tiene un peso insuficiente!')
elif bmi >= 18.5 and bmi < 25:
    print('Usted tiene un peso normal!')
elif bmi >= 25 and bmi < 30:
    print('Usted tiene sobrepeso!')
else:
    print('Usted tiene obesidad!')