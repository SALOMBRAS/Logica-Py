numero = int(input("digite o numero"))
    
if numero % 2 == 0:
    PAR_IMPAR = "PAR"
else:
    PAR_IMPAR = "IMPAR"
    
if numero >0:
    sinal = "positivo"
elif numero <0:
    sinal = "negativo"
else:
    sinal = "zero"
print(f"{numero} é {PAR_IMPAR} é {sinal}")