# To-do List com CustomTkinter

Este é um aplicativo de lista de tarefas (to-do list) desenvolvido com a biblioteca `CustomTkinter` e `matplotlib`. O aplicativo permite adicionar, editar, excluir e visualizar o progresso das tarefas com base no status de cada uma (marcada ou não). Também oferece a capacidade de exibir um gráfico de barras com as tarefas concluídas e não concluídas.

## Funcionalidades

- **Adicionar Tarefas**: O usuário pode adicionar novas tarefas à lista inserindo o texto no campo de entrada e clicando no botão "Adicionar".
- **Excluir Tarefas**: Cada tarefa adicionada possui um botão para excluir a tarefa da lista.
- **Editar Tarefas**: O usuário pode editar o texto de uma tarefa existente.
- **Salvar Tarefas**: As tarefas são salvas em um arquivo de texto (`tarefas.txt`), o que permite que as tarefas persistam entre as sessões do aplicativo.
- **Gráfico de Status**: O aplicativo permite exibir um gráfico de barras que mostra a quantidade de tarefas concluídas e não concluídas.

## Como Rodar o Projeto

### Requisitos

- Python 3.x
- Bibliotecas: `customtkinter`, `matplotlib`

Para instalar as bibliotecas necessárias, execute:

```bash
pip install customtkinter matplotlib
```
### Instruções
1. Clone ou baixe o repositório.
2. Abra o arquivo `todolist.py` no seu editor de código preferido.
3. Execute o script Python: 

```bash
python todolist.py
```
O aplicativo será aberto com a interface gráfica.

## Detalhamento do Código
### Estrutura do Código
- **Funções principais**:
    - `salvar_tarefas()`: Salva as tarefas em um arquivo `tarefas.txt` para persistência entre as sessões.
    - `adicionar_tarefa()`: Adiciona uma nova tarefa à lista, criando um checkbox e os botões de "Excluir" e "Editar".
    - `carregar_tarefas()`: Carrega as tarefas salvas do arquivo `tarefas.txt` ao iniciar o aplicativo.
    - `excluir_tarefa()`: Exclui uma tarefa selecionada, tanto da interface quanto do arquivo.
    - `editar_tarefa()`: Permite editar o texto de uma tarefa existente.
    - `mostrar_grafico()`: Exibe um gráfico de barras com a quantidade de tarefas concluídas e não concluídas.

## Interface
- **Campo de entrada**: Onde o usuário digita o nome da nova tarefa.
- **Botão "Adicionar"**: Adiciona a tarefa à lista.
- **Botões "Excluir" e "Editar"**: Associados a cada tarefa, permitem excluir ou editar a tarefa.
- **Gráfico**: Exibe o status das tarefas (concluídas e não concluídas) em forma de gráfico de barras.

### Temas
- O aplicativo utiliza o modo de aparência "escuro" (`dark`) por padrão, mas pode ser alterado para o modo "claro" (`light`) ou "escuro" (`dark`) usando o método `set_appearance_mode()`.

## Casos de Uso
### Caso de Uso 1: Adicionar uma nova tarefa
1. O usuário digita o nome de uma tarefa no campo de entrada.
2. O usuário clica no botão "Adicionar".
3. A tarefa é adicionada à lista de tarefas, e o aplicativo a exibe com um checkbox, botão de excluir e editar.
### Caso de Uso 2: Excluir uma tarefa
1. O usuário clica no botão "Excluir" associado à tarefa que deseja remover.
2. A tarefa é removida da interface e do arquivo `tarefas.txt`.
### Caso de Uso 3: Editar uma tarefa
1. O usuário clica no botão "Editar" ao lado da tarefa que deseja alterar.
2. Uma janela de edição é aberta, permitindo ao usuário alterar o texto da tarefa.
3. Após salvar, a tarefa é atualizada na interface e no arquivo.
### Caso de Uso 4: Exibir gráfico de status
1. O usuário clica no botão "Mostrar Gráfico".
2. O aplicativo exibe um gráfico de barras mostrando a quantidade de tarefas marcadas como concluídas e não concluídas.
## Capturas de Tela
### Interface do Aplicativo
1. **Tela Principal**: Exibe a lista de tarefas com a capacidade de adicionar, editar e excluir tarefas.
![alt text](image-2.png)
2. **Gráfico de Status**: Exibe o gráfico de barras com as tarefas concluídas e não concluídas.
![alt text](image-1.png)
### Exemplo de Gráfico
O gráfico exibido representa o status das tarefas, com as tarefas concluídas mostradas em verde e as não concluídas em vermelho.

## Personalizações Futuras
- Adicionar funcionalidades como prioridade nas tarefas.
- Implementar categorias de tarefas (ex.: Trabalho, Estudo, Pessoal).
- Permitir o uso de datas de vencimento para tarefas.
- Adicionar mais opções de personalização de tema (como fontes, cores, etc.).
## Contribuições
Se você deseja contribuir para este projeto, fique à vontade para abrir uma **issue** ou **pull request**.