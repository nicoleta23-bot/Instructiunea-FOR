#Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele impare, pentru intervalul de la a la b (a și b se citesc de la tastatură).
a=int(input("dati numarul a="))
b=int(input("dati numarul b="))
if a%2==0:
    for n in range(a+1,b,2):
        print(n,end=" ")
else:
    for n in range(a,b,2):
        print(n,end=" ")
