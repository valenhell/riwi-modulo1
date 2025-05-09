#guess the number game
#ejercicio 1
print("\nwelcome to the number guessing game")
def guess_the_number():
    #difinicion de funcion
    number_secret = 7
    attempts = 0
    #usamos while para que el juego continue hasta que el usuario adivine el numero
    while True:
        try:
            #try-except para capturar entradas no numericas
            guess = int(input("guess a number between 1 and 10: "))
            attempts += 1
            if guess < 1 or guess > 10:
                print("please enter a number between 1 and 10")
            elif guess == number_secret:
                print(f"congratulations! you guessed the number in {attempts} attempts")
                break
            #ponemos break para salir del bucle
            else:
                print("try again")
        except ValueError:
            print("please enter a valid number")
guess_the_number()