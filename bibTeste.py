import random

def menuDoJogo (): #Menu principal
    print ("\n================= Bem vindo ao jogo SENHA! =================")
    print ("{0:^60}".format("Diogenes Chagas"), end = "\n")
    print ("{0:^60}".format("Filipe Mei"), end = "\n")
    print ("\nA) INICIAR JOGO")
    print ("B) REGRAS DO JOGO\n")

def menuDeInstrucoes (): #Menu regras
    print ("\n================== Regras do jogo SENHA! ===================")
    print ("{0:^60}".format("Diogenes Chagas"), end = "\n")
    print ("{0:^60}".format("Filipe Mei"), end = "\n")
    print ("\n1) São necessários 2 (dois) jogadores;")
    print ("2) Seis cores estão disponíveis para a formação das senhas\n   (VERMELHO, AZUL, PRETO, BRANCO, AMARELO e VERDE);")
    print ("3) Cada jogador terá no máximo 6 chances para adivinhar a \n   senha escolhida pelo computador;")
    print ("4) O jogador que adivinhar primeiro a senha será o vencedor.\n   Caso nenhum deles acerte a combinação, vencerá aquele que\n   tiver a maior soma de pontos;")
    print ("5) Cada acerto parcial dá ao jogador 3 pontos, e cada acerto\n   total vale 7 pontos.\n")

def senhaMestra (cores, elementos): #A função random selecionara quatro elementos de cores sem que haja repetição
    senha = random.sample (cores, elementos) 
    return senha

def validaCorLista (lista, cor): #Funçao que testa se a cor e valida, ou seja, se ela esta na lista
    cor = str.upper(cor)
    if (cor in lista):
        return True
    else:
        return False
   
def acertosParciais (listaJogador, listaSenha): #Funçao que calcula o numero de cores que o jogador acertou gerando assim a pontuaçao
    acertosParciais = len(set(listaJogador).intersection(listaSenha)) #o comando 'intersection' compara as listas e retorna a quantidade de elementos iguais
    acertosReais = acertosParciais - acertosTotais (listaJogador, listaSenha) #retorna os acertos parciais reais 
    return acertosReais

def acertosTotais (listaJogador, listaSenha): #Calcula a quantidade de acertos totais
    acertosTotais = 0
    for i in range (len(listaSenha)): 
        if (listaJogador[i] == listaSenha[i]): #Compara elementos de mesma posiçao em cada uma das duas listas (escolha do jogador e senha gerada)
            acertosTotais += 1
    return acertosTotais #Retorna a quantidade de elementos que estao na mesma posiçao e que tem a mesma cor

def acertosPontuacao (acerto, valor): #Calcula a pontuaçao dos acertos parciais e totais
    if (acerto == 0):
        return 0
    else:
        return acerto * valor

def transformaLista (lista): # Transforma a lista em 'string' para gerar o tabuleiro
    virgula = ", "
    palavra = virgula.join (lista)
    return palavra

def tabuleiro (lista): #Funçao que gera o tabuleiro 
    indice = ["JOGADOR", "JOGADAS ANTERIORES", "A.P.", "A.T.", "PONTOS"] # Indice do tabuleiro
    print ("{0:^10}{1:^35}{2:^10}{3:^10}{4:^10}".format(indice[0],indice[1],indice[2],indice[3],indice[4]), end = "\n") #Formataçao do indice
    for conjunto in lista: #Para formatar e exibir a lista corretamente (Sem os colchetes)
        for elemento in conjunto: #extrai os elemetos da lista
            elemento = str(elemento)
            if (len(elemento) < 10): #formata elementos dependendo de seu tamanho
                print ("{0:^10}".format(elemento), end = "") #{0:^10} 0 - Elemento; ^ - Centralizar; 10 - Tamanho da celula
            else:
                print ("{0:^35}".format(elemento), end = "")
        print (end = "\n") #Pular linha para a nova adiçao de elementos de forma correta
