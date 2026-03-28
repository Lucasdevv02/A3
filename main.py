# Projeto A3 - Sistema de Cadastro de Clientes
# Estudante: Lucas Silva (ADS)

def sistema_cadastro():
    lista_clientes = []
    
    while True:
        print("\n--- MENU DE CADASTRO ---")
        print("1. Cadastrar Novo Cliente")
        print("2. Listar Clientes Cadastrados")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o e-mail: ")
            # Salvando em um dicionário
            cliente = {"nome": nome, "email": email}
            lista_clientes.append(cliente)
            print(f"\n✅ Cliente {nome} cadastrado com sucesso!")
            
        elif opcao == '2':
            print("\n--- CLIENTES CADASTRADOS ---")
            if not lista_clientes:
                print("Nenhum cliente cadastrado ainda.")
            for i, cliente in enumerate(lista_clientes, 1):
                print(f"{i}. Nome: {cliente['nome']} | E-mail: {cliente['email']}")
                
        elif opcao == '3':
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

if _name_ == "_main_":
    sistema_cadastro()
