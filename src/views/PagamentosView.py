from src.controllers.PagamentoController import PagamentoController
from src.utils.idCreator import gerar_pay_id

def PagamentosView(parent):
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox

    root = tk.Toplevel(parent)
    root.title("Gestão de Pagamentos")
    root.geometry("920x600")
    root.configure(bg="white")
    root.resizable(False, False)

    # Função para adicionar pagamento
    def adicionar_pagamento():
        nome_inquilino = nomeInquilinoEntry.get()
        valor = valorEntry.get()


        # Validação
        if not id_pagamento or not nome_inquilino or not valor or not data_pagamento:
            messagebox.showwarning("Aviso", "Preencha todos os campos", parent=root)
            return

        # Insere na treeview
        tree.insert("", "end", values=(id_pagamento, nome_inquilino, valor, data_pagamento))

        # Limpa campos
        idPagamentoEntry.delete(0, tk.END)
        nomeInquilinoEntry.delete(0, tk.END)
        valorEntry.delete(0, tk.END)
        dataPagamentoEntry.delete(0, tk.END)

    # Função para remover pagamento
    def remover_pagamento():
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um pagamento para remover", parent=root)
            return

        confirmado = messagebox.askyesno("Remover Pagamento", "Deseja remover este pagamento?", parent=root)
        if confirmado:
            for item in selecionado:
                tree.delete(item)


    # Sidebar
    sidebar = tk.Frame(root, bg="#2C3E50", width=200)
    sidebar.pack(side="left", fill="y")

    label_sidebar = tk.Label(sidebar, text="Área Pagamentos", bg="#2C3E50", font=("Verdana", 15, "bold"), fg="#E0E0E0")
    label_sidebar.pack(padx=10, pady=20)

    # Treeview para pagamentos
    colunas = ("ID Pagamento", "Nome Inquilino", "Valor", "Data Pagamento")
    tree = ttk.Treeview(root, columns=colunas, show="headings")
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=130, anchor="center")
    tree.pack(side="bottom", pady=40, padx=40, fill="both")

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    # Formulário de cadastro de pagamento
    frame_form = tk.LabelFrame(root, text="Formulário de Pagamento", bg="white", bd=2)
    frame_form.place(x=260, y=40, width=610, height=200)

    # Campos do formulário
    tk.Label(frame_form, text="Nome Inquilino", width=15, anchor="w", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    nomeInquilinoEntry = tk.Entry(frame_form, width=40, bd=1.5)
    nomeInquilinoEntry.grid(row=1, column=1)

    tk.Label(frame_form, text="Valor (MZN)", width=15, anchor="w", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    valorEntry = tk.Entry(frame_form, width=40, bd=1.5)
    valorEntry.grid(row=2, column=1)


    # Botões de ação
    botaoSalvar = tk.Button(frame_form, text="Salvar", width=20, relief="ridge", command=adicionar_pagamento,
                            bg="#2ECC71", fg="#ECF0F1")
    botaoSalvar.place(x=425, y=10)

    botaoRemover = tk.Button(frame_form, text="Cancelar", width=20, relief="ridge", command=remover_pagamento,bg="#7F8C8D", fg="#ECF0F1")
    botaoRemover.place(x=425, y=60)

    root.mainloop()