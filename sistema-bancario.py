def sacar(*, LIMITE_SAQUES, saldo, numero_saques, extrato, limite):
    if numero_saques < LIMITE_SAQUES:
        valor_saque = float(input("Digite o valor desejado para saque: "))
        
        if saldo - valor_saque >= 0:
            if valor_saque <= limite:
                saldo -= valor_saque
                print("Saque realizado com sucesso!")
                numero_saques += 1
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
            else:
                print(f"O limite de valor por saque é R$ {limite}.")
        else:
            print("Valor indisponível para saque.")
    else:
        print("O limite de saques diário foi atingido.")
    
    return saldo, extrato, numero_saques

def setDeposito(saldo, extrato):
    valor_deposito = float(input("Digite o valor desejado para depósito: "))
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
    else:
        print("Valor inválido!")
    return saldo, extrato

def getExtrato(saldo, *, transacoes):
    print("Não foram realizadas movimentações." if not transacoes else transacoes) 
    print(f"\nSaldo: R$ {saldo:.2f}")

def criarUsuario(lista_usuarios):
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira sua data de nascimento: ")
    cpf = input("Digite seu CPF: ")
    print("Insira seu endereço: ")
    logradouro = input("Logradouro: ")
    numero = input("Numero: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade/UF: ")

    if cpf in [usuario['cpf'] for usuario in lista_usuarios]:
        print("CPF já cadastrado.")
        return

    lista_usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf, 
        "endereço": {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade}
    })
    print("Usuário criado com sucesso!")

def criarConta(num_conta, lista_contas, lista_usuarios):
    cpf = input("Usuário (CPF): ")
    usuario_encontrado = next((usuario for usuario in lista_usuarios if usuario["cpf"] == cpf), None)

    if usuario_encontrado:
        num_conta += 1
        user_agencia = "0001"
        lista_contas.append({"usuario": cpf, "agencia": user_agencia, "conta": num_conta})
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado.")
    
    return num_conta, lista_contas

# Menu principal
menu = """
----- MENU -----
[1] - Criar usuário
[2] - Criar conta
[3] - Acessar funcionalidades
[4] - Sair
"""

# Menu de funcionalidades
menu2 = """
----- MENU -----
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Voltar
"""

lista_contas = []
lista_usuarios = []
num_conta = 0

saldo = 0.0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        criarUsuario(lista_usuarios)

    elif opcao == "2":
        num_conta, lista_contas = criarConta(num_conta, lista_contas, lista_usuarios)

    elif opcao == "3":
        while True:
            opcao2 = input(menu2)

            if opcao2 == "1":  # Depósito
                saldo, extrato = setDeposito(saldo, extrato)
                print(f"\nSaldo atual = R$ {saldo:.2f}")
                print(f"\nExtrato: \n{extrato}")

            elif opcao2 == "2":  # Saque
                saldo, extrato, numero_saques = sacar(
                    LIMITE_SAQUES=LIMITE_SAQUES, saldo=saldo, numero_saques=numero_saques, extrato=extrato, limite=limite
                )
                print(f"\nSaldo atual = R$ {saldo:.2f}")
                print(f"\nExtrato: \n{extrato}")

            elif opcao2 == "3":  # Extrato
                getExtrato(saldo, transacoes=extrato)

            elif opcao2 == "4":  # Voltar
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

    elif opcao == "4":  # Sair
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
