from typing import List

class Pessoa:
    def __init__(self, nome: str, musica_fav: str, banda_fav: str):
        self.nome = nome
        self.musica_fav = musica_fav
        self.banda_fav = banda_fav

    def __str__(self):
        return f"{self.nome} gosta da música {self.musica_fav} da banda {self.banda_fav}"

pessoas: List[Pessoa] = []

def imprimir_menu() -> None:
    print("O que você deseja fazer?")
    print("1 - Cadastrar nova pessoa")
    print("2 - Remover pessoa")
    print("3 - Editar pessoa")
    print("4 - Exibir todas a pessoas")
    print("4 - Encerrar programa")

def cadastrar_pessoa() -> None:
    nome = input("Digite o nome da pessoa: ")
    musica_fav = input("Digite a música favorita da pessoa: ")
    banda_fav = input("Digite a banda favorita da pessoa: ")
    pessoa = Pessoa(nome, musica_fav, banda_fav)
    pessoas.append(pessoa)
    print(f"{pessoa.nome} cadastrado com sucesso!")

def remover_pessoa() -> None:
    nome = input("Digite o nome da pessoa que deseja remover: ")
    for i, pessoa in enumerate(pessoas):
        if pessoa.nome == nome:
            pessoas.pop(i)
            print(f"{pessoa.nome} removido com sucesso!")
            break
    else:
        print(f"{nome} não encontrado.")

def editar_pessoa() -> None:
    nome = input("Digite o nome da pessoa que deseja editar: ")
    for pessoa in pessoas:
        if pessoa.nome == nome:
            musica_fav = input(f"Digite a nova música favorita de {pessoa.nome}: ")
            banda_fav = input(f"Digite a nova banda favorita de {pessoa.nome}: ")
            pessoa.musica_fav = musica_fav
            pessoa.banda_fav = banda_fav
            print(f"{pessoa.nome} editado com sucesso!")
            break
    else:
        print(f"{nome} não encontrado.")
        
def exibir_pessoas() -> None:
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")
    else:
        for pessoa in pessoas:
            print(pessoa)


while True:
    imprimir_menu()
    opcao = input("Digite sua opção: ")
    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        remover_pessoa()
    elif opcao == "3":
        editar_pessoa()
    elif opcao == "4":
        exibir_pessoas()
    elif opcao == "5":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
    print("="*50)  # linha para separar as saídas no terminal
