import bibTeste #Importar biblioteca especifica para o jogo

#---------- VARIAVEIS PARA O CORRETO FUNCIONAMENTO DO JOGO ----------#

cores = ["AZUL", "AMARELO", "VERDE", "PRETO", "BRANCO", "VERMELHO"] #Elementos que podem participar da senha
quantElementosSenha = 4 #Quantidade de elementos para a senha

pontoParcial = 3
pontoTotal = 7

listaJogador = []
listaTabuleiro = []

rodadas = 6 #Quantidade de rodadas

contador = 0
pontuacaoJogador1 = 0
pontuacaoJogador2 = 0

menu = ["A","B"] #Opcoes do menu do jogo

condicao = "NONE"
idJogadores = [1, 2] #Quantidade de jogdores
sair = ["SAIR", "CONTINUAR"] #Condicoes especiais para o jogo

#---------- CRIACAO DA SENHA MESTRA ----------#

senha = bibTeste.senhaMestra (cores, quantElementosSenha) #Criacao da senha mestra

#---------- MENU DO JOGO ----------#

bibTeste.menuDoJogo () #Exibicao do menu principal do jogo
opcaoMenu = str.upper (input ("Informe qual opção você deseja: "))
while (opcaoMenu not in menu): #Verifica se a opcao escolhida e valida
    opcaoMenu = str.upper (input ("Opção inválida, informe qual opção você deseja: "))

while (opcaoMenu != menu[0]): #Testa a opcao escolhida pelo jogador, se for diferente da que inicia o jogo, ela exibira o menu de regras
    if (opcaoMenu == menu[1]):
        bibTeste.menuDeInstrucoes()
        opcaoMenu = str.upper (input ("Digite 'A' para iniciar o jogo: "))
        while (opcaoMenu not in menu): #Verifica se a opcao escolhida e valida
            opcaoMenu = str.upper (input ("Opçao invalida, digite 'A' para iniciar o jogo: "))

#---------- INICIO DO JOGO ----------#

print ("\n==================== Que vença o melhor! ===================")

while (contador < rodadas) and (condicao != sair[0]): #Quantidade de vezes que o programa deve rodar, determinado pela variavel 'rodadas' ou pela condica de saida
    for elementos in idJogadores: #Quantidade de jogadores determinada pela funcao idJogadores
        print ("\nRodada do jogador", elementos,)

        #---------- ESCOLHA DAS CORES (JOGADOR) ----------#

        jogador = elementos
        
        for i in range (quantElementosSenha):
            print ("\nVoce ja selecionou", i,"cores")
            escolhaCores = str.upper (input ("Jogador, por favor, digite a cor desejada: "))
            while (bibTeste.validaCorLista (cores, escolhaCores)== False): #Verifica se a ortografia da cor digitada esta correta
                escolhaCores = str.upper (input ("Cor invalida, por favor digite uma cor valida: "))
            while (bibTeste.validaCorLista (listaJogador, escolhaCores) == True): #Verifica se a cor esta disponivel na lista do jogador, caso nao esteja, esta condicao informa que ela ja foi escolhida 
                escolhaCores = str.upper (input ("Cor escolhida, por favor digite uma cor valida: "))
                while (bibTeste.validaCorLista (cores, escolhaCores)== False):
                    escolhaCores = str.upper (input ("Cor invalida, por favor digite uma cor valida: "))
            listaJogador.append (escolhaCores) #Adiciona as cores escolhidas na lista do jogador

        #---------- CONTABILIZACAO DOS PONTOS ----------#

        acertosParciais = bibTeste.acertosParciais (listaJogador, senha) #Contabiliza acertos parciais
        acertosTotais = bibTeste.acertosTotais (listaJogador, senha) #Contabiliza acertos totais
        pontuacaoParcial = bibTeste.acertosPontuacao (acertosParciais, pontoParcial) #Contabiliza pontos dos acertos parciais
        pontuacaoTotal = bibTeste. acertosPontuacao (acertosTotais, pontoTotal) #Contabiliza pontos dos acertos totais

        #---------- DIVISAO DOS PONTOS----------#

        if (elementos == idJogadores[0]): #Divisao de acordo com o jogador em questao
            pontuacaoJogador1 += pontuacaoParcial + pontuacaoTotal
            pontuacao = pontuacaoJogador1
        else:
            pontuacaoJogador2 += pontuacaoParcial + pontuacaoTotal
            pontuacao = pontuacaoJogador2

        #---------- CONDICAO ESPECIAL ----------#

        if (acertosTotais == quantElementosSenha): #Caso o jogador acerte a senha, o jogo ira adicionar a condicao de saida automaticamente, encerrando o jogo
            del idJogadores[1] #Caso seja acionada a condicao acima, o codigo ira remover a proxima jogada do jogador 2
            condicao = sair[0]
        
        print (end = "\n")

        #---------- FORMULACAO DAS TABELAS ----------#
        
        listaJogadorLetras = bibTeste.transformaLista (listaJogador) #Transforma a lista em string
        listaTabuleiro.append ([jogador, listaJogadorLetras, acertosParciais, acertosTotais, pontuacao]) #Lista para alimentar a funcao do tabuleiro, esta abaixo
        bibTeste.tabuleiro (listaTabuleiro) #Funcao geradora do tabuleiro
        
        listaJogador = [] #Zerar a lista para que haja a possibilidade de novas jogadas

    #---------- CONDICOES PARA SAIR DO JOGO ----------#

    if (contador != (rodadas - 1)): #Determina ate quando o menu de condicao de saida deve ser exibido
        if (condicao != sair[0]):
            condicao = str.upper (input ("\nDigite 'SAIR' se desejam sair do jogo, se não digite 'CONTINUAR': "))
        while (condicao not in sair): #Verifica se a ortografia da condicao digitada esta correta
            print ("\nERRO: Opção inválida, por favor escolha outra opção") 
            condicao = str.upper (input ("Digite 'SAIR' se desejam sair do jogo, se não digite 'CONTINUAR': "))

    contador += 1 #Contador para saber quantas rodadas ja se passaram

#---------- RESULTADOS FINAIS DO JOGO ----------#

if (pontuacaoJogador1 > pontuacaoJogador2):
    print ("\nRESULTADO FINAL: Jogador 1 venceu! Voce obteve", pontuacaoJogador1, "pontos.")
elif (pontuacaoJogador1 == pontuacaoJogador2):
    print ("\nRESULTADO FINAL: Empate! Os dois jogadores obtiveram", pontuacaoJogador1, "pontos.")
else:
    print ("\nRESULTADO FINAL: Jogador 2 venceu! Voce obteve", pontuacaoJogador2, "pontos.")
