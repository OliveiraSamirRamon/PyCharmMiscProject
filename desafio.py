
from tabulate import tabulate
import random

class Entradas:
    def __init__(self, descricao, valor):
        self.id = random.randint(100, 9999)
        self.descricao = descricao
        self.valor = valor

produtos = [
    Entradas("teste", 11.1), 
    Entradas("teste", 122.1), 
    Entradas("aaa", 122.1),
    Entradas("bbb", 122.1),
    Entradas("ccc", 122.1),
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
    valor = validaEntradaMenu()
    abrirMenuSelecionado(valor)

def validaEntradaMenu():
    while True:
        try:
            valor = int(input("Digite um número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    return valor

def validarEntradaValor():
    while True:
        try:
            valor = float(input("Valor: "))
            break
        except ValueError:
            print("Valor inválido")
    valor = float(f"{valor:.2f}")
    return valor

def abrirMenuCadastrar():
    print("------------------------------Cadastro------------------------------")
    descricao = str(input("Descricacao: "))
    valor = validarEntradaValor()
    resposta = confirmacao()
    if resposta == "sim":
        produtos.append(Entradas(descricao, valor))
        print(f"Descricao {descricao} | Valor: {valor}")
        abrirMenuOpcoes()
    elif resposta == "nao":
        abrirMenuCadastrar()

def confirmacao():
    resposta = str(input("Confirma?: (sim/nao/voltar): "))
    while(resposta != "sim" and resposta != "nao" and resposta !="voltar"):
        print("resposta inválida")
        resposta = str(input("Confirma?: (sim/nao/voltar): "))
    if resposta == "voltar":
        abrirMenuOpcoes()
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
    valor = validarEntradaValor()
    novoCampo = Entradas(descricao, valor)
    indiceParaAlteracao = produtos.index(campoParaAlteracao)
    resposta = confirmacao()
    if resposta == "sim":
        produtos[indiceParaAlteracao] = novoCampo
    elif resposta == "nao":
        alterarValor(campoParaAlteracao)
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





