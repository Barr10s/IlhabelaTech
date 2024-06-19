nome_dopet = input("Insira o nome do seu pet: ")
banhos = int(input(f"Quantos banhos o {nome_dopet} tomou nos últimos 12 meses? "))
lucro = banhos*45 #Só atendemos animais de médio porte, brincadeira. Não consegui pensar em como fazer essa distinção sem usar IF ELSE, mas não chegamos lá ainda
idade_pet = int(input("Insira a idade do seu Animal de estimação e nós informaremos a real idade dele! "))
idade_real = idade_pet*7





print(f"Olá! O(a) {nome_dopet} tem {idade_real} anos e nos últimos 12 meses o lucro com este animal foi R${lucro}")









