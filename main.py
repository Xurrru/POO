from paciente import Paciente
pacientes:list[Paciente] = [
    Paciente("11.111.111-1", "Luis Arriagada", 40, "Isapre"),
    Paciente("22.222.222-2", "Paola Pardo", 40, "Fonasa"),
]

def leer_numero(mensaje: str) -> int:
    while True:
        try:
            num=int(input(mensaje))
            return num
        except ValueError:
            print("Error: Debe ingresar un numero")

def menu() -> int:
    print("Clinica")
    print("1.-Agregar Paciente")
    print("2.-Editar Paciente")
    print("3.-Eliminar un Paciente")
    print("4.-Imprimir un Paciente")
    print("5.-Imprimir todos los Pacientes")
    print("6.-Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def agregar_paciente() -> None:
    rut = input("Ingrese el RUT del paciente: ") 
    nombre = input("Ingrese el nombre del paciente: ")
    edad = leer_numero("Ingrese la edad del paciente: ")
    print("Previsiones disponibles")
    print("1.-Fonasa")
    print("2.-Isapre")
    print("3.-Particular")
    print("4.-Otro")
    print("5.-Salir")
    Prevision = leer_numero("Seleccione una opción: ")
    if Prevision == 1:
        prevision = "Fonasa"
    elif Prevision == 2:
        prevision = "Isapre"
    elif Prevision == 3:
        prevision = "Particular"
    elif Prevision == 4:
        prevision = "Otro"
    else:
        prevision = ""
        print("Error: Opción inválida. El paciente no fue registrado.")
        return
    
    try:
        paciente = Paciente(rut, nombre, edad, prevision)
    except (ValueError, TypeError) as e:
        print(f"Error al crear el paciente: {e}")
        return
    
    pacientes.append(paciente)
    print("Paciente agregado correctamente.")
    print("--------------------")

def buscar_paciente() -> Paciente | None:
    rut = input("Ingrese el RUT del paciente a buscar: ")
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
    return None

def imprimir_pacientes() -> None:
    if len(pacientes) == 0:
        print("No hay pacientes registrados.")
    else:
        for paciente in pacientes:
            print(paciente)
            print("--------------------")
    
def confirmar(mensaje: str) -> bool:
    while True:
        respuesta = input(mensaje + " (s/n): ").strip().lower()
        if respuesta in ('s', 'n'):
            return respuesta == 's'
        print("Error: Debe ingresar 's' para sí o 'n' para no.")

def eliminar_paciente() -> None:
    paciente = buscar_paciente()
    if paciente:
        if confirmar(f"¿Está seguro que desea eliminar al paciente {paciente.nombre}?"):
            pacientes.remove(paciente)
            print("Paciente eliminado.")
        else:
          print("Eliminación cancelada.")
    else:
        print("Paciente no encontrado.")

def editar_paciente() -> None:
    paciente = buscar_paciente()
    if paciente:
        print("Menu edicion paciente")
        print("1.-Editar Nombre")
        print("2.-Editar Edad")
        print("3.-Editar Prevision")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar una opción numérica.")
            return
        if opcion == 1:
            print(f"Nombre actual: {paciente.nombre}")
            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
            if not nuevo_nombre:
                print("Error: El nombre no puede estar vacío.")
                return
            paciente.nombre = nuevo_nombre
            print("Nombre actualizado.")
            print("--------------------")
        elif opcion == 2:
            print(f"Edad actual: {paciente.edad}")
            try:
                nueva_edad = int(input("Ingrese la nueva edad: ").strip())
                if nueva_edad < 0:
                    print("Error: La edad no puede ser negativa.")  
                else:
                    paciente.edad = nueva_edad
                    print("Edad actualizada.")
            except ValueError:
                print("Error: Por favor, ingrese un número válido para la edad.")
            print("--------------------")
        elif opcion == 3:
            print(f"Previsión actual: {paciente.prevision}")
            print("Previsiones disponibles")
            print("1.-Fonasa")
            print("2.-Isapre")
            print("3.-Particular")
            print("4.-Otro")
            try:
                nueva_prevision = int(input("Seleccione una opción: ").strip())
            except ValueError:
                print("Error: Debe ingresar una opción numérica.")
                return
            if nueva_prevision == 1:
                paciente.prevision = "Fonasa"
            elif nueva_prevision == 2:
                paciente.prevision = "Isapre"
            elif nueva_prevision == 3:
                paciente.prevision = "Particular"
            elif nueva_prevision == 4:
                paciente.prevision = "Otro"
            else:
                print("Error: Opción inválida")
                return
            print("Previsión actualizada.")
            print("--------------------")
        else:
            print("Error: Opción inválida.")

def main():
    while True:
        op = menu()
        if op==1:
            print("Agregando Paciente")
            agregar_paciente()
        elif op==2:
            print("Editando Paciente")
            editar_paciente()
        elif op==3:
            print("Eliminando Paciente")
            eliminar_paciente()
        elif op==4:
            print("Imprimiendo un Paciente")
            print("--------------------")
            buscar =buscar_paciente()
            if buscar is not None:
                print(buscar)
            else:
                print("Paciente no encontrado")
            print("--------------------")
        elif op==5:
            print("Imprimiendo todos los Pacientes")
            print("--------------------")
            imprimir_pacientes()
        elif op==6:
            print("Saliendo del programa")
            break
    
if __name__ == "__main__":
    main()

