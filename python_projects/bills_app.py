class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount 

def add_expense(expense_list):
    category = input('Ingresa la categoría del gasto: ')
    amount = float(input('Ingresa el monto del gasto: '))
    expense = Expense(category, amount)
    expense_list.append(expense)
    print('Gasto registrado exitosamente!')

def expense_summary(expense_list):
    categories = {}
    total = 0
    for expense in expense_list:
        if expense.category in categories:
            categories[expense.category] += expense.amount
        else:
            categories[expense.category] = expense.amount
        total += expense.amount
    print('Resumen de gastos:')
    for category, amount in categories.items():
        print(f'{category}: ${amount:.2f}')
    print(f'Total: ${total:.2f}')

expenses = []

while True:
    print('\nBienvenido al gestor de gastos')
    print('1. Agregar un nuevo gasto')
    print('2. Mostrar un resumen de gastos')
    print('3. Salir')
    opcion = input('Selecciona una opción: ')
    if opcion == '1':
        add_expense(expenses)
    elif opcion == '2':
        expense_summary(expenses)
    elif opcion == '3':
        break
    else:
        print('Opción inválida. Inténtalo de nuevo')
