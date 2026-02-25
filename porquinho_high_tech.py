numero1 = int(input("PORTAL 1 - Digite um número par: "))

if numero1 % 2 == 0:
    print("Portal 1 aberto!")

  
    numero2 = int(input("PORTAL 2 - Digite um número múltiplo de 3: "))

    if numero2 % 3 == 0:
        print("Portal 2 aberto!")

     
        numero3 = int(input("PORTAL 3 - Digite um número entre 10 e 30: "))

        if 10 <= numero3 <= 30:
            print("Portal 3 aberto! Cofre liberado!")
        else:
            print("Portal 3 bloqueado!")
    else:
        print("Portal 2 bloqueado!")
else:
    print("Portal 1 bloqueado!")

