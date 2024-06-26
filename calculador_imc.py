avaliados = [] 

def menu_salvar_carregar():
    while True:
        print("*********************************")
        print("**** SALVAR E CARREGAR DADOS ****")
        print("*********************************")
        
        print("""MENU DE SALVAR E CARREGAR
        1 - Salvar Dados em um Arquivo
        2 - Carregar Dados de um Arquivo
        3 - Voltar ao Menu Principal""")
        
        opc = int(input("Escolha uma opção: "))
        
        if opc == 1:
            with open("avaliados.txt", "w") as file:
                for dados in avaliados:
                    file.write(f"{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n")
            print("Dados salvos com sucesso.")
        elif opc == 2:
            try:
                with open("avaliados.txt", "r") as file:
                    avaliados.clear()
                    for line in file:
                        id, nome, imc, classificacao = line.strip().split(",")
                        avaliados.append([int(id), nome, float(imc), classificacao])
                print("Dados carregados com sucesso.")
            except FileNotFoundError:
                print("Arquivo não encontrado.")
        elif opc == 3:
            break
        else:
            print("Escolha uma opção válida!")


def menu_estatisticas():
    while True:
        print("*********************************")
        print("********* ESTATÍSTICAS **********")
        print("*********************************")
        
        print("""MENU DE ESTATÍSTICAS E ORDENAÇÃO
        1 - Exibir a Média de IMCs
        2 - Exibir o Maior e Menor IMC
        3 - Exibir Contagem de Avaliados por IMC
        4 - Voltar ao Menu Principal""")
        
        opc = int(input("Escolha uma opção: "))
        
        if opc == 1:
            if avaliados:
                soma_imc = sum([dados[2] for dados in avaliados])
                media_imc = soma_imc / len(avaliados)
                print("-------------------------")
                print(f"A média de IMCs é: {media_imc:.2f}")
                print("-------------------------")
                
        elif opc == 2:
            if len(avaliados) == 0:
                print("Nenhum avaliado registrado.")
            else:
                maior_imc = max(avaliados, key=lambda x: x[2])
                menor_imc = min(avaliados, key=lambda x: x[2])
                print(f"O maior IMC é {maior_imc[2]} de {maior_imc[1]}")
                print(f"O menor IMC é {menor_imc[2]} de {menor_imc[1]}")

        elif opc == 3:
           pass  # Criar Tarefa (6)
        elif opc == 4:
            break
        else:
            print("Escolha uma opção válida!")

def classifica_imc(imc):

    if imc < 16:
        return "Magreza Grave"
    elif imc <= 16.9:
        return "Magreza Moderada"
    elif imc <= 18.5:
        return "Magreza Leve"
    elif imc <= 24.9:
        return "Peso Ideal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 34.9:
        return "Obesidade Grau I"
    elif imc <= 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"
    

def nova_ordem(lista):
    alfa = []

    for c in lista:
        alfa.append(c[1])
    
    alfa.sort()
    
    for index, al in enumerate(alfa):
        for li in lista:
            if li[1] == al:
                alfa[index] = li[0]
                break
    
    return alfa


def print_formatado(lista, ordem):

    for item in ordem:
        print(f"{lista[item-1][0]}: O usuario {lista[item-1][1]} tem o imc {lista[item-1][2]} e sua classificação é: {lista[item-1][3]} ")


def imprime_ordem_imc(lista):
    lista_ordenada = sorted(lista, key = lambda x: x[2])
    for pessoa in lista_ordenada:
        nome = pessoa[1]
        imc = pessoa[2]
        grau = pessoa[3]
        print(f"    \n*{nome} tem o IMC {imc}, o que é considerado {grau}*")
        # CÓDIGO ESCRITO PELOS GURI, NÃO TEM JEITO

avaliados = []
id = 0

while True:
    print("*********************************")
    print("*******CALCULADORA DE IMC********")
    print("*********************************")
    
    print("""MENU
          1 - Calcular IMC
          2 - Exibir Resultados
          3 - Atualizar Dados de um Avaliado
          4 - Remover um Avaliado
          5 - Estatísticas
          6 - Salvar e Carregar Dados
          7 - Sair""")
    
    opc = int(input("Escolha uma opção: "))
    
    if opc == 1:
        nome = input("Digite o nome do avaliado: ")
        peso = float(input("Digite o peso do avaliado: "))
        altura = float(input("Digite a altura do avaliado: "))
        imc = round(peso / altura ** 2, 2)
        classificacao = classifica_imc(imc)
        print(f"O IMC de {nome} é {imc} e está classificado como: {classificacao}")

        id += 1
        dados = [id, nome, imc, classificacao]
        avaliados.append(dados)
    
    elif opc == 2:
        if len(avaliados) == 0:
            print("Nenhum avaliado registrado.")
        else:
            print("*********************************")
            print("*******EXIBIÇÃO DE RESULTADOS*****")
            print("*********************************")
            print("""SUBMENU DE EXIBIÇÃO DE RESULTADOS:
                  1 -ID
                  3 - Imprim Imprimir Todos os Resultados
                  2 - Imprimir por ir Avaliados Ordenados por Nome
                  4 - Imprimir Avaliados Ordenados por IMC
                  5 - Voltar ao Menu Principal""")
            sub_opc = int(input("Escolha uma opção: "))
            
            if sub_opc == 1:
                for dados in avaliados:
                    print(f"ID:{dados[0]} O IMC de {dados[1]} é {dados[2]} e está classificado como: {dados[3]}")
            
            elif sub_opc == 2:
                if sub_opc == 2:
                    id_desajada = int(input("Digite o ID desejado: "))
                    encontrado = True
                    for dados in avaliados:
                        if dados[0] == id_desajada:
                            print(f"ID:{dados[0]} O IMC de {dados[1]} é {dados[2]} e está classificado como: {dados[3]}")
                        if not encontrado:
                            print("ID não encontrado")
            
            elif sub_opc == 3:
                ordem_alfabetica = avaliados
                ordem_alfabetica = nova_ordem(ordem_alfabetica)

                for c in ordem_alfabetica:
                    print(c)

                print_formatado(avaliados, ordem_alfabetica)
                pass
            
            elif sub_opc == 4:
                imprime_ordem_imc(avaliados)
            
            elif sub_opc == 5:
                continue
    
    elif opc == 3:
        id_procurada = int(input("Digite a Id do avaliado para atualizar: "))
        encontrado = False
        for dados in avaliados:
            if dados[0] == id_procurada:
                nome = input("Digite o novo nome do avaliado: ")
                peso = float(input("Digite o novo peso do avaliado: "))
                altura = float(input("Digite a nova altura do avaliado: "))
                imc = round(peso / altura ** 2, 2)
                classificacao = classifica_imc(imc)
                dados[1] = nome
                dados[2] = imc
                dados[3] = classificacao
                print("Dados atualizados com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Id não encontrada.")
    
    elif opc == 4:
        id_procurada = int(input("Digite a Id do avaliado para remover: "))
        encontrado = False
        for dados in avaliados:
            if dados[0] == id_procurada:
                avaliados.remove(dados)
                print("Avaliado removido com sucesso.")
                encontrado = True
                break
        if not encontrado:
            print("Id não encontrada.")
    
    elif opc == 5:
        if len(avaliados) == 0:
            print("Nenhum avaliado registrado.")
        else:
            menu_estatisticas()
    
    elif opc == 6:
        menu_salvar_carregar()
    
    elif opc == 7:
        break
    
    else:
        print("Escolha uma opção válida!")
