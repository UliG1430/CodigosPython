def abrir_archivos():
    anombres=open ("nombres_1.txt","r", encoding="UTF-8")
    aeval1=open("eval1.txt","r", encoding="UTF-8")
    aeval2=open("eval2.txt","r", encoding="UTF-8")
    return anombres,aeval1,aeval2

def limpiar_archivo (archivo):
    for i in range (0,len(archivo)) :
       archivo[i]=archivo[i].replace(",","")
            
    return archivo

promedio=[]
estructura={}
nombres,eval1,eval2=abrir_archivos()
nombres=nombres.read().split()
print(nombres)

eval1=eval1.read().split(",")
eval2=eval2.read().split(",")
#nombres=limpiar_archivo(nombres)
print(nombres)

for i in range (0,len(nombres)):
    suma=float(eval1[i])+float(eval2[i])
    estructura[nombres[i]]=suma
    promedio.append(suma/2)
print (promedio)

promedio=sum (promedio)/float(len(promedio))
print (f"PROMEDIO {promedio}")

for clave in estructura.keys():
    if (estructura[clave]/2<promedio):
        print (f"EL ALUMNO {clave} tuvo un prmedio de {estructura[clave]/2} por lo que no supero el promedio")
