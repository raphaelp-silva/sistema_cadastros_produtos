from sistema_cadastros.lib1.interface import *
from sistema_cadastros.lib1.arquivo import *
from time import sleep

arq = 'sistema-cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Cadastrar novo produto", "Consultar produto", "Editar produto", "Excluir produto", "Exibir todos os produtos", "Sair"])
    if resposta == 1:
        nome_produto = str(input("Digite o nome do produto: "))
        numero_serie = str(input("Digite o número de série: "))
        valor = float(input("Digite o valor do produto: "))
        cadastrar(arq, nome_produto, numero_serie, valor) #TO-DO -> criar e finalizar a funcão
    elif resposta == 2:
        cabecalho("consultar produto")
        #consultarProduto() #TO-DO -> criar e finalizar a funcão
    elif resposta == 3:
        cabecalho("editar produto")
        #editarProduto() #TO-DO -> criar e finalizar a funcão
    elif resposta == 4:
        cabecalho("excluir produto")
        nome = str(input("Digite o nome do produto: "))
        apagarProduto(arq, nome) #TO-DO -> criar e finalizar a funcão
    elif resposta == 5:
        cabecalho("exibindo todos os produtos")
        exibirProdutos(arq)
    elif resposta == 6:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente!")
    sleep(1)