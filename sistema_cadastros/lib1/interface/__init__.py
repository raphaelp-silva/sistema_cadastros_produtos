def leiaInt(msg): #função para validar um número inteiro
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um numero inteiro válido")
        except KeyboardInterrupt:
            print("O usuário não digitou nenhum valor")
            return 0
        else:
            return n


def linha(tam = 72):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(72)) #centralizando o texto do cabeçalho
    print(linha())


def indice(nprod, nserie, preco):
    print(f"{nprod:<5}{nserie.center(60)}{preco:>1}")
    


def menu(lista): #criando a funcao que exibe o menu principal do sistema
    cabecalho("-> MENU PRINCIPAL DO SISTEMA <-") #utilizando a funcao cabecalho para receber o titulo do menu
    c = 1
    for item in lista: #estrutura de repeticao para criar uma lista com cada item da lista em uma linha, enumerados por um indice
        print(f"{c} - {item}")
        c += 1
    print(linha())
    opc = leiaInt("Digite sua opção: ") #lendo a opcao do usuário e retornando a opção selecionada na função 
    return opc