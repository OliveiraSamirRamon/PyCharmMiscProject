
from tabulate import tabulate
import random

class Produto:
    def __init__(self, id, descricao, valor):
        self.id = id
        self.descricao = descricao
        self.valor = valor

produtos = [
    Produto(random.randint(100, 999), "teste", 11.1), 
    Produto(random.randint(100, 999), "teste", 122.1), 
    Produto(random.randint(100, 999), "aaa", 122.1),
    Produto(random.randint(100, 999), "bbb", 122.1),
    Produto(random.randint(100, 999), "ccc", 122.1),
    ]

print("--------------------------------------------------------------------------------------------")
print("Bem vindo ao sistema de gestão financeira python")
print("--------------------------------------------------------------------------------------------")

# auth = False

# while auth == False:
#     nome = input("Digite seu usuário: ")
#     senha = input("Digite a senha: ")
#     if nome != "Samir" and senha != "123":
#         print("-----------------------")
#         print("Usuário inválido")
#         print("-----------------------")
#     else:
#         auth = True 
          
# print("-----------------------")



# print("Bem vindo", nome)


def abrirMenuSelecionado(valor):
    match valor:
        case 0:
            sair()
        case 1:
            abrirMenuCadastrar()
        case 2:
            abrirMenuListar()
        case 3:
            abriMenuApagar()
        case 4:
            abrirMenuAlterar()
        case _:
            print("valor inválido")
            abrirMenuSelecionado()

def escolheOpcao():
    valor = validaEntrada()
    abrirMenuSelecionado(valor)

def validaEntrada():
    while True:
        try:
            valor = int(input("Digite um número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    return valor

def abrirMenuCadastrar():
    print("------------------------------Cadastro------------------------------")
    descricao = str(input("Descricacao: "))
    valor = float(input("Valor: "))
    resposta = confirmacao()
    if resposta == "sim":
        produtos.append(Produto(random.randint(100, 999), descricao, valor))
        print(f"Descricao {descricao} | Valor: {valor}")
        abrirMenuOpcoes()
    elif resposta == "nao":
        abrirMenuCadastrar()

def confirmacao():
    resposta = str(input("Confirma?: (sim/nao): "))
    while(resposta != "sim" and resposta != "nao"):
        print("resposta inválida")
        resposta = str(input("Confirma?: (sim/nao): "))
    return resposta

def abrirMenuListar():
    print("------------------------------Listagem------------------------------")
    dados = converterParaDic(produtos)
    print(tabulate(dados, headers="keys", tablefmt='orgtbl'))
    abrirMenuOpcoes()

def converterParaDic(lista):
    dados = [{"Id": p.id, "Descricao": p.descricao, "Valor": p.valor} for p in lista]
    return dados

def abriMenuApagar():
    print("------------------------------Apagar------------------------------")
    busca = str(input("Digite o nome do campo a ser apagado: "))
    listaFiltrada = filtrarLista(busca)
    dados = converterParaDic(listaFiltrada)
    print(tabulate(dados, headers="keys", tablefmt='orgtbl'))
    iniciarProcessoDeApagar(listaFiltrada)

def iniciarProcessoDeApagar(listaFiltrada):
    if len(listaFiltrada) > 1:
            print("Existe mais de um item correspondente a busca: ")
            id = int(input("Digite o id do campo que deseja apagar: "))
            for item in listaFiltrada:
                if item.id == id:
                    listaFiltrada = [item]

    if len(listaFiltrada) == 1:
        resposta = confirmacao()
        if resposta == "sim":
            apagarItem(listaFiltrada)
        elif resposta == "nao":
            abriMenuApagar()
    else:
        print("Campo não encontrado")
        abriMenuApagar()

def apagarItem(listaFiltrada):
    indiceProduto = 0
    id = listaFiltrada[indiceProduto].id
    for produto in produtos:
        if produto.id == id:
            produtos.remove(produto)
            print("Campo apagado")
            abrirMenuOpcoes()
            break

def filtrarLista(busca):
    listaFiltrada = []
    for p in produtos:
        if busca.lower() in p.descricao.lower():
            listaFiltrada.append(p)
    return listaFiltrada

def abrirMenuAlterar():
    busca = str(input("Digite o nome do campo a ser alterado: "))
    listaFiltrada = filtrarLista(busca)
    dados = converterParaDic(listaFiltrada)
    print(tabulate(dados, headers="keys", tablefmt='orgtbl'))
    iniciarProcessoDeAlteracao(listaFiltrada)

def iniciarProcessoDeAlteracao(listaFiltrada):
    if len(listaFiltrada) > 1:
        print("Existe mais de um item correspondente a busca: ")
        id = int(input("Digite o id do campo que deseja alterar: "))
        for item in listaFiltrada:
            if item.id == id:
                alterarValor(item)

    elif len(listaFiltrada) == 1:
        alterarValor(listaFiltrada[0])
        
def alterarValor(campoParaAlteracao):
    descricao = str(input("Descricacao: "))
    valor = str(input("Valor: "))
    novoCampo = Produto(123, descricao, valor)
    indiceParaAlteracao = produtos.index(campoParaAlteracao)
    produtos[indiceParaAlteracao] = novoCampo
    abrirMenuOpcoes()

def sair():
    print("Adeus!")

def abrirMenuOpcoes():
    print("--------------------------------------------------------------------------------------------")
    print("O que deseja fazer hoje?: ")
    print("--------------------------------------------------------------------------------------------")
    print("" \
    "\n 1-Cadastrar" \
    "\n 2-Listar" \
    "\n 3-Apagar" \
    "\n 4-Alterar" \
    "\n 0-Sair do sistema" \
    "\n" \
    "")
    print("--------------------------------------------------------------------------------------------")
    escolheOpcao()

abrirMenuOpcoes()





