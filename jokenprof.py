import random
from time import sleep

def tesoura():    
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


def pedra():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

def papel():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

def mostraJogada(player, maquina):
    print("\n\nVocê: ")
    if player == 0:
        pedra()
    elif player == 1:
        papel()
    else: 
        tesoura()
    print("\nMáquina: ")
    sleep(0.5)
    if maquina == 0:
        pedra()
    elif maquina == 1:
        papel()
    else:
        tesoura()

def mostraPlacar(placar):
    print(f"Vitórias: {placar[0]}\nDerrotas: {placar[1]}\nEmpates: {placar[2]}")


def jokenpo(player, maquina, placar):
    
    if player == maquina:
        placar[2] += 1
    elif player == 0 and maquina == 1 or player == 1 and maquina == 2 or player == 2 and maquina == 0:
        placar[1] += 1
    else:
        placar[0] += 1
    
 
            

#A lista placar é: Vitórias, Derrotas, Empates
placar = [0,0,0]
gameOn = "sim"
# loop do jogo 
while gameOn.lower() == "sim":
    
    maquina = random.randint(0,2)
    player = 5 
    
    while player > 2 or player < 0: # se a jogada nao cair dentro de um dos valores válidos, o programa pede novamente
        player = int(input("escolha sua jogada: pedra(0), papel(1) ou tesoura (2): "))
        
    mostraJogada(player,maquina)
    jokenpo(player, maquina, placar)
    mostraPlacar(placar)
    
    gameOn = input("voce quer que o jogo continue?: ")
    if not gameOn.lower() == "sim":
        print("jogaremos outra vez")
    