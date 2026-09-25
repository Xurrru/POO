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
        print("Error: Opción inválida")
        return
    pacientes.append(Paciente(rut, nombre, edad, prevision))

def main():
    while True:
        op = menu()
        if op==1:
            print("Agregando Paciente")
        elif op==2:
            print("Editando Paciente")
        elif op==3:
            print("Eliminando Paciente")
        elif op==4:
            print("Imprimiendo un Paciente")
        elif op==5:
            print("Imprimiendo todos los Pacientes")
        elif op==6:
            print("Saliendo del programa")
            break
    
if __name__ == "__main__":
    main()

