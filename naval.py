import random

# Functions
###################################################################################################################
def print_map(matriz):  # Printa a matriz enquanto o mapa do jogador é montado
    print("\tx 0\t1\t2\t3\t4\t5")   #referencia das colunas
    print("y\t-------------------------------------------") #Deixar bonito <3
    for i in range(0,linhas):
        print("\n")
        print(i, end="")    # Referencia das linhas
        print("|", end="")
        for j in range(0,colunas):
            print("\t", end=" ")
            print(matriz[i][j], end="") # Numeros na matriz # 0 = vazio # 1 = ocupado
    print("\n") # pula linha
    return

def validacao(matriz,x,y,tam,orientacao):   # Verifica se nao ha nenhum navio no espaco que o novo navio ocupará
    
    if(orientacao == 1):    # Navio na vertical
        for i in range(y, y+tam):   # Percorrer o espcao que o navio vai ocupar
            if(matriz[i][x] == 1):  # 1 = ocupado # Da mesma forma qu ena linha 14
                return 0    # sai da funcao e retorna zero
    
    if(orientacao == 2):    # Mesma coisa na Horizontal
        for i in range(x, x+tam):
            if(matriz[y][i] == 1):
                return 0
    
    return 1    # Se a funcao chega ate aqui significa que nao ha nenhum navio no espaco que o novo navio ocupará
###################################################################################################################
print("      _\n                    | \ \n                     '.|\n     _-   _-    _-  _-||    _-    _-  _-   _-    _-    _-\n       _-    _-   - __||___    _-       _-    _-    _-\n    _-   _-    _-  |   _   |       _-   _-    _-\n      _-    _-    /_) (_) (_\        _-    _-       _-\n              _.-'           `-._      ________       _-\n        _..--`                   `-..'       .'\n    _.-'  o/o                     o/o`-..__.'        ~  ~\n .-'      o|o                     o|o      `.._.  // ~  ~\n `-._     o|o    BATALHA NAVAL     o|o        |||<|||~  ~\n     `-.__o\o                     o|o       .'-'  \\ ~  ~\n          `-.______________________\_...-``'.       ~  ~\n                                    `._______`.\n\n\n")

# Main
###################################################################################################################

linhas = 6
colunas = 6
ganhou = 16

r = input("Digite 'r' para ver as regras ou 'c' para continuar")
if(r == 'r' or r == 'R'):
    print("\n\t\tREGRAS:\n\t1- MONTAGEM DO MAPA\n\tEscolha uma peca pelo seu nome. Informe se ela estara de pe ou deitada. E suas coordenadas.\n\t2- JGOUE\n\tInforme as coordenadas do seu chute.")

# MONTAGEM DO MAPA DO JOGADOR
######################################################################
mapa_player=[[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]  # Matriz 6x6
pecas={"sub1": 2, "sub2": 2, "contra": 3, "navio": 4, "porta": 5}   # Pecas : Tamanho


while(len(pecas) != 0): # Enquanto houver peças na lista
####INICIO DO LOOP    
    print_map(mapa_player)
    print(pecas)

    peca_atual = input("Informe o nome da peca que sera inserida\n")    # Nome da peca
    if(not pecas.get(peca_atual)):  # Verifica se o nome da peca esta correto
        print("Peca invalida!")
        continue    #volta para o inicio do loop

    orientacao = int(input("1-Vertical | 2-Horizontal\n"))  # Peca em pé ou deitada
    if(orientacao<1 or orientacao>2):   # verifica se nao é um numero aleatorio
        print("Opcao invalida!")
        continue    #volta para o inicio do loop

    y = int(input("Informe o y da peca (0-5)\n"))
    if(y<0 or y>5): # verifica se esta no range da matriz
        print("Valor fora do tabuleiro!")
        continue    #volta para o inicio do loop

    x = int(input("Informe o x da peca (0-5)\n"))
    if(x<0 or x>5): # verifica se esta no range da matriz
        print("Valor fora do tabuleiro!")
        continue    #volta para o inicio do loop

    if(orientacao == 2 ):   # CASO HORIZONTAL
        i=x # Começo do navio
            #verifica se nao sai do tabuleiro      #funcao defina na linha 5
        if(x+pecas.get(peca_atual) <= linhas and validacao(mapa_player,x,y,pecas.get(peca_atual),orientacao)==1):
            for i in range(i,x+pecas.get(peca_atual)):  # Percorre o tamanho da peca
                mapa_player[y][i] = 1    # y = linha fixo   # Muda status da casa no tabuleiro para ocupado = 1
            del pecas[peca_atual]   # Deleta peca da lista
        else:
            print("A peca nao cabe no espaco desejado!")

    elif(orientacao == 1 ): #CASO VERTICAL
        i=y

        # Mesma coisa do anterior mas com y no lugar de x

        if(y+pecas.get(peca_atual) <= colunas and validacao(mapa_player,x,y,pecas.get(peca_atual),orientacao==1)):
            for i in range(i,y+pecas.get(peca_atual)):
                mapa_player[i][x] = 1    # x = coluna fixo
            del pecas[peca_atual]
        else:
            print("A peca nao cabe no espaco desejado!")
    
print("\n\n\n\n\n\t\tSEU MAPA ESTA PRONTO!\n\n\n")
print_map(mapa_player)
######################################################################



# MONTAGEM DO MAPA DA IA
######################################################################
mapa_ia=[[0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]]  # Matriz 6x6
pecas={"sub1": 2, "sub2": 2, "contra": 3, "navio": 4, "porta": 5}   # Pecas : Tamanho

while(len(pecas) != 0): # Enquanto houver peças na lista
    val = random.randint(2,5)   # Gera numero no range do tamanho dos navios
    flag = 0    # Parar o loop que gera x e y

    if(val in pecas.values()):
        peca_atual = list(pecas.keys())[list(pecas.values()).index(val)]    # Pega o nome do navio pelo seu valor (tamanho)
        orientacao = random.randint(1,2)    #vertical|horizontal

        while(flag != 1 and orientacao == 1):    # Vertical
            x = random.randint(0, 5)            # gera x
            y = random.randint(0, linhas-val)   # gera y de forma que o navio caiba no espaco
            if(validacao(mapa_ia, x, y, pecas.get(peca_atual), orientacao)):    # verifica se nao ha navios no caminho
                flag = 1
                for i in range(y,y+pecas.get(peca_atual)):
                    mapa_ia[i][x] = 1    # x = coluna fixo
                del pecas[peca_atual]

        while(flag != 1 and orientacao == 2):    # Horizontal
            y = random.randint(0, 5)
            x = random.randint(0, colunas-val)
            if(validacao(mapa_ia, x, y, pecas.get(peca_atual), orientacao)):
                flag = 1
                for i in range(x,x+pecas.get(peca_atual)):  # Percorre o tamanho da peca
                    mapa_ia[y][i] = 1    # y = linha fixo   # Muda status da casa no tabuleiro para ocupado = 1
                del pecas[peca_atual]   # Deleta peca da lista
  
######################################################################


# JOGO
######################################################################
mapa_disp = [['/','/','/','/','/','/'],
        ['/','/','/','/','/','/'],
        ['/','/','/','/','/','/'],
        ['/','/','/','/','/','/'],
        ['/','/','/','/','/','/'],
        ['/','/','/','/','/','/']]

pontos_player=0
pontos_ia=0


while(ganhou - pontos_ia > 0 and ganhou - pontos_player > 0):   # Se algum chegar a 0 todos os navios form afundados
    flag = False    # Verifica se a jogada foi valida
    print("\n\t\t\tPontos player:", pontos_player)
    print("\n\t\t\tPontos ia:", pontos_ia)
    print_map(mapa_disp)

    

    # TURNO DO JOGADOR
    while(not flag):
        x=-1
        y=-1
        while(not(0 <= x <= 5) or not(0 <= y <= 5)): # Verifia o range
            y = int(input("Informe o y da peca (0-5)\n"))
            x = int(input("Informe o x da peca (0-5)\n"))

        if(mapa_disp[y][x] == '/'): # Verifica se a casa ja nao foi chutadada
            flag = True # Jogada valida
            if(mapa_ia[y][x] == 1): #atinge navio
                print("\n\n\n\n\n\n\tNAVIO ATINGIDO!!\n\n\n\n")
                mapa_disp[y][x] = '*'
                pontos_player = pontos_player +1    #marca ponto
            else:   #atinge agua
                print("\n\n\n\n\n\n\t~Agua~~~~\n\n\n\n")
                mapa_disp[y][x] = '~'
            if(pontos_player == ganhou):
                print("\n\n\n\n\n\n\n\n\n\n\t\tPARABENS VOCE GANHOU!!!!!!!!!")
                break
        else:
            print("\n\n\n\n\n\n\n\n\tLOCAL INVALIDO!!\n\n\n")
    flag = False
    
    #TURNO DA IA
    while(not flag):
        y = random.randint(0, 5)
        x = random.randint(0, 5)
        if(mapa_player[y][x] != 'X'):
            flag = True
            if(mapa_ia[y][x] == 1):
                print("\n\n\n\n\n\n\tNAVIO ATINGIDO!!\n\n\n\n")
                mapa_player[y][x] = 'X'
                pontos_ia = pontos_ia +1
            else:
                print("\n\n\n\n\n\n\t~Agua~~~~\n\n\n\n")
                mapa_player[y][x] = 'X'
            if(pontos_ia == ganhou):
                print("\n\n\n\n\n\n\n\n\n\n\t\tPARABENS VOCE PERDEU!!!!!!!!!")
                break

######################################################################

###################################################################################################################