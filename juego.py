import random
jugada = input("Ingrese su jugada (piedra, papel o tijera):\n").lower()
opciones = ["piedra","papel","tijera"]
vs = random.choice(opciones)
if jugada in opciones:
    print(f"Tu jugaste {jugada}")
    print(f"Computador jugó {vs}")
    if jugada==vs:
        print("Es un empate.")
    elif (jugada=="piedra" and vs=="tijera") or (jugada=="tijera" and vs=="papel") or (jugada=="papel" and vs=="piedra"):
        print("Ganaste!!")
    else:
        print("Perdiste.")
        
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")