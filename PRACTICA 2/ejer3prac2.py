#3. Dado un texto solicite por teclado una letra e imprima las palabras que comienzan con dicha
#letra. En caso que no se haya ingresado una letra, indique el error. Ver: módulo string

from string import ascii_letters


text="""Un texto es una composición de signos codificados en un sistema de escritura que 
forma una unidad de sentido. También es una composición de caracteres imprimibles generados
 por un algoritmo de cifrado que, 
aunque no tienen sentido para cualquier persona, sí puede ser descifrado por su destinatario original"""

letra=str(input("INGRESE UNA LETRA: "))
text=text.lower().split()
if (letra in ascii_letters):
   for i in text:
        if (i.startswith(letra)):
            print (i)
else:
    print ("El caracter ingresado no es una letra")
