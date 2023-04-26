tasks = []


def add_task():
    task = input('Ingrese la tarea que desea agregar: ')
    tasks.append(task)
    print('La tarea ha sido agregada correctamente!')


def delete_task():
    task = input('Ingrese la tarea que desea eliminar: ')
    if task in tasks:
        tasks.remove(task)
        print('La tarea ha sido eliminada correctamente!')
    else:
        print('La tarea ingresada no se encuentra en la lista!')


def completed_task():
    task = input('Ingrese la tarea que desea marcar como completada: ')
    if task in tasks:
        tasks[tasks.index(task)] = f'{task} (Completada)'
        print('La tarea ha sido marcada como completada!')
    else:
        print('La tarea ingresada no se encuentra en la lista!')


while True:
    print('\nSeleccione una opción:')
    print('1. Agregar tarea')
    print('2. Eliminar tarea')
    print('3. Marcar tarea como completada')
    print('4. Mostrar lista de tareas')
    print('5. Salir')
    opc = int(input('Ingrese una opción: '))
    if opc == 1:
        add_task()
    elif opc == 2:
        delete_task()
    elif opc == 3:
        completed_task()
    elif opc == 4:
        if len(tasks) == 0:
            print('La lista de tareas está vacía!')
        else:
            print('Lista de tareas:')
            for task in tasks:
                print(f'- {task}')
    elif opc == 5:
        break
    else:
        print('Opción inválida. Intente de nuevo!')
