# Prova_AP2_4N
Diretório Main do Projeto da Prova AP2 da Turma 4N

# Calculadora de IMC

Este é um aplicativo simples em Python que calcula e classifica o Índice de Massa Corporal (IMC) de avaliados. O objetivo é permitir o cálculo do IMC de indivíduos com base no peso e altura informados, além de fornecer funcionalidades adicionais como exibição de resultados, estatísticas e salvamento/carregamento de dados.

## Funcionalidades Implementadas

- **Calcular IMC:** Permite inserir dados de nome, peso e altura para calcular o IMC de um avaliado.
- **Exibir Resultados:** Permite visualizar todos os avaliados cadastrados, com opções para imprimir por ID, nome ou IMC.
- **Atualizar Dados de um Avaliado:** Permite editar os dados de um avaliado já cadastrado.
- **Remover um Avaliado:** Permite remover um avaliado da lista.
- **Estatísticas:** Permite visualizar informações estatísticas sobre os avaliados, incluindo média de IMCs, maior e menor IMC registrado e contagem por categoria de IMC.
- **Salvar e Carregar Dados:** Permite salvar os dados em um arquivo e carregá-los posteriormente para continuar o trabalho.

## Tarefas e Implementações

### Grupo 1

**Tarefa: Implementar Impressão por ID**
- Descrição: Implementar a exibição do resultado do avaliado através da busca pelo ID do mesmo.
- Localização no código: Menu Principal, opção 2 (Exibir Resultados), sub-opção 2 (Imprimir por ID).
- Detalhes da Implementação: Solicitar o ID do avaliado, buscar na lista de avaliados e exibir os dados correspondentes.
- Nível de Conhecimento: Básico. Não requer conhecimentos avançados de programação.

### Grupo 2

**Tarefa: Implementar Impressão por Nome**
- Descrição: Implementar a exibição da lista de avaliados ordenada por nome.
- Localização no código: Menu Principal, opção 2 (Exibir Resultados), sub-opção 3 (Imprimir Avaliados Ordenados por Nome).
- Detalhes da Implementação: Ordenar a lista de avaliados pelo nome e exibir os dados.
- Nível de Conhecimento: Básico. Não requer conhecimentos avançados de programação.

### Grupo 3

**Tarefa: Implementar Impressão por IMC**
- Descrição: Implementar a exibição da lista de avaliados ordenada por IMC.
- Localização no código: Menu Principal, opção 2 (Exibir Resultados), sub-opção 4 (Imprimir Avaliados Ordenados por IMC).
- Detalhes da Implementação: Ordenar a lista de avaliados pelo valor do IMC e exibir os dados.
- Nível de Conhecimento: Básico. Não requer conhecimentos avançados de programação.

### Grupo 4

**Tarefa: Implementar Cálculo e Exibição da Média de IMCs**
- Descrição: Implementar a exibição da média dos IMCs avaliados.
- Localização no código: Menu Principal, opção 5 (Estatísticas), sub-opção 1 (Exibir a Média de IMCs).
- Detalhes da Implementação: Calcular a média dos IMCs presentes na lista de avaliados e exibir o resultado.
- Nível de Conhecimento: Básico. Não requer conhecimentos avançados de programação..

### Grupo 5

**Tarefa: Implementar Exibição do Maior e Menor IMC**
- Descrição: Implementar a exibição do maior e menor IMC avaliados, juntamente com o nome e a classificação.
- Localização no código: Menu Principal, opção 5 (Estatísticas), sub-opção 2 (Exibir o Maior e Menor IMC).
- Detalhes da Implementação: Encontrar e exibir o maior e menor IMC da lista de avaliados.
- Nível de Conhecimento: Básico. Não requer conhecimentos avançados de programação.

### Grupo 6

**Tarefa: Implementar Contagem de Avaliados por Categoria de IMC**
- Descrição: Implementar a exibição das classificações com suas contagens de avaliados.
- Localização no código: Menu Principal, opção 5 (Estatísticas), sub-opção 3 (Exibir Contagem de Avaliados por Classificação de IMC).
- Detalhes da Implementação: Contar e exibir a quantidade de avaliados para cada categoria de IMC.
- Nível de Conhecimento: Básico. Não requer conhecimentos avançados de programação.

## Comentários Adicionais

- As funções `menu_salvar_carregar()` e `menu_estatisticas()` estão implementadas e funcionais, conforme o esperado.
- Os menus principais e submenus estão estruturados corretamente para direcionar o usuário para as funcionalidades desejadas.
- A estrutura condicional (`if`, `elif`, `else`) está adequada para cada menu e submenu, garantindo que as opções sejam tratadas de maneira correta.

  ## Menus do programa (COMPLETO)
  Menu Principal:
    1. Calcular IMC
    2. Exibir Resultados
    3. Atualizar Dados de um Avaliado
    4. Remover um Avaliado
    5. Estatísticas 
    6. Salvar e Carregar Dados
    7. Sair
Submenu de Exibição de Resultados:
    1. Imprimir Todos os Resultados
    2. Imprimir por ID
    3. Imprimir Avaliados por Nome
    4. Imprimir Avaliados por IMC
    5. Voltar ao Menu Principal
Submenu de Estatísticas e Ordenação:
    1. Exibir a Média de IMCs
    2. Exibir o Maior e Menor IMC
    3. Exibir Contagem de Avaliados por IMC
    4. Voltar ao Menu Principal
Submenu de Salvar e Carregar Dados:
    1. Salvar Dados em um Arquivo 
    2. Carregar Dados de um Arquivo
    3. Voltar ao Menu Principal

Portanto, o próximo passo será implementar as partes marcadas com `pass` conforme as tarefas definidas para cada grupo, para completar as funcionalidades da calculadora de IMC conforme os requisitos estabelecidos.
