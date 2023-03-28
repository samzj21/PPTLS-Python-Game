import random as ra   
opciones = ["piedra", "papel", "tijeras", "lagarto", "spock"]
valid = True
jugadas = 0
empate = 0
ganadas = 0
perdidas = 0
totalg = 0
totalp = 0
print("Bienvenido a piedra, papel, tijeras, lagarto o spock versión 3 de 5")
while valid: 
    print("\nPor favor ingrese una de las siguientes opciones: ") 
    for i in opciones:
        print(i)
        
    op_usuario = input("Tu selección es: ").lower()
    if op_usuario not in opciones:
        print("\nPor favor ingrese una opción válida.")
        continue
    
    op_computadora = ra.choice(opciones)
    print(f"La computadora seleccionó: {op_computadora}")

    if op_usuario == op_computadora:
        empate = empate + 1
        print(f"\nEmpate!, ambos eligieron {op_usuario}")
        
    elif op_usuario == "tijeras" and op_computadora == "papel":
        print(f"\nGanaste!, {op_usuario} corta {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "papel" and op_computadora == "piedra":
        print(f"\nGanaste!, {op_usuario} cubre {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "piedra" and op_computadora == "lagarto":
        print(f"\nGanaste!, {op_usuario} aplasta {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "lagarto" and op_computadora == "spock":
        print(f"\nGanaste!, {op_usuario} envenena a {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "spock" and op_computadora == "tijeras":
        print(f"\nGanaste!, {op_usuario} rompe {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "tijeras" and op_computadora == "lagarto":
        print(f"\nGanaste!, {op_usuario} decapita {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "lagarto" and op_computadora == "papel":
        print(f"\nGanaste!, {op_usuario} come al {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "papel" and op_computadora == "spock":
        print(f"\nGanaste!, {op_usuario} desautoriza a {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "spock" and op_computadora == "piedra":
        print(f"\nGanaste!, {op_usuario} vaporiza {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_usuario == "piedra" and op_computadora == "tijeras":
        print(f"\nGanaste!, {op_usuario} aplasta {op_computadora}")
        ganadas = ganadas + 1
        
    elif op_computadora == "tijeras" and op_usuario == "papel":
        print(f"\nPerdiste!, {op_computadora} corta {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "papel" and op_usuario == "piedra":
        print(f"\nPerdiste!, {op_computadora} cubre {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "piedra" and op_usuario == "lagarto":
        print(f"\nPerdiste!, {op_computadora} aplasta {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "lagarto" and op_usuario == "spock":
        print(f"\nPerdiste!, {op_computadora} envenena a {op_usuario}")
        perdidas = perdidas + 1     
        
    elif op_computadora == "spock" and op_usuario == "tijeras":
        print(f"\nPerdiste!, {op_computadora} rompe {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "tijeras" and op_usuario == "lagarto":
        print(f"\nPerdiste!, {op_computadora} decapita {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "lagarto" and op_usuario == "papel":
        print(f"\nPerdiste!, {op_computadora} come al {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "papel" and op_usuario == "spock":
        print(f"\nPerdiste!, {op_computadora} desautoriza a {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "spock" and op_usuario == "piedra":
        print(f"\nPerdiste!, {op_computadora} vaporiza {op_usuario}")
        perdidas = perdidas + 1
        
    elif op_computadora == "piedra" and op_usuario == "tijeras":
        print(f"\nPerdiste!, {op_computadora} aplasta {op_usuario}")
        perdidas = perdidas + 1

    if perdidas == 3:
        print("\n¡Has perdido el 3 de 5!")
        print(f"Conteo de derrotas: {perdidas}")
        print(f"Conteo de empates: {empate}")
        print(f"Conteo de victorias: {ganadas}")
        empate = 0
        ganadas = 0
        perdidas = 0
        totalp = totalp + 1
    elif ganadas == 3:
        print("\n¡Has ganado el 3 de 5!")
        print(f"Conteo de victorias: {ganadas}")
        print(f"Conteo de empates: {empate}")
        print(f"Conteo de derrotas: {perdidas}")
        empate = 0
        ganadas = 0
        perdidas = 0
        totalg = totalg + 1
        
    finalizar = input("\n¿Deseas jugar de nuevo?: ").lower()
    if finalizar == "no" or finalizar == "n":
        jugadas = jugadas + 1
        print(f"\nJugaste: {jugadas} veces en la ronda")
        print(f"Ganaste: {ganadas} veces en la ronda")
        print(f"Empataste: {empate} veces en la ronda")
        print(f"Perdiste: {perdidas} veces en la ronda")
        print(f"Ganaste en total: {totalg} veces en este juego")
        print(f"Perdiste en total: {totalp} veces en este juego")
        print("Fin del juego")
        valid = False
    elif finalizar == "si" or finalizar == "s":
            jugadas = jugadas + 1
            print(f"\nVeces jugadas: {jugadas} veces esta ronda")
            print(f"Has empatado: {empate} veces esta ronda")
            print(f"Has ganado: {ganadas} veces esta ronda")
            print(f"Has perdido: {perdidas} veces esta ronda")
            print(f"Has ganado en total: {totalg} veces en este juego")
            print(f"Has perdido en total: {totalp} veces en este juego")
            valid = True
        
