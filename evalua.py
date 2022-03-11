import sys
import csv
import numpy as np

filename = sys.argv[1]
header={
        'date':0,
        'eval':1,
        'title':2,
        'claridad':6,
        'conclusiones':7,
        'originalidad':3,
        'creatividad':4,
        'exposición':5,
        'complejidad':11,
        'calculos':12,
        }
#dict con trabajos y calificaciones
datos={}
#dict con número de evaluaciones para cada trabajo
ncal={}
with open(filename) as ifile:
    filereader=csv.reader(ifile)
    for i,line in enumerate(filereader):
        if i <1:
            continue
        calif=[int(line[header['claridad']])*0.30,
                int(line[header['conclusiones']])*0.20,
                int(line[header['originalidad']])*0.10,
                int(line[header['creatividad']])*0.10,
                int(line[header['exposición']])*0.10,
                int(line[header['complejidad']])*0.10,
                int(line[header['calculos']])*0.10,
                ]
        if line[header['title']] in datos.keys():
            datos[line[header['title']]]+=np.array(calif)
            ncal[line[header['title']]]+=1
        else:
            datos[line[header['title']]]=np.array(calif)
            ncal[line[header['title']]]=1
final={}
with open("resultados.csv",'w') as ofile:
    print('Trabajo, calificación, promedio por rubro, evaluaciones'); 
    print('Trabajo, calificación, promedio por rubro, evaluaciones', file=ofile); 
    for w in datos:
        cal =np.sum(datos[w])/ncal[w]
        final[cal]=w
        print('"'+w+'"', cal, datos[w], ncal[w], sep=',', file=ofile)

print('final1')
print(final)

ordena=sorted(list(final.keys()))
ordena.reverse()
print(ordena)
with open("ordenados.csv",'w') as ofile:
    print('Trabajo, calificación', file=ofile); 
    for w in ordena:
        print(w)
        print('"'+final[w]+'"', w, sep=',', file=ofile)
        final.pop(w)
    
