def c1(EFI):
    if EFI<0:
        return True
    else:
        return False
def c2(MI):
    if MI<13:
        return True
    else:
        return False
def c3(SLI):
    if SLI<1530:
        return True
    else:
        return False
def c4(BI):
    if BI<15.5:
        return True
    else:
        return False
def c5(RC):
    if RC>5:
        return True
    else:
        return False
def c6(PI):
    if PI<79:
        return True
    else:
        return False
def c7(LDI):
    if LDI>0:
        return True
    else:
        return False
def c8(EFI,MI,SLI,BI,RC,PI,LDI):
    L=[c1(EFI),c2(MI),c3(SLI),c4(BI),c5(RC),c6(PI),c7(LDI)]
    c=0
    for i in L:
        if i is True:
            c=c+1
    if c>=5:
        return True
    else:
        return False
def c9(EFI,MI,SLI,BI,RC,PI,LDI):
    L=[c1(EFI),c2(MI),c3(SLI),c4(BI),c5(RC),c6(PI),c7(LDI)]
    c=0
    for i in L:
        if i is True:
            c=c+1
    print(c,"/7")
    
mcv=float(input('MCV:'))
rbc=float(input('RBC: without x10^6'))
hb=float(input('hb:'))
mch=float(input('mch:'))
rdw=float(input('rdw:'))

EFI=(mcv-rbc-(5*hb)-3.4)    #1
MI=mcv/rbc                  #2
SLI=(((mcv)**2)*mch/100)    #3
BI=rdw                      #4
RC=rbc                      #5
PI=mcv                      #6
LDI=1.39*rbc-0.3*rdw-3.28   #7

print("----------------------------------------")

print("EFI:",end='')
print(EFI)
if c1(EFI):
    print("Significant")
else:
    print("Not Significant")
print("----------------------------------------")

print("MI:",end='')
print(MI)
if c2(MI):
    print("Significant")
else:
    print("Not Significant")
print("----------------------------------------")

print("SLI:",end='')
print(SLI)
if c3(SLI):
    print("Significant")
else:
    print("Not Significant")
print("----------------------------------------")

print("BI:",end='')
print(BI)
if c4(BI):
    print("Significant")
else:
    print("Not Significant")
print("----------------------------------------")

print("RC:",end='')
print(RC," x 10^6")
if c5(RC):
    print("Significant")
else:
    print("Not Significant")
print("----------------------------------------")

print("PI:",end='')
print(PI)
if c6(PI):
    print("Significant")
else:
    print("Not Significant")
print("----------------------------------------")

print("LDI:",end='')
print(LDI)
if c7(LDI):
    print("Significant")
else:
    print("Not Significant")
print("----------------------------------------")



if c8(EFI,MI,SLI,BI,RC,PI,LDI):
    print("HPLC advised")
else:
    print("HPLC NOT advised")

c9(EFI,MI,SLI,BI,RC,PI,LDI)


