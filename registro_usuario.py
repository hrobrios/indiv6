import csv

# Definir la función para registrar usuarios
def registrar_usuario(nombre, identificador, contraseña, teléfono, edad):
    with open('usuarios.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, identificador, contraseña, teléfono, edad])

# Registrar usuarios
registrar_usuario("juan", "ID001", "pass123", "1234567890", 25)
registrar_usuario("pedro", "ID002", "pass456", "9876543210", 30)
registrar_usuario("sergio", "ID002", "pass456", "6543210", 30)
registrar_usuario("pat", "ID002", "pass456", "9876543210", 30)
registrar_usuario("ojrge", "ID002", "pass456", "9876543210", 30)
registrar_usuario("taz", "ID002", "pass456", "9876543210", 30)
registrar_usuario("ken", "ID002", "pass456", "9876543210", 30)
registrar_usuario("ryu", "ID002", "pass456", "9876543210", 30)
registrar_usuario("sabat", "ID002", "pass456", "9876543210", 30)


print("Usuarios registrados exitosamente.")

