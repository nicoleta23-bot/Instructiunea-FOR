"""Să se calculeze sumele: 	s1=1+2+3+…+n
			s2=1*2+2*3+3*4+…+(n-1)*n
			s3=1+1*2+1*2*3+…+1*2*3*…*n
			s4=12+22+32+…+n2
			s5=1/2+2/3+3/4+…+n/(n+1)
			s6=1+2+22+23+24+…+2n
			Notă: Pentru fiecare sumă n – se va citi de la tastatură"""

n1=int(input("dati numarul n1:"))
s1=0
for i in range(1,n1+1):
    s1+=i
print("s1=",s1)

n2=int(input("dati numarul n2:"))
s2=0
for i in range(2,n2+1):
    s2+=(i-1)*i
print("s2=",s2)

n3=int(input("dati numarul n3:"))
s3=0
for i in range(1,n3+1):
    p=1
    for n in range(1,i+1):
        p*=n
    s3+=p
print("s3=",s3)

n4=int(input("dati numarul n4:"))
s4=0
for i in range(1,n4+1):
    s4+=i*10+2
print("s4=",s4)

n5=int(input("dati numarul n5:"))
s5=0
for i in rance(1,n5+1):
    s5+=n/(n+1)
print("s5=",s5)

n6=int(input("dati numarul n6:"))
s6=0
for i in rance(2,n6+1):
    if i<10:
        s6+=20+i
    else:
        s6+=20*(10**(i//10))+i
 print("s6=",s6)       