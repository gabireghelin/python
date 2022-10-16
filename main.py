# TRABALHO ALGP02
# GABRIELA SCHMITT REGHELIN

import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''

for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '

for i in range(100):#imprimir todo o conteúdo da variável memória
  print (memoria[i], end="|")
  
while(opcao != 4):
    #Menu do programa
    print("\n\n1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()

    if(opcao == 1):# lógica da primeira escolha
      
      # testar e encontrar o primeiro lugar na memoria com espaços vazios suficientes
      
      indice = -1
      cont=0
      gravou = 0
      
      for i in range(100):
        
        if (memoria[i] == ' '): # se a celula for vazia
          
          if (cont == 0):
            indice = i # guardar qual o indice do primeiro espaco vazio
          
          cont +=1 # adicionar ao contador do numero de celulas vazias
          
          if (cont == tamanho): # ao encontrar espacos suficientes, gravar a nova informacao
            for t in range(tamanho):
              memoria[indice+t] = letra
            gravou = 1
            break
          
        else:
          cont=0 # resetar contador quando encontramos uma celula ja preenchida

      if (gravou == 0):
        print("\nNão encontrou espaço na memória.\n")
        
      for i in range(100): #imprimir o conteúdo da variável memória
        print (memoria[i], end="|")


    else:
        if (opcao == 2): # lógica da melhor escolha
          # comparar espacos livres maiores ou iguais ao tamanho minimo
          # e escolher o menor deles para gravar a nova informacao
          
          sufic = 0
          indice=-1
          indiceescolhido=-1
          espacos=0
          espacosescolhido=-1
          
          for i in range(100):  
            
            if (memoria[i] == ' '): # se a celula for vazia
              
              if (espacos == 0):
                indice = i # guardar qual o indice do primeiro espaco vazio

              espacos +=1 # adicionar ao contador do numero de celulas vazias
              
              if (espacos >= tamanho): # encontrou espacos suficientes ou mais
                sufic = 1
            
            else:
              # se o numero de espacos livres for suficiente e/ou menor que o 
              # espaco anteriormente registrado, ele é o novo espaco escolhido

              # para o primeiro espaco suficiente encontrado:
              if (espacos>=tamanho and espacosescolhido == -1):
                espacosescolhido = espacos
                indiceescolhido = indice
                
              # para os proximos espacos encontrados:
              if (espacos>=tamanho and espacos<espacosescolhido):
                espacosescolhido = espacos
                indiceescolhido = indice
                
              espacos=0 # resetar contador quando encontramos uma celula ja preenchida
              
          if (sufic == 1):
            for t in range(tamanho): # gravar nova informacao no espaco selecionado
              memoria[indiceescolhido+t] = letra          
          else:
            print("\nNão encontrou espaço na memória.\n")
          
          for i in range(100): # imprimir o conteúdo da variável memória
            print (memoria[i], end="|")

        else:

          if(opcao == 3): # lógica da pior escolha
            # comparar espacos livres maiores ou iguais ao tamanho minimo
            # e escolher o maior deles para gravar a nova informacao
            
            sufic = 0
            indice=-1
            indicemaior=-1
            espacos=0
            espacosmaior=0
            
            for i in range(100):  
              
              if (memoria[i] == ' '): # se a celula for vazia
                
                if (espacos == 0):
                  indice = i # guardar qual o indice do primeiro espaco vazio
                
                espacos +=1 # adicionar ao contador do numero de celulas vazias
                
                if (espacos == tamanho or espacos > tamanho): # encontra espacos suficientes ou mais

                  sufic = 1
                  
                  if(espacosmaior == 0):
                    indicemaior = indice
                    espacosmaior = espacos
                  
                  if(espacos>=espacosmaior):

                    indicemaior = indice
                    espacosmaior = espacos
              
              else:
                espacos=0 # resetar contador quando encontramos uma celula ja preenchida
            #fim do loop
                
            if(sufic == 1):
              for t in range(tamanho): # gravar nova informacao no espaco selecionado
                memoria[indicemaior+t] = letra          
            else:
              print("\nNão encontrou espaço na memória.\n")
              
            for i in range(100): # imprimir o conteúdo da variável memória
              print (memoria[i], end="|")