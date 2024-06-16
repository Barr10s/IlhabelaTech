nome = input("Escreva o nome do cliente: ") #escrever em MAIÚSCULA, não consegui usar o upper.
sobrenome = input('Escreva o sobrenome do cliente: ') #escrever em MAIÚSCULA, não consegui usar o upper.
mes = input("Mês que o cliente realizou a compra: ") #escrever em MAIÚSCULA, não consegui usar o upper.
valor = input("Valor gasto pelo cliente: ")
nomeparacupom = nome
cupom = nome + sobrenome + "É10."



print(f"Olá, {nome} {sobrenome}. Em {mes} você realizou uma compra no valor de R${valor} e ganhou um desconto de 10% em sua próxima compra. Use o cupom {cupom}")