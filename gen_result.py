import sys, csv
from subprocess import *

kernel_number = (1, 2, 3 ,4, 5, 6, 7, 8, 9)

tabla=[]
tabla.append(["","Fallos en bifurcaciones","Bifurcaciones"])

for i in kernel_number:
    print("Compilando version {0}...".format(i))
    if (call("gcc -O0 -o branch{0} branch{1}.c".format(i,i), shell=True)==-1):
      print("Ha ocurrido un error durante la compilacion")
      sys.exit(0)


    print("Ejecutando version {0}...".format(i))
    texto=Popen("sudo perf stat  -e instructions:u,branch-misses:u,branches:u ./branch{0}".format(i), shell=True,stderr=PIPE,stdout=PIPE).communicate()[1].split("\n")
    tabla.append(["branch{0}".format(i),texto[4].split()[0],texto[5].split()[0]])

print("Generando fichero...")
with open("bifurcaciones.csv","wb") as f:
    writer=csv.writer(f)
    writer.writerows(tabla)

print("Listo!")
