from customtkinter import *
import customtkinter as ctk
import matplotlib.pyplot as plt

# Lista para armazenar os checkboxes e seus botões (excluir e editar)
checkboxes = []

def salvar_tarefas():
    """Salva as tarefas em um arquivo .txt"""
    with open("tarefas.txt", "w") as file:
        for checkbox in checkboxes:
            file.write(checkbox[0].cget("text") + "\n")

def adicionar_tarefa():
    texto_tarefa = entrada.get()  # Pega o texto inserido pelo usuário no entry
    if texto_tarefa:  # Verifica se o campo de entrada não está vazio
        # Cria uma variável para o checkbox (se está marcado ou não)
        var = ctk.BooleanVar()

        # Cria um novo checkbox com a variável e o texto da tarefa
        checkbox = ctk.CTkCheckBox(master=frame_tarefas, text=texto_tarefa, variable=var)

        # Cria o botão de exclusão para a nova tarefa
        btn_excluir = CTkButton(master=frame_tarefas, text="Excluir", command=lambda c=checkbox: excluir_tarefa(c))

        # Cria o botão de editar para a nova tarefa
        btn_editar = CTkButton(master=frame_tarefas, text="Editar", command=lambda c=checkbox: editar_tarefa(c))

        # Adiciona o checkbox e os botões à interface
        checkbox.pack(anchor="w", pady=5)
        btn_editar.pack(anchor="w", pady=5)
        btn_excluir.pack(anchor="w", pady=5)

        # Adiciona o checkbox e os botões à lista de checkboxes
        checkboxes.append((checkbox, btn_editar, btn_excluir))

        # Salva as tarefas no arquivo
        salvar_tarefas()

        # Limpa o campo de entrada depois de adicionar
        entrada.delete(0, "end")
    else:
        print("Digite o nome da tarefa.")  # Caso o campo esteja vazio

def carregar_tarefas():
    """Carrega as tarefas de um arquivo .txt"""
    try:
        with open("tarefas.txt", "r") as file:
            for line in file:
                texto_tarefa = line.strip()  # Remove a quebra de linha
                if texto_tarefa:
                    # Cria a variável para o checkbox
                    var = ctk.BooleanVar()
                    checkbox = ctk.CTkCheckBox(master=frame_tarefas, text=texto_tarefa, variable=var)

                    # Cria os botões de excluir e editar para cada tarefa
                    btn_excluir = CTkButton(master=frame_tarefas, text="Excluir", command=lambda c=checkbox: excluir_tarefa(c))
                    btn_editar = CTkButton(master=frame_tarefas, text="Editar", command=lambda c=checkbox: editar_tarefa(c))

                    # Adiciona a checkbox e os botões à interface
                    checkbox.pack(anchor="w", pady=5)
                    btn_editar.pack(anchor="w", pady=5)
                    btn_excluir.pack(anchor="w", pady=5)

                    # Armazena a referência do checkbox e seus botões na lista
                    checkboxes.append((checkbox, btn_editar, btn_excluir))
    except FileNotFoundError:
        # Caso o arquivo não exista, não há tarefas salvas
        pass

def excluir_tarefa(checkbox):
    """Exclui a tarefa selecionada e remove do arquivo"""
    # Encontra o checkbox na lista
    for c, btn_editar, btn_excluir in checkboxes:
        if c == checkbox:
            # Remove o checkbox e os botões da interface
            c.pack_forget()
            btn_editar.pack_forget()
            btn_excluir.pack_forget()

            # Remove a tarefa da lista
            checkboxes.remove((c, btn_editar, btn_excluir))

            # Salva novamente as tarefas no arquivo
            salvar_tarefas()
            break

def editar_tarefa(checkbox):
    """Permite editar o texto da tarefa"""
    # Cria uma nova janela para a edição do texto
    def salvar_edicao():
        novo_texto = entrada_edicao.get()  # Pega o texto digitado
        if novo_texto:
            checkbox.configure(text=novo_texto)  # Atualiza o texto da checkbox
            salvar_tarefas()  # Salva as alterações no arquivo
            edicao_window.destroy()  # Fecha a janela de edição
        else:
            print("Digite um texto válido.")

    edicao_window = ctk.CTkToplevel()  # Cria uma nova janela (Toplevel)
    edicao_window.title("Editar Tarefa")

    entrada_edicao = ctk.CTkEntry(edicao_window, placeholder_text="Novo texto da tarefa")
    entrada_edicao.pack(pady=10)

    btn_salvar_edicao = CTkButton(edicao_window, text="Salvar", command=salvar_edicao)
    btn_salvar_edicao.pack(pady=10)

def mostrar_grafico():
    """Função que cria o gráfico com as tarefas marcadas e não marcadas"""
    # Contabiliza as tarefas marcadas e não marcadas
    marcadas = sum([1 for c, _, _ in checkboxes if c.get()])
    nao_marcadas = len(checkboxes) - marcadas

    # Cria o gráfico
    tarefas = ['Metas finalizadas', 'Metas não finalizadas']
    valores = [marcadas, nao_marcadas]

    plt.figure(figsize=(6, 4))
    plt.bar(tarefas, valores, color=['green', 'red'])
    plt.title("Status das Tarefas")
    plt.xlabel("Tarefa")
    plt.ylabel("Quantidade")
    plt.show()

# App
app = ctk.CTk()
app.title("To-do List")
app.geometry("480x610")
app.resizable(False, False)
ctk.set_appearance_mode("dark")

# Campo de entrada
entrada = ctk.CTkEntry(app, placeholder_text="Crie sua nota aqui...", height=26, width=286)
entrada.place(x=50, y=120)

# Texto do titulo
txt = CTkLabel(app, text="To-do List", text_color="white",font=("Arial", 72, "bold"))
txt.place(x=70,y=20)

# Frames para design do titulo
f1 = CTkFrame(app,width=350,height=5, fg_color="white")
f1.place(x=70, y=93)
f2 = CTkFrame(app,width=350,height=5, fg_color="white")
f2.place(x=70, y=25)

# Botão para adicionar tarefas
b = CTkButton(app, text="Adicionar", command=adicionar_tarefa, fg_color="white", text_color="#3b3c36", hover_color="#E0E0E0", font=("Arial", 18, "bold"), height=14, width=20)
b.place(x=350, y=120)

# Frame para armazenar as tarefas (checkboxes) com a rolagem
frame_tarefas = ctk.CTkScrollableFrame(app, width=375, height=350)  # Definindo width e height diretamente no construtor
frame_tarefas.place(x=50, y=166)

# Botão para mostrar gráfico
btn_grafico = CTkButton(app, text="Mostrar Gráfico", command=mostrar_grafico, fg_color="white", text_color="#3b3c36", hover_color="#E0E0E0", font=("Arial", 12, "bold"), height=40, width=80)
btn_grafico.place(x=185, y=550)

# Carrega as tarefas ao iniciar o aplicativo
carregar_tarefas()

app.mainloop()
