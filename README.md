# A3 PYTHON
PROJETO A3

import json

class Cliente:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"


class SistemaCadastro:
    def __init__(self):
        self.clientes = []
        self.proximo_id = 1

    def adicionar_cliente(self, nome, email, telefone):
        cliente = Cliente(self.proximo_id, nome, email, telefone)
        self.clientes.append(cliente)
        self.proximo_id += 1
        print(f"Cliente {nome} adicionado com sucesso!")

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        print("\n--- Lista de Clientes ---")
        for cliente in self.clientes:
            print(cliente)

    def editar_cliente(self, id_cliente, nome=None, email=None, telefone=None):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            if nome:
                cliente.nome = nome
            if email:
                cliente.email = email
            if telefone:
                cliente.telefone = telefone
            print(f"Cliente ID {id_cliente} atualizado com sucesso!")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")

    def deletar_cliente(self, id_cliente):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            self.clientes.remove(cliente)
            print(f"Cliente ID {id_cliente} removido com sucesso!")
        else:
            print(f"Cliente com ID {id_cliente} não encontrado.")

    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                return cliente
        return None

    def salvar_dados(self, arquivo="clientes.json"):
        with open(arquivo, "w") as f:
            dados = [cliente.__dict__ for cliente in self.clientes]
            json.dump(dados, f)
        print(f"Dados salvos em {arquivo}.")

    def carregar_dados(self, arquivo="clientes.json"):
        try:
            with open(arquivo, "r") as f:
                dados = json.load(f)
                self.clientes = [Cliente(**cliente) for cliente in dados]
                self.proximo_id = max(cliente.id for cliente in self.clientes) + 1
            print(f"Dados carregados de {arquivo}.")
        except FileNotFoundError:
            print(f"Arquivo {arquivo} não encontrado. Nenhum dado carregado.")


def menu():
    sistema = SistemaCadastro()
    sistema.carregar_dados()

    while True:
        print("\n--- Menu de Cadastro ---")
        print("1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Editar Cliente")
        print("4. Deletar Cliente")
        print("5. Salvar Dados")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            sistema.adicionar_cliente(nome, email, telefone)
        elif opcao == "2":
            sistema.listar_clientes()
        elif opcao == "3":
            id_cliente = int(input("ID do Cliente a editar: "))
            nome = input("Novo Nome (pressione Enter para manter): ")
            email = input("Novo Email (pressione Enter para manter): ")
            telefone = input("Novo Telefone (pressione Enter para manter): ")
            sistema.editar_cliente(
                id_cliente,
                nome if nome else None,
                email if email else None,
                telefone if telefone else None,
            )
        elif opcao == "4":
            id_cliente = int(input("ID do Cliente a deletar: "))
            sistema.deletar_cliente(id_cliente)
        elif opcao == "5":
            sistema.salvar_dados()
        elif opcao == "6":
            sistema.salvar_dados()
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

