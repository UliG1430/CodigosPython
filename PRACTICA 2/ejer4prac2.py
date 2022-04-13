
def evaluar_titulo(evaluar):
    evaluar= evaluar.replace("titulo:","")
    palabras_titulo= len(evaluar.split())
    if (palabras_titulo>10):
        return False
    else:
        return True

def evaluar_resumen (resumen):
    evaluaciones= {"faciles de leer":0,"aceptable para leer":0, "dificil de leer":0, "muy dificil":0}
    resumen= resumen.split(".")
    for i in resumen:
        oracion=i
        if not oracion:
            continue
        cantidad= (len(oracion.split()))
        match cantidad:
            case cantidad if (0 < cantidad <= 12):
                evaluaciones["faciles de leer"]+=1
            case cantidad if (13 <= cantidad <= 17):
                evaluaciones["aceptable para leer"]+=1
            case cantidad if (18 <= cantidad <= 25):
                evaluaciones["dificil de leer"]+=1
            case cantidad if (cantidad > 25):
                evaluaciones["muy dificil"]+=1
    return evaluaciones

evaluar=""" titulo: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures."""
lista=evaluar.split('resumen:')
titulo=lista[0]
resumen=lista[1]
cumple_titulo=evaluar_titulo(titulo)
evaluaciones=evaluar_resumen(resumen)
if (cumple_titulo):
    print ("TITULO: CUMPLE")
else:
    print ("TITULO: NO CUMPLE")
print (evaluaciones)