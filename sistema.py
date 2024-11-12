from sistema_cadastros.lib1.interface import *
from sistema_cadastros.lib1.arquivo import *
from time import sleep


while True:
    resposta = menu(["Cadastrar novo produto", "Consultar produto", "Excluir produto", "Exibir todos os produtos", "Sair"])
    if resposta == 1:
        nome_produto = str(input("Digite o nome do produto: "))
        numero_serie = str(input("Digite o número de série: "))
        valor = float(input("Digite o valor do produto: "))
        cadastrar(nome_produto, numero_serie, valor)
    elif resposta == 2:
        cabecalho("consultar produto")
        nome = str(input("Digite o nome do produto a ser consultado: "))
        consultarProduto(nome)
    elif resposta == 3:
        cabecalho("excluir produto")
        nome = str(input("Digite o nome do produto: "))
        apagarProduto(nome) #TO-DO -> criar e finalizar a funcão
    elif resposta == 4:
        cabecalho("exibindo todos os produtos")
        exibirProdutos()
    elif resposta == 5:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente!")
    sleep(1)