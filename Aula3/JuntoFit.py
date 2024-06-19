frequencia = int(input("Quantidade de dias treinando: "))
conta = 21 - frequencia
print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO.")
if frequencia >= 21: 
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
elif frequencia == 0:
    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
else:
    print(f"CONTINUE TREINANDO! VOCÊ ESTÁ A {conta} DIAS DE ALCANÇAR NOSSA META DA PROMOÇÃO TREINA JUNTO")


