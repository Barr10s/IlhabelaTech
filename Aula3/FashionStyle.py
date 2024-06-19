compra=float(input("Valor da compra: R$"))

if compra <= 249.99:
    print("POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA")
elif compra >=250 and compra <=499.99:
    print("PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00")
else:
    print("PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%")