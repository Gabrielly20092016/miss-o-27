numero = int(input("Digite um número: "))
12

if numero % 2 == 0:
    print("Portal 1 liberado! Número é par.")
   
    if numero % 3 == 0:
        print("Portal 2 liberado! Número é múltiplo de 3.")
        
    
        if 10 <= numero <= 30:
            print("Portal 3 liberado! O cofre abriu! 🎉")
        else:
            print("Portal 3 bloqueado! Número fora do intervalo.")
            
    else:
        print("Portal 2 bloqueado! Número não é múltiplo de 3.")
        
else:
    print("Portal 1 bloqueado! Número não é par.")