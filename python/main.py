alumnos = [
    ['juan', [['matematicas', 8], ['lengua', 9], ['sociales', 7], ['naturales', 7]]],
    ['ana', [['lengua', 9], ['matematicas', 10], ['sociales', 8], ['naturales', 6]]],
    ['luis', [['lengua', 6], ['sociales', 8], ['matematicas', 7], ['naturales', 6]]],
    ['maria', [['lengua', 9], ['sociales', 10], ['naturales', 10], ['matematicas', 9]]]
]

def agregar_calificaciones(nombre, materia, nota):
    alumno_encontrado = False
    for alumno in alumnos:
        if alumno[0] == nombre:
            alumno_encontrado = True
            materias = alumno[1]
            materia_encontrada = False
            for mat in materias:
                if mat[0] == materia:
                    mat[1] = nota
                    print(f'la calificacion de {materia} para {nombre} fue actualizada a {nota}')
                    materia_encontrada = True
                    break
            if not materia_encontrada:
                materias.append([materia, nota])
                print(f'la materia {materia} con la calificacion {nota} fue anadida para {nombre}')
            break
    if not alumno_encontrado:
        alumnos.append([nombre, [[materia, nota]]])
        print(f'el alumno {nombre} fue anadido con la materia {materia} y la calificacion {nota}')

def mostrar_calificaciones(nombre):
    for alumno in alumnos:
        if alumno[0] == nombre:
            print(f'\ncalificaciones de {nombre}:')
            for materia in alumno[1]:
                print(f'{materia[0]}: {materia[1]}')

def mostrar_todos_los_alumnos():
    print("\nlista de todos los alumnos y sus calificaciones:")
    for alumno in alumnos:
        print(f"\nalumno: {alumno[0]}")
        for materia in alumno[1]:
            print(f'{materia[0]}: {materia[1]}')

def ingresar_datos():
    while True:
        print("\nopciones:")
        print("1. ingresar/modificar calificaciones de un alumno")
        print("2. mostrar todos los alumnos y sus calificaciones")
        print("3. salir")
        
        opcion = input("seleccione una opcion (1/2/3): ")

        if opcion == '1':
            nombre = input("ingrese el nombre del alumno (o 'salir' para finalizar): ").lower()
            if nombre == 'salir':
                print("fin del programa")
                break
            alumno_encontrado = False
            for alumno in alumnos:
                if alumno[0] == nombre:
                    alumno_encontrado = True
                    mostrar_calificaciones(nombre)
                    break
            if not alumno_encontrado:
                print(f"alumno {nombre} no encontrado")
                agregar_nuevas_calificaciones = input(f"¿desea agregar al alumno {nombre}? (s/n): ").lower()
                if agregar_nuevas_calificaciones == 's':
                    matematicas = float(input("ingrese la nota de matematicas: "))
                    lengua = float(input("ingrese la nota de lengua: "))
                    sociales = float(input("ingrese la nota de sociales: "))
                    naturales = float(input("ingrese la nota de naturales: "))
                    alumnos.append([nombre, [['matematicas', matematicas], ['lengua', lengua], ['sociales', sociales], ['naturales', naturales]]])
                    print(f"alumno {nombre} anadido con sus calificaciones")
                else:
                    print(f"no se ha anadido al alumno {nombre}")
        
        elif opcion == '2':
            mostrar_todos_los_alumnos()

        elif opcion == '3':
            print("fin del programa")
            break

        else:
            print("opcion no valida, intente nuevamente")

ingresar_datos()
