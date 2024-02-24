w = float(input("Ingrese el peso de la persona en Kg:\n"))
h = float(input("Ingrese la altura en centimetros:\n"))
if w<=0 or h<=0:
    print("Los valores ingresados no pueden ser 0")
else:
    #imc = w/((h/100)**2)
    imc = w/pow(h/100,2)
    clasificacion=""
    if imc<18.5:
        clasificacion="Bajo Peso"
    elif imc>=18.5 and imc<=25:
        clasificacion="Adecuado"
    elif imc>25 and imc<=30:
        clasificacion="Sobrepeso"
    elif imc>30 and imc<=35:
        clasificacion="Obesidad Ggrado I"
    elif imc>35 and imc<=40:
        clasificacion="Obesidad Ggrado II"
    else:
        clasificacion="Obesidad Ggrado III"
    print(f"Su IMC es {imc:.2f}")
    print(f"La clasificación OMS es {clasificacion}")
