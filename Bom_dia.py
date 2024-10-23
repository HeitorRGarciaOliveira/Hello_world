import math
while True:
    valor1 = int(input("Digite o valor que sera calculado: "))
    valor2 = int(input("Digite o valor que sera calculado: "))
    print("\n1. soma \n2. subtrair \n3. multiplicar \n4. dividir \n5. elevar \n6. raiz") 
    valor3 = input("\n")
    if valor3 == "1":
        print(valor1+valor2)
    elif valor3 == "2":
        print(valor1-valor2)
    elif valor3 == "3":
        print(valor1*valor2)
    elif valor3 == "4":
        print(valor1/valor2)
    elif valor3 == "5":
        print(math.pow(valor1,valor2))
    elif valor3 == "6":
        print(math.sqrt(valor1))