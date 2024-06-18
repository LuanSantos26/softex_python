numero = int(input("digite um numero que seja meno ou igual a 1000:"));
if numero >= 1000:
 print("o numero tem que ser menor que 1000");
else:
   centenas=numero//100
   resto=numero % 100
   dezenas=numero //10
   unidades= resto % 10
if centenas>0:
    print("centenas",centenas);
    print("dezenas", dezenas);
    print("unidades", unidades);
else:
    print("dezenas", dezenas);
    print("unidades", unidades);