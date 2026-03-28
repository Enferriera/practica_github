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
            while True:
                print(''' Elija el dia de la reserva
                    1. Lunes
                    2. Martes
                    ''')
                dia=input("Ingrese una opcion de dia: ")
                match dia:
                    case "1":
                        nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        while not nombre_paciente.isalpha():
                            print("El nombre no debe contener numeros")
                            nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        if nombre_paciente==lunes1 or nombre_paciente==lunes2 or nombre_paciente == lunes3 or nombre_paciente==lunes4:
                            print("El paciente ya tiene turno reservado")
                            
                        else:
                            if lunes1=="":
                                lunes1=nombre_paciente
                                print("Se agendo en el primer turno")
                            elif lunes2=="":
                                lunes2=nombre_paciente
                                print("Se agendo en el segundo turno")
                            elif lunes3=="":
                                lunes3=nombre_paciente
                                print("Se agendo en el tercer turno")
                            elif lunes4=="":
                                lunes4=nombre_paciente
                                print("Se agendo en el cuarto turno")
                            else:
                                print("No hay turnos disponibles")

                        break
                            
                    case "2":
                        nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        while not nombre_paciente.isalpha():
                            print("El nombre no debe contener numeros")
                            nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        if nombre_paciente==martes1 or nombre_paciente==martes2 or nombre_paciente == martes3:
                            print("El paciente ya tiene turno reservado")
                            
                        else:
                            if martes1=="":
                                martes1=nombre_paciente
                                print("Se agendo en el primer turno")
                            elif martes2=="":
                                martes2=nombre_paciente
                                print("Se agendo en el segundo turno")
                            elif martes3=="":
                                martes3=nombre_paciente
                                print("Se agendo en el tercer turno")
                            
                            else:
                                print("No hay turnos disponibles")
                        break
                    case _:
                        print("La opcion ingresada no es valida")
        case "2":
           while True:
                print(''' Elija el dia a cancelar
                    1. Lunes
                    2. Martes
                    ''')
                dia=input("Ingrese una opcion de dia: ")
                match dia:
                    case "1":
                        nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        while not nombre_paciente.isalpha():
                            print("El nombre no debe contener numeros")
                            nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        if nombre_paciente==lunes1:
                            lunes1=""
                            print("El 1er turno del lunes fue cancelado")
                        elif nombre_paciente==lunes2:
                            lunes2=""
                            print("El 2do turno del lunes fue cancelado")
                        elif nombre_paciente==lunes3:
                            lunes3=""
                            print("El 3er turno del lunes fue cancelado")
                        elif nombre_paciente==lunes4:
                            lunes4=""
                            print("El 4to turno del lunes fue cancelado")
                        else:
                            print(f"El paciente {nombre_paciente} no tiene reserva de turno el lunes")
                        break
                    case "2":
                        nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        while not nombre_paciente.isalpha():
                            print("El nombre no debe contener numeros")
                            nombre_paciente=input("Ingrese el nommbre del paciente: ").strip().capitalize()
                        if nombre_paciente==martes1:
                            martes1=""
                            print("El 1er turno del martes fue cancelado")
                        elif nombre_paciente==martes2:
                            martes2=""
                            print("El 2do turno del martes fue cancelado")
                        elif nombre_paciente==martes3:
                            martes3=""
                            print("El 3er turno del martes fue cancelado")
                        
                        else:
                            print(f"El paciente {nombre_paciente} no tiene reserva de turno el martes")
                        break
                        
        case "3":
            pass
        case "4":
            pass
        case "5":
            print("Gracias por usar nuestros servcios.")
            break
        case _:
            print("La opcion ingresada no es valida.")