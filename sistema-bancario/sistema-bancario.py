def sacar(*, LIMITE_SAQUES, saldo, numero_saques, extrato, limite ):
    if (numero_saques < LIMITE_SAQUES):
            sacar = float(input("Digite o valor desejado para saque: "))

            if (saldo - sacar) > 0:

                if sacar <= limite:

                    saldo = saldo - sacar
                    print("Saque realizado com sucesso!")
                    numero_saques +=1
                    extrato += f"Saque: R$ {sacar:.2f}\n"

                else:
                    print(f"O limite de valor por saque é  R$ {limite}.")
                    
            else:
                print("Valor indisponível para saque.")
    else:
            print("O limite de saques diário foi atingido.")

    return saldo, extrato


def setDeposito(saldo, extrato):
    depositar = float(input("Digite o valor desejado para depósito: "))
    if depositar>0:
        saldo = saldo+depositar
        extrato += f"Depósito: R$ {depositar}\n"
    else:
        print("Valor inválido!")

    return saldo, extrato


def getExtrato(saldo, *, transacoes):
    print("Não foram realizadas movimentações." if not transacoes else transacoes) # se extrato for uma string vazia, executa print; se nao for vazia, retorna extrato
    print(f"\nSaldo: R$ {saldo:.2f}")

     
def criarUsuario(lista_usuarios):
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira sua data de nascimento: ")
    cpf = int(input("Digite seu CPF: "))
    print("Insira seu endereço: ")
    logradouro = input("Logradouro: ")
    numero = int(input("Numero: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade/UF: ")


    if cpf in lista_usuarios:
        print("CPF já cadastrado.")
        return

    lista_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade}})

#------------------------------------------------------------------------------------------------------------------------------------------------------

menu = """
----- MENU -----

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

"""

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1": # depósito----------------------------------------------------------------------
        print("Depósito")
        saldo, extrato = setDeposito(saldo, extrato)
        print(f"\nSaldo atual = R$ {saldo: .2f}")
        print(f"\nExtrato: \n{extrato}")
       
        

    elif opcao == "2": # saque----------------------------------------------------------------------
        print("Saque\n")

        saldo1, extrato1 = sacar(LIMITE_SAQUES=LIMITE_SAQUES, saldo= saldo, numero_saques= numero_saques, extrato=extrato, limite=limite)
        print(f"\nSaldo atual = R$ {saldo1: .2f}")
        print(f"\nExtrato: \n{extrato}")
    

        
        
    elif opcao == "3": #extrato-----------------------------------------------------------------
       getExtrato(saldo, transacoes=extrato)


    elif opcao == "4": #sair----------------------------------------------------------------------
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operaçao desejada.")