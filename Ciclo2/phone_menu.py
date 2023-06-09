def mostrar_menu():
    print("Bienvenido al menú telefónico:")
    print("1. Saldo")
    print("2. Recargar")
    print("3. Transferir")
    print("4. Salir")

def procesar_opcion(opcion):
    if opcion == "1":
        mostrar_saldo()
    elif opcion == "2":
        realizar_recarga()
    elif opcion == "3":
        realizar_transferencia()
    elif opcion == "4":
        print("Gracias por usar el menú telefónico. ¡Hasta luego!")
        loop = False
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

def mostrar_saldo():
    # Lógica para mostrar el saldo del usuario
    print("Tu saldo actual es $100")

def realizar_recarga():
    # Lógica para realizar una recarga
    print("Recarga exitosa. Tu saldo se ha actualizado.")

def realizar_transferencia():
    # Lógica para realizar una transferencia
    print("Transferencia realizada con éxito.")

# Loop principal del menú telefónico
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    procesar_opcion(opcion)

    if opcion == "4":
        break
