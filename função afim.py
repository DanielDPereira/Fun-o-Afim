print("Bem vindo a calculadora de função afim")
print("f(x) = ax+b")

a = float(input("Defina o valor de A: "))

if a != 0:

    b = float(input("Defina o valor de B: "))

    x = float(input("Gostaria de testar usando qual valor para X? "))

    y = a * x + b

    print("Quando X for ", x, " Y será ", y)
    print("A raiz da função é ", -b/a)

    if a > 0:
        print("A função é crescente 🙂 / ")
    
    if 0 > a:
        print("A função é decrescente ☹️ \ ")

else:
    print("Não é possível calcular, pois A não pode ser nulo")

print("Calculadora criada por Daniel Dias Pereira")

input()
