#calculadora

#Menu inicial
while True:
    print("\nEscolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("X - Sair")
#Lê a opção do usuario
    opcao = input("Opção: ").upper() 
#Sai do programa
    if opcao == 'X':
        print("Encerrando a calculadora...")
        break
    #verifica se a opção é valida
    elif opcao in ['1', '2', '3', '4']:
        numeros = []
        while True:
            num = input("Digite um número (ou 'P' para parar): ")
            if num.upper() == 'P':  #para de receber numero
                break
            elif num.replace('.', '', 1).isdigit():  #Verifica se um numero é valido
                numeros.append(float(num))  #converte um numero
            else:
                print("Por favor, digite um número válido.")
                continue

        # verifica se tem numero o suficiente na operação
        if len(numeros) < 2:
            print("Por favor, forneça pelo menos dois números.")
            continue

        # Calcula o resultado da operação escolhida
        resultado = numeros[0]  # Inicializando o resultado com o primeiro número
        for num in numeros[1:]:
            if opcao == '1':  # Adição
                resultado += num
            elif opcao == '2':  # Subtração
                resultado -= num
            elif opcao == '3':  # Multiplicação
                resultado *= num
            elif opcao == '4':  # Divisão
                resultado /= num

        print("Resultado:", resultado)

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

