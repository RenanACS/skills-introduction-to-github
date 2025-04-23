

         


while True:
    try:     
        numero1 = float(input('Coloque seu primeiro número: '))
        numero2 = float(input('Coloque seu segundo número: '))
        operador = input('Coloque seu operador (+ - * /): ')

        if operador == '+':
            print("Resultado:", numero1 + numero2)
        elif operador == '-':
            print("Resultado:", numero1 - numero2)
        elif operador == '*':
            print("Resultado:", numero1 * numero2)
        elif operador == '/':
            if numero2 == 0:
                print('Não é possível dividir por 0')
            else:
                print("Resultado:", numero1 / numero2)
        else:
            print('Operador inválido')

        # esse input e if estavam com indentação errada e posição incorreta
        sair = input('Você quer sair? [s]im: ')
        if sair.lower() == 's':  # precisa chamar .lower()
            break

    except ValueError:
        print("Erro: por favor, insira apenas números.")
