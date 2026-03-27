lunes1=""
lunes2=""
lunes3=""
lunes4=""

martes1=""
martes2=""
martes3=""

operador=input("Ingrese el nombre del operador: ").strip().capitalize()

while not operador.isalpha():
    print("El nombre solo debe tener letras")
    operador=input("Ingrese el nombre del operador: ").strip().capitalize()

print(f"Gestion de turnos atendido por {operador}")

while True:
    print(''' Elija la opcion del menu que desee
          1. Reservar turno
          2. Cancelar turno (por nombre)
          3. Ver agenda del día
          4. Ver resumen general
          5. Cerrar sistema
          ''')
    opcion=input("Ingrese la opcion del menu que desee: ")
    
    match opcion:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Gracias por usar nuestros servcios.")
            break
        case _:
            print("La opcion ingresada no es valida.")