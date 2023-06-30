menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = str(input("Escolha uma opção \n"))
    if opcao == 'd':
        print("Depósito\n")
        valor = float(input("Insira o valor da transação\n"))
        while valor<=0:
            valor = float(input("Insira um valor positivo\n"))
        saldo += valor
        extrato.append(valor)

    elif opcao == "s":
        print("Saque\n")
        if ((numero_saques < 3) and (limite > 0 and limite <= 500)):
            valor = float(input("Insira o valor da transação \n"))
            if (valor > saldo):
                print("Saldo insuficiente \n")
            else:
                numero_saques += 1
                limite -= valor
                saldo -= valor
                extrato.append(valor)

        else:
            print("Não é possível efetuar o saque\n")
            print(f"Limite: R$ {limite} \n"
                  f"Numero de saques efetuados: {numero_saques}\n")

    elif opcao == "e":
        print("Extrato\n")
        print(f"Limite: R$ {limite} \n"
              f"Saques disponíveis: {numero_saques} \n")
        
        if not extrato:
            print("Não foram feitas movimentações \n")
        else:
            for i in range(0, len(extrato)):
                print(extrato[i])

        print(f"Saldo atual: R$ {saldo:.02f}")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, insira novamente a operação desejada \n")