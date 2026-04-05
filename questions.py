import random
import string
import r

rounds = [
        {
         'theme': 'Entrada',
         'scores': {
                    'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                    'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                    'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                    'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
                    'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
                   }
        },
        {
         'theme': 'Plato principal',
         'scores': {
                    'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                    'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                    'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                    'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                    'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                   }
        },
        {
         'theme': 'Postre',
         'scores': {
                    'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                    'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                    'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                    'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
                    'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                   }
        },
        {
         'theme': 'Cocina internacional',
         'scores': {
                    'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
                    'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                    'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                    'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
                    'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
                   }
        },
        {
         'theme': 'Final libre',
         'scores': {
                    'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
                    'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
                    'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
                    'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                    'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
                   }
        }
]

total={'Valentina':{"puntaje":0,"ganadas":0,"mejor ronda":0,"promedio":0}
       ,'Mateo':{"puntaje":0,"ganadas":0,"mejor ronda":0,"promedio":0}
       ,'Camila':{"puntaje":0,"ganadas":0,"mejor ronda":0,"promedio":0}
       ,'Santiago':{"puntaje":0,"ganadas":0,"mejor ronda":0,"promedio":0}
       ,'Lucía':{"puntaje":0,"ganadas":0,"mejor ronda":0,"promedio":0}
       }
i=0
for elem in rounds:
    user=rounds[i]
    participante=user['scores']
    ganador=["",0]
    ronda_total=0
    maxi=0
    for elem in user['scores']:
        #
        ronda_total=r.puntos(ronda_total,participante[elem])

        total[elem]["puntaje"]+=ronda_total
        #
        maxi=r.maximo(ronda_total,elem,maxi,ganador)
        r.mejor_ronda(total,elem,ronda_total)
        ronda_total=0

    total[ganador[0]]["ganadas"]+=1
    print(f"Ronda {i+1} - {user['theme']} :")
    print(f"    Ganador: {ganador[0]} ({ganador[1]} pts)")
    total=r.tabla(total)
    print()
    i+=1
    
r.sacar_promedio(total)

print(f"Participante    {"   ".join(total['Valentina'])}")
print("-----------------------------------------------------------")
for elem in total:
    print(f"{elem:<9}{r.dic(total[elem])}")
print("-----------------------------------------------------------")