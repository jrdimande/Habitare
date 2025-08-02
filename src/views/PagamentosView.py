from src.controllers.PagamentoController import PagamentoController
from src.utils.idCreator import gerar_pay_id
from src.utils.tempo import hoje
from src.storage.inquilino_json import load, open_and_dump
from src.storage.pagamento_json import dump
from src.storage.pagamento_json import load as load_pagamento
from src.storage.imovel_json import load as load_imovel

pagamento_controller = PagamentoController()
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
        id_inquilino = idInquilinoEntry.get().strip()
        valor = valorEntry.get()

        # Validação
        # Verificar se o ID especificado existe
        dados_inquilinos = load()
        inquilino_existe = False

        for i in range(len(dados_inquilinos["inquilinos"])):
            if dados_inquilinos["inquilinos"][i]["id"] == id_inquilino:
                inquilino_existe = True

        if not inquilino_existe:
            messagebox.showwarning("Aviso", "Nenhum registro correspondente ao ID especificado")
            idInquilinoEntry.delete(0, tk.END)
            return

        # Verificar se os campos estão preenchidos
        if not id_inquilino or not valor:
            messagebox.showwarning("Aviso", "Preencha todos os campos", parent=root)
            return

        # Validar valor do pagamento

        valor_valido = False
        valor_a_pagar = None

        id_imovel = None
        dados_imoveis = load_imovel()

        # Buscar o imóvel do inquilino
        for inq in dados_inquilinos["inquilinos"]:
            if inq["id"] == id_inquilino:
                id_imovel = inq["imovel"]
                break

        # Obter o valor a pagar do imóvel correspondente
        for imovel in dados_imoveis["imoveis"]:
            if imovel["id"] == id_imovel:
                valor_a_pagar = imovel["preco"]
                break

        if not valor.isdigit():
            messagebox.showwarning("Valor Inválido", "Insira um valor válido")
            valorEntry.delete(0, tk.END)
            return

        if  not valor or float(valor) != float(valor_a_pagar):
            messagebox.showwarning("Valor Incorreto", "O valor introduzido não corresponde ao valor que o inquilino deve pagar")
            return

        id_pagamento = gerar_pay_id()  # <- gerar id para pagamento
        pagamento_controller.adicionar_pagamento(id_pagamento, id_inquilino, valor, hoje)

        # Carregar dados dos inquilinos para fazer busca do inquilino com o id especificado e fazer adicionar pagamento à lista de pagamentos
        dados_inquilinos = load()
        for i in range(len(dados_inquilinos["inquilinos"])):
            if dados_inquilinos["inquilinos"][i]["id"] == id_inquilino:
                pagamento = {"id" : id_pagamento,
                             "valor" : valor,
                             "data" : hoje
                             }
                dados_inquilinos["inquilinos"][i]["pagamentos"].append(pagamento)
                open_and_dump(dados_inquilinos)

        dump(pagamento_controller)

        # Insere na treeview
        tree.insert("", "end", values=(id_pagamento, id_inquilino, valor, hoje))

        # Limpa campos
        valorEntry.delete(0, tk.END)
        idInquilinoEntry.delete(0, tk.END)

    # Função para remover pagamento
    def remover_pagamento():
        "Remove pagamento"
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione um pagamento para remover", parent=root)
            return

        confirmado = messagebox.askyesno("Remover Pagamento", "Deseja remover este pagamento?", parent=root)
        if confirmado:
            for item in selecionado:
                valores = tree.item(item, "values")
                id_pagamento = valores[0]
                id_inquilino = valores[1]
                tree.delete(item)

                # Carregar dados dos inquilinos para fazer busca do inquilino com o id especificado remover pagamento à lista de pagamentos
                dados_inquilinos = load()
                inquilinos = dados_inquilinos["inquilinos"]

                for i in inquilinos:
                    if i["id"] == id_inquilino:
                        pagamentos = i["pagamentos"]
                        for p in range(len(pagamentos)):
                            if pagamentos[p]["id"] == id_pagamento:
                                pagamentos.pop(p)
                                open_and_dump(dados_inquilinos)
                pagamento_controller.remover_pagamento(id_pagamento, id_inquilino)
                dump(pagamento_controller)


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
    tk.Label(frame_form, text="ID Inquilino", width=15, anchor="w", bg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    idInquilinoEntry = tk.Entry(frame_form, width=40, bd=1.5)
    idInquilinoEntry.grid(row=1, column=1)

    tk.Label(frame_form, text="Valor (MZN)", width=15, anchor="w", bg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    valorEntry = tk.Entry(frame_form, width=40, bd=1.5)
    valorEntry.grid(row=2, column=1)


    # Botões de ação
    botaoSalvar = tk.Button(frame_form, text="Salvar", width=20, relief="ridge", command=adicionar_pagamento,
                            bg="#2ECC71", fg="#ECF0F1")
    botaoSalvar.place(x=425, y=10)

    botaoRemover = tk.Button(frame_form, text="Cancelar", width=20, relief="ridge", command=remover_pagamento,bg="#7F8C8D", fg="#ECF0F1")
    botaoRemover.place(x=425, y=60)




    def mostrar_menu(event):
        item = tree.identify_row(event.y)
        if item:
            tree.selection()
            menu_popup.post(event.x_root, event.y_root)


    menu_popup = tk.Menu(root, tearoff=0)
    menu_popup.add_command(label="Remover", command=remover_pagamento)
    tree.bind("<Button-3>",  mostrar_menu)



    def update_treeview():
        dados_pagamentos = load_pagamento()
        for p in range(len(dados_pagamentos["pagamentos"])):
            pagamento_controller.adicionar_pagamento(
                dados_pagamentos["pagamentos"][p]["id"],
                dados_pagamentos["pagamentos"][p]["id_inquilino"],
                dados_pagamentos["pagamentos"][p]["valor"],
                dados_pagamentos["pagamentos"][p]["data"]
            )
            pagamento = pagamento_controller.pagamentos[p]
            #tree.insert("", "end", values=(id_pagamento, id_inquilino, valor, hoje))
            tree.insert("", "end", values=(pagamento.id_pagamento, pagamento.id_inquilino, pagamento.valor, pagamento.data_de_pagamento))

    update_treeview()

    botao_carregar = tk.Button(frame_form, text="Carregar", width=20, relief="ridge", command=update_treeview, bg=None, fg=None)
    botao_carregar.place(x=425, y=100)

    root.mainloop()