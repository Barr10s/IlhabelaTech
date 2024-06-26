frutas = ['maçã', 'banana', 'laranja', 'uva', 'manga']
alergias = []

alergia_fruta = frutas[2]
alergias.append(alergia_fruta)

for verificacao in frutas: #estou dizendo para que verificacao leia a lista frutas
    if verificacao in alergias: #ou seja, se o que está em frutas, estiver em alergias, então tchain:
        print(f'{verificacao} está na lista de alergias.')
    else:
        print("A lista está correta")