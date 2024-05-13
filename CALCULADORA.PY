#ATV_CALCULADORA
while True:
    numero1 = float(input("Digite o numero: "))
    operacao = input("digite a operação ")
    numero2 = float(input("Digite o numero: "))
    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    else:
        resultado = "Operação invalida!"
    print(f"{numero1} {operacao} {numero2} = {resultado}")