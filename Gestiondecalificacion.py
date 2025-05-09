# Función para determinar el estado de aprobación
def determinar_estado_aprobacion():
    # Solicitar al usuario ingresar una calificación
    academic_marks = float(input("Ingresa calificación (0-100): "))
    
    # Validación de rango
    if academic_marks < 0 or academic_marks > 100:
        print("Error: La calificación debe estar entre 0 y 100.")
        return
    
    # Determinar si está aprobado o reprobado
    if academic_marks >= 50:
        print("Aprobado")
    else:
        print("Reprobado")

# Función para calcular el promedio de las calificaciones
def calcular_promedio():
    # Solicito al usuario una lista de calificaciones
    academic_marks = input("Ingresa las calificaciones separadas por comas: ")
    
    # Convertir la entrada a una lista de números
    listAcademic_marks = [float(cal) for cal in academic_marks.split(",")]
    
    # Calcular el promedio
    grade_point_averege = sum(listAcademic_marks) / len(listAcademic_marks)
    print(f"El promedio de las calificaciones es: {grade_point_averege:.2f}")

# Función para contar las calificaciones mayores que un valor específico
def contar_calificaciones_mayores_que_valor():
    # Solicito al usuario una lista de calificaciones
    academic_marks = input("Ingresa las calificaciones separadas por comas: ")
    
    # Convertir la entrada a una lista de números
    listAcademic_marks = [float(cal) for cal in academic_marks.split(",")]
    
    # Solicito al usuario el valor de referencia
    value_of = float(input("Ingresa el valor numérico para comparar: "))
    
    # Contar cuántas calificaciones son mayores que el valor
    counter = sum(1 for cal in listAcademic_marks if cal > value_of)
    print(f"Hay {counter} calificaciones mayores que {value_of}.")

# Función para contar las calificaciones específicas
def contar_calificaciones_especificas():
    # Solicito al usuario una lista de calificaciones
    academic_marks = input("Ingresa las calificaciones separadas por comas: ")
    
    # Convertir la entrada a una lista de números
    listAcademic_marks = [float(cal) for cal in academic_marks.split(",")]
    
    # Solicito al usuario la calificación específica a contar
    academic_marks_specific = float(input("Ingresa la calificación que deseas contar: "))
    
    # Contar cuántas veces aparece la calificación específica
    counter = listAcademic_marks.count(academic_marks_specific)
    print(f"La calificación {academic_marks_specific} aparece {counter} veces en la lista.")

# Función principal para gestionar las opciones del menú
def main():
    print("Bienvenido al programa de calificaciones.")
    
    while True:
        # Mostrar menú de opciones
        print("\n¿Qué te gustaría hacer?")
        print("1. Determinar el estado de aprobación")
        print("2. Calcular el promedio de las calificaciones")
        print("3. Contar calificaciones mayores que un valor específico")
        print("4. Contar calificaciones específicas")
        print("5. Salir")
        
        # Pedir al usuario que elija una opción
        option = input("Elige una opción (1-5): ")
        
        # Ejecución según la opción seleccionada
        if option == '1':
            determinar_estado_aprobacion()
        elif option == '2':
            calcular_promedio()
        elif option == '3':
            contar_calificaciones_mayores_que_valor()
        elif option == '4':
            contar_calificaciones_especificas()
        elif option == '5':
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()

import zipfile
#elnombre del archivo .py y del .zip
nombre_archivo = "Gestiondecalificacion.py"
nombre_zip = "Gestiondecalificacion.zip"
# Crear un archivo zip
with zipfile.zipfile(nombre_zip, 'w' , zipfile.ZIP_DEFLATED) as zipf:
    # Agregar el archivo .py al zip
    zipf.write(nombre_archivo)
    print("archivo comprimido como entrega.zip")