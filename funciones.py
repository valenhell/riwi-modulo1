#solicitar los datos,da un rango de las calificaciones
def request_student_data():
    name = input("Enter the student's name: ")
    grade = []
    for i in range(1,6):
        grade = float(input(f"enter the grade {i} (of 1 to 5 ): "))
        grade.append(grade)
    return name,grade
#calcular el promedio
def calculate_average(grades):
    return sum(grades) / len(grades)
#determinar el estado de aprobacion
def show_results(name,average):
    if average >= 3:
        print(f"{name}is aproved with and avarange of {average:.2f}")
    else:
        print(f"{name} is disapproved with an average of {average:.2f}")
#funcion principal #el main es el punto de entrada del programa
def main():
    amount = int(input("how many students do you want to admit: "))
    for i in range(amount):
        name, grades = request_student_data()
        average = calculate_average(grades)
        show_results(name, average)
#ejecucion del programa
if __name__ == "__main__":
    main()