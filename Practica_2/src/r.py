def maximo (ronda,nom, max,ganador):
    if(ronda>max):
        ganador[0]=nom
        ganador[1]=ronda
    return ganador[1]

def puntos(ronda,participante):
    for elem in participante:
        ronda+=int(participante[elem])
    return ronda
        
def mejor_ronda(total,nom,ronda):
    if total[nom]["mejor ronda"] < ronda:
        total[nom]["mejor ronda"]=ronda 

    
def sacar_promedio(total):
    for elem in total:
        total[elem]["promedio"]=total[elem]["puntaje"]/5

def tabla(total):
    orden=dict(sorted(total.items(),key=lambda item:item[1]["puntaje"],reverse=True))
    print("    Posiciones: ")
    for elem in orden:
        print(f"               {elem} : {orden[elem]["puntaje"]}")
    return orden

def dic(diccionario):
    todo=""
    for elem in diccionario:
        todo+="         "+str(diccionario[elem])
    return todo

