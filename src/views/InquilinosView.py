from src.controllers.InquilinoController import InquilinoController
from src.utils.idCreator import gerar_inq_id
import src.storage.imovel_json as imo


InquilinoController = InquilinoController()
# Cria UI para área inquilinos


def InquilinosView(parent):
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    from src.utils.tempo import hoje  # Data atual (automatizada)
    from src.utils.validators import validar_inquilino  # Validação dos dados inseridos
    from src.storage.inquilino_json import dump, load  # Métodos de persistência JSON

    # Janela principal da view de inquilinos
    root = tk.Toplevel(parent)
    root.title("Gestão de inquilinos")
    root.geometry("920x600")
    root.configure(bg="white")
    root.resizable(False, False)

    # Função para adicionar novo inquilino
    def adicionar_inquilino():
        nome = nameEntry.get().strip().title()
        contacto = contactoEntry.get().strip().strip()
        imovel = imovelEntry.get()

        # Validar imóvel antes de adicionar inquilino
        dados_imoveis = imo.load()
        imoveis = dados_imoveis["imoveis"]
        imovel_existe = False

        for i in imoveis:
            if i["id"] == imovel and i["estado"] == False:
                imovel_existe = True

        if not imovel_existe:
            messagebox.showwarning("Aviso", "Imóvel indisponível")
            return

        # Validação básica de campos obrigatórios
        if not nome or not contacto or not imovel:
            messagebox.showwarning("Aviso", "Preencha todos os campos", parent=root)
            return

        # Adiciona o inquilino no controlador e salva os dados
        id_inquilino = gerar_inq_id()
        InquilinoController.adicionar_inquilino(id_inquilino, nome, contacto, hoje, imovel)
        ultimo = InquilinoController.inquilinos[-1]  # Recupera o último inquilino adicionado
        dump(InquilinoController)  # Salva no JSON

        # Valida os dados do inquilino
        valido = validar_inquilino(nome, contacto, hoje)

        if valido:
            # Adiciona à tabela da interface
            tree.insert("", "end", values=(ultimo.id, nome, contacto, imovel, hoje))
            messagebox.showinfo("Sucesso", "Inquilino cadastrado com sucesso", parent=root)
        else:
            messagebox.showwarning("Aviso", "Contacto Inválido", parent=root)

        # Limpa os campos após salvar
        nameEntry.delete(0, tk.END)
        contactoEntry.delete(0, tk.END)
        imovelEntry.delete(0, tk.END)

    # Função para remover um inquilino selecionado na tabela
    def remover_inquilino():
        inquilino_selecionado = tree.selection()
        if inquilino_selecionado:
            confirmado = messagebox.askyesno("Remover Inquilino", "Deseja remover este inquilino", parent=root)
            if confirmado:
                for item in inquilino_selecionado:
                    valores = tree.item(item, "values")
                    id_inquilino = valores[0]
                    tree.delete(item)  # Remove da interface
                    InquilinoController.remover_inquilino(str(id_inquilino))  # Remove do controlador
                    dump(InquilinoController)  # Atualiza o JSON
                    messagebox.showinfo("Removido", "Inquilino removido com sucesso", parent=root)
        else:
            messagebox.showwarning("Aviso", "Seleciona um inquilino para remover", parent=root)

    # Função para cancelar o cadastro
    def cancelar():
        nameEntry.delete(0, tk.END)
        contactoEntry.delete(0, tk.END)
        imovelEntry.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Cadastro cancelado", parent=root)

    # Função para atualizar dados de um inquilino
    def atualizar_inquilino():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Seleciona um inquilino para atualizar", parent=root)
            return

        item = selecionado[0]
        valores = tree.item(item, "values")

        id_inquilino = str(valores[0])
        nome_antigo = valores[1]
        contacto_antigo = valores[2]
        casa_antiga = valores[3]

        # Janela secundária para atualizar dados
        janela_update = tk.Toplevel(root)
        janela_update.title("Atualizar Inquilino")
        janela_update.geometry("300x250")
        janela_update.resizable(False, False)
        janela_update.configure(bg="white")

        # Campos preenchidos com dados antigos
        tk.Label(janela_update, text="Nome", bg="white").pack(pady=5)
        entry_nome = tk.Entry(janela_update, width=40)
        entry_nome.pack()
        entry_nome.insert(0, nome_antigo)

        tk.Label(janela_update, text="Contacto", bg="white").pack(pady=5)
        entry_contacto = tk.Entry(janela_update, width=40)
        entry_contacto.pack()
        entry_contacto.insert(0, contacto_antigo)

        tk.Label(janela_update, text="Imóvel", bg="white").pack(pady=5)
        entry_imovel = tk.Entry(janela_update, width=40)
        entry_imovel.pack()
        entry_imovel.insert(0, casa_antiga)

        # Função interna para salvar alterações
        def salvar_alteracoes():
            novo_nome = entry_nome.get()
            novo_contacto = entry_contacto.get()
            novo_imovel = entry_imovel.get()

            if not novo_nome or not novo_contacto or not novo_imovel:
                messagebox.showwarning("Aviso", "Preencha todos os campos", parent=janela_update)
                return

            InquilinoController.atualizar_inquilino(id_inquilino, novo_nome, novo_contacto, novo_imovel)
            dump(InquilinoController)

            tree.item(item, values=(id_inquilino, novo_nome, novo_contacto, novo_imovel, valores[4]))
            messagebox.showinfo("Atualizado", "Inquilino atualizado com sucesso", parent=janela_update)
            janela_update.destroy()

        # Botão para confirmar a atualização
        tk.Button(janela_update, text="Salvar", command=salvar_alteracoes, bg="#2980B9", fg="white").pack(pady=20)

    # Sidebar
    sidebar = tk.Frame(root, bg="#2C3E50", width=200)
    sidebar.pack(side="left", fill="y")

    nomelabel = tk.Label(sidebar, text="Área Inquilino", bg="#2C3E50", font=("Verdana", 15, "bold"), fg="#E0E0E0")
    nomelabel.pack(padx=10, pady=20)

    # Tabela com os inquilinos (Treeview)
    colunas = ("ID", "Nome", "Contacto", "Imóvel", "Entrada")
    tree = ttk.Treeview(root, columns=colunas, show="headings")
    for col in colunas:
        tree.heading(col, text=col, anchor="center")
        tree.column(col, width=120, anchor="center")
    tree.pack(side="bottom", pady=40, padx=40)

    # Scrollbar para a tabela
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    # Formulário de cadastro
    frame_form = tk.LabelFrame(root, text="Formulário de Cadastro", bg="white", bd=2)
    frame_form.place(x=245, y=40, width=610, height=200)

    # Campos do formulário
    nameLabel = tk.Label(frame_form, text="Nome", width=10, anchor="w", bg="white")
    nameLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    nameEntry = tk.Entry(frame_form, width=40, bd=1.5)
    nameEntry.grid(row=0, column=1)

    contactoLabel = tk.Label(frame_form, text="Contacto", width=10, anchor="w", bg="white")
    contactoLabel.grid(row=1, column=0, pady=10, padx=10, sticky="w")

    contactoEntry = tk.Entry(frame_form, width=40, bd=1.5)
    contactoEntry.grid(row=1, column=1, pady=10, padx=10, sticky="w")

    imovelLabel = tk.Label(frame_form, text="Imóvel", width=10, anchor="w", bg="white")
    imovelLabel.grid(row=2, column=0, pady=5, padx=10, sticky="w")

    imovelEntry = tk.Entry(frame_form, width=40, bd=1.5)
    imovelEntry.grid(row=2, column=1, pady=10, padx=10, sticky="w")

    # Botões de ação
    botaoSalvar = tk.Button(frame_form, text="Salvar", width=20, relief="ridge", command=adicionar_inquilino,
                            bg="#2ECC71", fg="#ECF0F1")
    botaoSalvar.place(x=425, y=10)

    botaoCancelar = tk.Button(frame_form, text="Cancelar", width=20, relief="ridge", command=cancelar,
                              bg="#7F8C8D", fg="#ECF0F1")
    botaoCancelar.place(x=425, y=60)

    # Menu de contexto (right-click)
    def mostrar_menu(event):
        item = tree.identify_row(event.y)
        if item:
            tree.selection_set(item)
            menu_popup.post(event.x_root, event.y_root)

    menu_popup = tk.Menu(root, tearoff=0)
    submenu = tk.Menu(menu_popup, tearoff=0)
    menu_popup.add_command(label="Atualizar", command=atualizar_inquilino)
    menu_popup.add_separator()
    menu_popup.add_command(label="Remover", command=remover_inquilino)
    menu_popup.add_separator()
    menu_popup.add_command(label="Pagamentos", command=None)
    menu_popup.add_separator()
    menu_popup.add_cascade(label="Mais Opções", menu=submenu)

    tree.bind("<Button-3>", mostrar_menu)

    # Função para carregar os dados salvos no JSON e preencher o Treeview
    def update_treeview():
        dados = load()
        for i in range(len(dados["inquilinos"])):
            InquilinoController.adicionar_inquilino(
                dados["inquilinos"][i]["id"],
                dados["inquilinos"][i]["nome"],
                dados["inquilinos"][i]["contacto"],
                dados["inquilinos"][i]["data_de_entrada"],
                dados["inquilinos"][i]["imovel"]
            )
            inquilino = InquilinoController.inquilinos[i]
            tree.insert("", "end", values=(inquilino.id,
                                           inquilino.nome,
                                           inquilino.contacto,
                                           inquilino.imovel,
                                           inquilino.data_de_entrada))

    # Chamada inicial para preencher a tabela ao abrir o app
    update_treeview()
