usuarios = {
    'alfredo':'1234',
    'navas' : '5678' 
    }

def registrar_usuario(usuarios):
    while True:
        usuario = input("\nIngrese el nombre de usuario (o 'exit' para regresar): ").lower()
        if usuario == 'exit':
            break
        if usuario in usuarios:
            print("El usuario ya existe. ingrese otro nombre.")
        else:
            contrasena = input("Ingrese la contraseña: ")
            usuarios[usuario] = contrasena
            print("Usuario registrado correctamente.")
            break

def iniciar_sesion(usuarios):
    while True:
        usuario = input("\nIngrese el nombre de usuario (o 'exit' para regresar): ").lower()
        if usuario == 'exit':
            break
        contrasena = input("Ingrese su contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("\nInicio de sesión exitoso.")
            break
        else:
            print("Nombre de usuario o contraseña incorrectos.")
    
def mostrar_usuarios_registrados(usuarios):
    print("\nLos usuarios registrados son los siguientes:")
    print(list(usuarios.keys()))

def mostrar_menu():
    print("\nMenú:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Mostrar usuarios registrados")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    try:
        opcion_int = int(opcion)
    except ValueError:
        opcion_int = None
    if opcion == '1':
        registrar_usuario(usuarios)
    elif opcion == '2':
        iniciar_sesion(usuarios)
    elif opcion == '3':
        mostrar_usuarios_registrados(usuarios)
    elif opcion == '4':
        print("\nSaliendo del programa...\n")
        break
    else:
        print("Opción inválida, por favor ingrese entre las opciones (1), (2) y (3).")