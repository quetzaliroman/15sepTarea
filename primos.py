print("*** Numeros primos ***")
rango = int(input("Hasta que numero quieres ver cuales son los numeros primos?: "))

for apu in range(2, rango + 1):
    primos = True
    for apu2 in range(2,apu):
        if apu == apu2:
           break
        elif apu%apu2 == 0:
           primos = False
        else:
           continue
    if primos == True:
        print(" ",apu, end=" ")
        
