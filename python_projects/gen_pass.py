import random
import string


long_pass = int(input('Ingrese la longitud de la contraseña deseada: '))
types = string.ascii_letters + string.digits + string.punctuation
passwd = ''.join(random.choice(types) for i in range(long_pass))

print(f'Su contraseña aleatoria y segura es: {passwd}')
