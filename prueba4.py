usuarios = []
def ingresar_usuario(nusuario,sexo,contraseña):
    for u in usuarios:
        if u["nusuario"].lower() == nusuario.lower():
            print("Usuario ya existe. Intente otro.")
            return
    nuevo_usuario = {
        "nusuario":nusuario,
        "sexo":sexo,
        "contraseña":contraseña
    }
    usuarios.append(nuevo_usuario)
    print("¡Usuario ingresado con éxito!")

def buscar_usuario(nusuario):
    for u in usuarios:
        if u["nusuario"] == nusuario:
            print(f"El sexo del usuario es: {u['sexo']} y la contraseña es: {u['contraseña']}.")
            return
    print("El usuario no se encuentra.")

def eliminar_usuario(usuario):
    for u in usuarios:
        if u["nusuario"].lower() == usuario.lower():
            usuarios.remove(u)
            print("Usuario eliminado con éxito.")
            return
    print("No se pudo eliminar usuario.")
    
def menu_principal():
    while True:
        print("---Menú de ingreso de usuarios---")
        print("1.- Ingresar un usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir")

        try:
            opcion = int(input("Ingresa una opción (1-4): "))

            match opcion:
                case 1:
                    nusuario = input("Ingrese nombre de usuario: ")

                    while True:
                        sexo = input("Ingrese sexo: ").upper()
                        if sexo in ["F", "M"]:
                            break
                        else:
                            print("Debe ingresar M o F solamente. Intente de nuevo")

                    while True:
                        contraseña = input("Ingrese contraseña: ")
                        if len(contraseña) >= 8 and " " not in contraseña:
                            break
                        else:
                            print("Contraseña no válida. Intente otra.")

                    ingresar_usuario(nusuario,sexo,contraseña)
        
                case 2:
                    nusuario = input("Ingrese usuario a buscar: ")
                    buscar_usuario(nusuario)

                case 3:
                    usuario = input("Ingrese usuario a eliminar: ")
                    eliminar_usuario(usuario)

                case 4:
                    print("Programa terminado.")
                    print("Saliendo del sistema...")
                    break

                case _:
                    print("Por favor escoge una opción válida.")

        except ValueError:
            print("Por favor ingresa solo un número.")
            
menu_principal()