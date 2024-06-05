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

        depositar = float(input("Digite o valor desejado para depósito: "))
        if depositar>0:
            saldo = saldo+depositar
            extrato += f"Depósito: R$ {depositar}\n"
        else:
            print("Valor inválido!")
        

    elif opcao == "2": # saque----------------------------------------------------------------------
        print("Saque\n")

    
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

        
        
    elif opcao == "3": #extrato-----------------------------------------------------------------
        print("Não foram realizadas movimentações." if not extrato else extrato) # se extrato for uma string vazia, executa print; se nao for vazia, retorna extrato
        print(f"\nSaldo: R$ {saldo:.2f}")


    elif opcao == "4": #sair----------------------------------------------------------------------
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operaçao desejada.")