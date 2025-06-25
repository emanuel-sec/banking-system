menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 50000 # R$500,00 em centavos
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()
    if opcao == 'd':
        print("---- SEÇÃO DE DEPÓSITO ----")
        input_deposito = input("Digite o valor a ser depositado: ")
        try:
            input_deposito = input_deposito.replace(',', '.')
            input_deposito = int(float(input_deposito) * 100)
        except ValueError:
            print('Entrada inválida! Por favor, digite apenas números!')
            continue
        if input_deposito > 0:
            saldo += input_deposito
            extrato += f"Depósito: R${input_deposito / 100:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Por favor digite um valor maior que zero!")

    elif opcao == "s":
        print("---- SEÇÃO DE SAQUE ----")
        input_saque = input("Digite o valor a ser retirado: ")
        try:
            input_saque = input_saque.replace(',', '.')
            input_saque = int(float(input_saque) * 100)
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números!")
            continue
        if input_saque <= 0:
            print("Valor inválido! Digite um valor maior que zero.")
        elif input_saque > limite:
            print('Saque não autorizado: o valor excede o limite permitido por transação (R$500,00).')
            extrato += f'Saque:    Valor solicitado excede o limite.\n'
        elif numero_saques >= LIMITE_SAQUES:
            print('Você atingiu o limite diário de saques. Tente novamente amanhã!')
            extrato += f'Saque:    Limite diário atingido.\n'
        elif input_saque > saldo:
            print('O valor de saque é superior ao seu saldo!')
            extrato += f'Saque:    Saldo insuficiente para o valor solicitado.\n'
        else:
            saldo -= input_saque
            numero_saques += 1
            extrato += f"Saque:    R${input_saque / 100:.2f}\n"
            print("Saque efetuado com sucesso!")
            print(f"Você ainda pode fazer {LIMITE_SAQUES - numero_saques} saque(s) hoje.")
            print(f"Saldo atual: R${saldo / 100:.2f}")

    elif opcao == 'e':
        print("---- SEÇÃO EXTRATO ----")
        if extrato == "":
            print("Nenhuma movimentação realizada.")
        else:
            print(extrato)
        print(f"Saldo atual: R${saldo / 100:.2f}")

    elif opcao == "q":
        print("Saindo do sistema...")
        break