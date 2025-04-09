numero = int(input("insira um valor para fazer uma conta"))
numero2 = int(input("insira outro valor para fazer a conta"))

meio = input("escolha o tipo de conta")

if meio == '+':
    print (numero+numero2)
elif meio == '-':
    print (numero2-numero)
elif meio == '*':
    print (numero*numero2)
elif meio == '/':
    print (numero/numero2)
else:
    print ("inválido")