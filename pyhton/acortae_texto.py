def acortar_texto () :
    """
    acorta un texto si excede la longitud maxima,añadiendo puntos suspensivos al final.
     args:
       texto(str) : cadena de texto a procesar.
      max_longitud(int): longitad maxima permitida para el texto resultante
     returns: str: texto original o version acortada con puntos suspensivos.
     """
    """""
    if len(texto) <= max_longitud:
        return texto
    else:
        #asegurarnos de dejar espacio para los tres puntoss susupensivos
        return texto[:max_longitud - 3] + "..."
    # ejemplo
    texto_largo = "este es un texto muy largo que necesita ser acortado para cumplir con los nummeros"
    print(acortar_texto(texto_largo,20))
    """""
    #programa principal que interactua con el usuario
    print("bienvenido al acortador de texto")
    print("_ _ _ _")
    while True:
     #solicitar texto al usurio
     texto = input("\nIngrese el texto que desea acortar (o salir para terminar): ")
     #opcion para salir del programa
     """""
     if texto.lower() == salir :
        print("¡hasta luego!") 
        break"""""
     
     #solicitar longitud maxima 
     while True:
        try:
          
           max_longitud = int(input("ingrese la longitud maxima deseada: "))
           
           if max_longitud < 3:
              print("la longitud minima dbe ser 3(para los puntos suspensivos)") 
              
           break
        
        except ValueError:
           print("por favor ingrese un numero valido.") 

           #acortar el texto y mostrar el resultado
           texto_acortado = acortar_texto(texto, max_longitud)
           print(f"texto acortado: {texto_acortado}")

acortar_texto()



