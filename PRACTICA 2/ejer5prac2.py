from itertools import count


frase=str(input('INGRESE UNA FRASE: '))
palabra=str (input ('INGRESE LA PALABRA: '))
palabra=palabra.lower()
veces=frase.lower().count(palabra)
print (veces)