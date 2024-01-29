def calculadora ():
  while True:
    print("\nOperações disponíveis:")
    print("1:Soma")
    print("2:Subtração")
    print("3:Multiplicação")
    print("4:Divisão")
    print("0:Sair")

    escolha = int(input("Digite o número para a operação desejada: "))

    if escolha == 0:
      print("Saindo da calculadora. Até Mais!")
      break
    elif escolha not in [1, 2, 3, 4]:
      print("Essa opção não existe. Tente outro número.")
      continue

    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if escolha == 1:
      resultado = num1 + num2
      print(f"Resultado da soma: {resultado}")
    elif escolha == 2:
      resultado = num1 - num2
      print(f"Resultado da subtração: {resultado}")
    elif escolha == 3:
      resultado = num1 * num2
      print(f"Resultado da multiplicação: {resultado}")
    elif escolha == 4:
      if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado da divisão: {resultado}")
      else:
        print("Erro: Divisão por zero!")

calculadora ()
