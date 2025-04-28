#Importação das bibliotecas
from os import system
import unicodedata

#Função de reinício do sistema
def reinicio():
    print("Deseja realizar outra operação? Digite o número da opção desejada:")
    print()
    print("1-Sim")
    print("2-Não, desejo sair do sistema")
    print()
    escolha_repeticao=str(input(""))

    while escolha_repeticao not in ["1","2"]:
        system("cls")
        print()
        print("Opção inválida. Deseja realizar outra operação? Digite o número da opção desejada:")
        print()
        print("1-Sim")
        print("2-Não, desejo sair do sistema")
        print()
        escolha_repeticao=str(input(""))

    if escolha_repeticao == "1":
        selecao()
    elif escolha_repeticao == "2":
        print()
        input("Pressione Enter para sair do sistema...")


#Lógica da Criptografia
def funcao_criptografia():
    print()
    entrada_cripto = str(input("Digite o que deseja criptografar: "))

    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
    lista_alfabeto_cripto = list(entrada_cripto)
    criptografia = []

    for letra in lista_alfabeto_cripto:

        #Tratamento de letras Maiúsculas
        if letra.lower() in alfabeto and letra.isupper():
            letra_minus = letra.lower()
            posicao_letra = alfabeto.index(letra_minus)
            criptografia.append(alfabeto[posicao_letra + 1].upper())
        
        #Tratamento de letras Minúsculas
        elif letra in alfabeto and not letra.isupper():
            posicao_letra = alfabeto.index(letra)
            criptografia.append(alfabeto[posicao_letra + 1])

        #Tratamento de letras Maiúsculas Acentuadas
        elif letra not in alfabeto and letra.isupper():
            separa_caractere = unicodedata.normalize('NFD', letra)
            letra_normal = separa_caractere[0].lower()
            acento = separa_caractere[1]
            if letra_normal in alfabeto:
                posicao_letra = alfabeto.index(letra_normal)
                letra_encriptada = (alfabeto[posicao_letra + 1])
                letra_final = unicodedata.normalize('NFC', letra_encriptada + acento)
                criptografia.append(letra_final.upper())

        #Tratamento de letras Minúsculas Acentuadas
        elif letra.lower() not in alfabeto and letra.isalpha():
            separa_caractere = unicodedata.normalize('NFD', letra)
            letra_normal = separa_caractere[0]
            acento = separa_caractere[1]
            posicao_letra = alfabeto.index(letra_normal)
            letra_encriptada = (alfabeto[posicao_letra + 1])
            letra_final = unicodedata.normalize('NFC', letra_encriptada + acento)
            criptografia.append(letra_final)

       #Tratamento de tudo que não for letra
        else:
            criptografia.append(letra)


    saida_criptografia = ''.join(criptografia)

    print()
    print("Sua mensagem criptografada é: ", saida_criptografia)
    print()
    reinicio()


#Lógica da Descriptografia
def funcao_descriptografia():
    print()
    entrada_descripto = str(input("Digite o que deseja descriptografar: "))

    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lista_alfabeto_descripto = list(entrada_descripto)
    descriptografia = []

    for letra in lista_alfabeto_descripto:
        
        #Tratamento de letras Maiúsculas
        if letra.lower() in alfabeto and letra.isupper():
            letra_minus = letra.lower()
            posicao_letra = alfabeto.index(letra_minus)
            descriptografia.append(alfabeto[posicao_letra - 1].upper())
        
        #Tratamento de letras Minúsculas
        elif letra in alfabeto and not letra.isupper():
            posicao_letra = alfabeto.index(letra)
            descriptografia.append(alfabeto[posicao_letra - 1])
        
        #Tratamento de letras Maiúsculas Acentuadas
        elif letra not in alfabeto and letra.isupper():
            separa_caractere = unicodedata.normalize('NFD', letra)
            letra_base = separa_caractere[0].lower()
            acento = separa_caractere[1]
            if letra_base in alfabeto:
                posicao_letra = alfabeto.index(letra_base)
                letra_descripto = (alfabeto[posicao_letra - 1])
                letra_final = unicodedata.normalize('NFC', letra_descripto + acento)
                descriptografia.append(letra_final.upper())

       #Tratamento de letras Minúsculas Acentuadas
        elif letra.lower() not in alfabeto and letra.isalpha():
            separa_caractere = unicodedata.normalize('NFD', letra)
            letra_base = separa_caractere[0]
            acento = separa_caractere[1]
            posicao_letra = alfabeto.index(letra_base)
            letra_descripto = (alfabeto[posicao_letra - 1])
            letra_final = unicodedata.normalize('NFC', letra_descripto + acento)
            descriptografia.append(letra_final)

      #Tratamento de recebimento da letra "a" minúscula; a = z
        elif letra == 'a':
            descriptografia.append('z')

      #Tratamento de recebimento da letra "A" maiúscula; A = Z
        elif letra == 'A':
            descriptografia.append('Z')
        
        #Tratamento de tudo que não for letra
        else:
            descriptografia.append(letra)

    saida_descripto = ''.join(descriptografia)
    print()
    print("Sua mensagem descriptografada é: ", saida_descripto)
    print()
    reinicio()


#Função para escolha da operação
def selecao():
    global escolha
    system("cls")
    print("CIFRA DE CÉSAR - BETA 1.0")
    print()
    print("Olá! Digite o número da operação desejada:")
    print()
    print("1-Criptografia")
    print("2-Descriptografia")
    print()
    escolha = str(input())
    #Chamada das funcões de acordo a entrada do usuário
    if escolha == "1":
        funcao_criptografia()
    elif escolha == "2":
        funcao_descriptografia()

#Acionando a função da escolha da operação
selecao()

#Tratamento de entradas inválidas
while escolha not in ["1","2"]:
    system("cls")
    print()
    print("Opção inválida. Digite o número da operação desejada:")
    print()
    print("1-Criptografia")
    print("2-Descriptografia")
    print()
    escolha = str(input())
    if escolha == "1":
        funcao_criptografia()
    elif escolha == "2":
        funcao_descriptografia()






