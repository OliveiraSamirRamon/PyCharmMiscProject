
from tabulate import tabulate
from art import *
import random

class Entradas:
    def __init__(self, descricao, valor):
        self.id = random.randint(100, 9999)
        self.descricao = descricao
        self.valor = valor

entradas = [
    Entradas("teste", 200.12), 
    Entradas("teste", 200.24), 
    Entradas("aaa", 200.05),
    Entradas("bbb", 200.13),
    Entradas("ccc", 200.10),
    ]

print("--------------------------------------------------------------------------------------------")
tprint("BEM VINDO")
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


def abrir_menu_selecionado(valor):
    match valor:
        case 0:
            sair()
        case 1:
            abrir_menu_cadastrar()
        case 2:
            abrir_menu_listar()
        case 3:
            abrir_menu_apagar()
        case 4:
            abrir_menu_alterar()
        case 5:
            abrir_balanco_financeiro()
        case _:
            print("valor inválido")
            abrir_menu_selecionado()

def escolhe_opcao():
    valor = valida_entradaMenu()
    abrir_menu_selecionado(valor)

def valida_entradaMenu():
    while True:
        try:
            valor = int(input("Digite um número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
    return valor

def validar_entrada_valor():
    while True:
        try:
            valor = float(input("Valor: "))
            break
        except ValueError:
            print("Valor inválido")
    valor = float(f"{valor:.2f}")
    return valor

def abrir_menu_cadastrar():
    print("------------------------------Cadastro------------------------------")
    descricao = str(input("Descricacao: "))
    valor = validar_entrada_valor()
    resposta = confirmacao()
    if resposta == "sim":
        entradas.append(Entradas(descricao, valor))
        print(f"Descricao {descricao} | Valor: {valor}")
        abrir_menu_opcoes()
    elif resposta == "nao":
        abrir_menu_cadastrar()

def confirmacao():
    resposta = str(input("Confirma?: (sim/nao/voltar): "))
    while(resposta != "sim" and resposta != "nao" and resposta !="voltar"):
        print("resposta inválida")
        resposta = str(input("Confirma?: (sim/nao/voltar): "))
    if resposta == "voltar":
        abrir_menu_opcoes()
    return resposta

def abrir_menu_listar():
    print("------------------------------Listagem------------------------------")
    dados = converter_para_dic(entradas)
    print(tabulate(dados, headers="keys", tablefmt='orgtbl'))
    abrir_menu_opcoes()

def converter_para_dic(lista):
    dados = [{"Id": p.id, "Descricao": p.descricao, "Valor": f"{p.valor:.2f}"} for p in lista]    
    return dados

def abrir_menu_apagar():
    print("------------------------------Apagar------------------------------")
    busca = str(input("Digite o nome do campo a ser apagado: "))
    listaFiltrada = filtrar_lista(busca)
    dados = converter_para_dic(listaFiltrada)
    print(tabulate(dados, headers="keys", tablefmt='orgtbl'))
    iniciar_processo_de_apagar(listaFiltrada)

def iniciar_processo_de_apagar(listaFiltrada):
    if len(listaFiltrada) > 1:
            print("Existe mais de um item correspondente a busca: ")
            id = int(input("Digite o id do campo que deseja apagar: "))
            for item in listaFiltrada:
                if item.id == id:
                    listaFiltrada = [item]

    if len(listaFiltrada) == 1:
        resposta = confirmacao()
        if resposta == "sim":
            apagar_item(listaFiltrada)
        elif resposta == "nao":
            abrir_menu_apagar()
    else:
        print("Campo não encontrado")
        abrir_menu_apagar()

def apagar_item(listaFiltrada):
    indiceProduto = 0
    id = listaFiltrada[indiceProduto].id
    for produto in entradas:
        if produto.id == id:
            entradas.remove(produto)
            print("Campo apagado")
            abrir_menu_opcoes()
            break

def filtrar_lista(busca):
    listaFiltrada = []
    for p in entradas:
        if busca.lower() in p.descricao.lower():
            listaFiltrada.append(p)
    return listaFiltrada

def abrir_menu_alterar():
    busca = str(input("Digite o nome do campo a ser alterado: "))
    listaFiltrada = filtrar_lista(busca)
    dados = converter_para_dic(listaFiltrada)
    print(tabulate(dados, headers="keys", tablefmt='orgtbl'))
    iniciar_processo_de_alteracao(listaFiltrada)

def iniciar_processo_de_alteracao(listaFiltrada):
    if len(listaFiltrada) > 1:
        print("Existe mais de um item correspondente a busca: ")
        id = int(input("Digite o id do campo que deseja alterar: "))
        for item in listaFiltrada:
            if item.id == id:
                alterar_valor(item)

    elif len(listaFiltrada) == 1:
        alterar_valor(listaFiltrada[0])
        
def alterar_valor(campoParaAlteracao):
    descricao = str(input("Descricacao: "))
    valor = validar_entrada_valor()
    novoCampo = Entradas(descricao, valor)
    indiceParaAlteracao = entradas.index(campoParaAlteracao)
    resposta = confirmacao()
    if resposta == "sim":
        entradas[indiceParaAlteracao].descricao = novoCampo.descricao
        entradas[indiceParaAlteracao].valor = novoCampo.valor
    elif resposta == "nao":
        alterar_valor(campoParaAlteracao)
    abrir_menu_opcoes()

def sair():
    tprint("Adeus!")

def abrir_menu_opcoes():
    print("--------------------------------------------------------------------------------------------")
    print("O que deseja fazer hoje?: ")
    print("--------------------------------------------------------------------------------------------")
    print("" \
    "\n 1-Cadastrar" \
    "\n 2-Listar" \
    "\n 3-Apagar" \
    "\n 4-Alterar" \
    "\n 5-Trazer balanço financeiro" \
    "\n 0-Sair do sistema" \
    "\n" \
    "")
    print("--------------------------------------------------------------------------------------------")
    escolhe_opcao()

def abrir_balanco_financeiro():
    total = sum(entrada.valor for entrada in entradas)
    print("total: {:.2f}".format(total))
    abrir_menu_opcoes()
abrir_menu_opcoes()





