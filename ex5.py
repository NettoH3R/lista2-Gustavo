player1 = int(input("jogador 1 \n1.pedra \n2.papel \n3.tesoura \nEscolha uma opção: "))
player2 = int(input("\njogador 2 \n1.pedra \n2.papel \n3.tesoura \nEscolha uma opção:: "))

if ((player1 == 1) and (player2 == 3)) or ((player1 == 2) and (player2 == 1)) or ((player1 == 3) and (player2 == 2)):
    print ('O jogador 1 é o vencedor')
else:
    print ('O jogador 2 é o vencedor')