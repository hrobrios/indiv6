import csv

# función para verificar información
def verificar_informacion():
    with open('usuarios.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            nombre = row[0]
            teléfono = row[3]
            edad = row[4]
            # Realizar operaciones o verificaciones con los datos obtenidos
            print(f"Nombre: {nombre}, Teléfono: {teléfono}, Edad: {edad}")

# Verificar información
verificar_informacion()
