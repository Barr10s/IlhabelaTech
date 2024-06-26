#NÃO CRIEI ESSE CÓDIGO!
#import random -- isso aqui eu inventei, para deixar o jogo mais randomizado, mas não consegui implementar
numero_secreto = 40
acertou = False

while not acertou:
    palpite = int(input("Digite um número: "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        acertou = True
    elif palpite < numero_secreto:
        print("O núnero secreto é maior. Tente novamente.")
    else:
        print("O número secreto é menor. Tente novamente.")

print("Fim do jogo")

