from random import randint

def menu():
    opcao = int(input("Digite 1 para Humano X Humano, 2 para Humano X Computador e 3 para Computador X Computador "))

    if opcao==2:
        return jogoHxC()
    elif opcao==3:
        return jogoCxC()



def jogoCxC():
    pontuacaoC1=0
    pontuacaoC2=0
    while pontuacaoC1 <= 3 or pontuacaoC2 <= 3:
        computador1=(randint(1,3))
        computador2=(randint(1,3))
        if computador1==1 and computador2==2:
            print("Computador venceu")
            pontuacaoC = pontuacaoC+1
        elif computador1==2 and computador2==3:
            print("Computador venceu")
            pontuacaoC = pontuacaoC+1
        elif computador1==3 and computador2==1:
            print("Você venceu!!!!!")
            pontuacaoH = pontuacaoH+1
        elif computador1==1 and computador2==3:
            print("Você venceu!!!!!")
            pontuacaoH = pontuacaoH+1
        elif computador1==2 and computador2==1:
            print("Você venceu!!!!!")
            pontuacaoH = pontuacaoH+1
        elif computador1==3 and computador2==2:
            print("Computador venceu")
            pontuacaoC = pontuacaoC+1
    if pontuacaoH==3:
        print("Parabens!!!!!!!!")
        print("Fim de jogo")







def jogoHxC():
    pontuacaoH=0
    pontuacaoC=0
    while pontuacaoH <= 3 or pontuacaoC <= 3:
        PPT = int(input("Escolha 1 para Pedra, 2 para papel e 3 para tesoura"))
        computador=(randint(1,3))
        if PPT==1 and computador==2:
            print("Computador venceu")
            pontuacaoC = pontuacaoC+1
        elif PPT==2 and computador==3:
            print("Computador venceu")
            pontuacaoC = pontuacaoC+1
        elif PPT==3 and computador==1:
            print("Você venceu!!!!!")
            pontuacaoH = pontuacaoH+1
        elif PPT==1 and computador==3:
            print("Você venceu!!!!!")
            pontuacaoH = pontuacaoH+1
        elif PPT==2 and computador==1:
            print("Você venceu!!!!!")
            pontuacaoH = pontuacaoH+1
        elif PPT==3 and computador==2:
            print("Computador venceu")
            pontuacaoC = pontuacaoC+1
    if pontuacaoH==3:
        print("Parabens!!!!!!!!")
        print("Fim de jogo")
    else:
        print("Sinto muito, o PC eh superior nessa arte")
        print("Fim de jogo")
